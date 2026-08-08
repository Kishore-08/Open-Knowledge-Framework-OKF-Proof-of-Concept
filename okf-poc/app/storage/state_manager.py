"""
State management for ingestion pipeline.

Tracks processed files, content hashes, and processing state to enable
incremental ingestion and avoid re-processing unchanged documents.
"""

import hashlib
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class StateManager:
    """Manages processing state for incremental ingestion."""

    def __init__(self, cache_dir: str):
        """
        Initialize state manager.
        
        Args:
            cache_dir: Root cache directory where .state/ subdirectory will be created
        """
        self.cache_dir = cache_dir
        self.state_dir = os.path.join(cache_dir, ".state")
        os.makedirs(self.state_dir, exist_ok=True)

    def _state_path(self, state_file: str = "processing.json") -> str:
        """Get path to a state file."""
        return os.path.join(self.state_dir, state_file)

    def load_processing_state(self) -> Dict:
        """
        Load processing state for local raw documents.
        
        Returns:
            Dictionary with 'files' mapping relative paths to file metadata
        """
        path = self._state_path("processing.json")

        if not os.path.exists(path):
            return {"files": {}}

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, dict) else {"files": {}}
        except (OSError, json.JSONDecodeError) as exc:
            print(f"⚠️ Could not load processing state from {path}: {exc}")
            return {"files": {}}

    def save_processing_state(self, state: Dict) -> None:
        """
        Save processing state atomically.
        
        Args:
            state: State dictionary to persist
        """
        path = self._state_path("processing.json")
        temp_path = f"{path}.tmp"

        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, sort_keys=True)

        os.replace(temp_path, path)

    def load_crawler_state(self, source_name: str) -> Dict[str, Dict]:
        """
        Load crawler synchronization state for a documentation source.
        
        Args:
            source_name: Name of the documentation source
            
        Returns:
            Dictionary mapping URLs to their metadata (etag, content_hash, etc.)
        """
        path = self._state_path(f"{self._safe_name(source_name)}.json")

        if not os.path.exists(path):
            return {}

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                return {}

            return data.get("pages", {})

        except (OSError, json.JSONDecodeError) as exc:
            print(f"⚠️ Could not load crawler state from {path}: {exc}")
            return {}

    def save_crawler_state(self, source_name: str, pages: Dict[str, Dict]) -> None:
        """
        Save crawler synchronization state atomically.
        
        Args:
            source_name: Name of the documentation source
            pages: Dictionary mapping URLs to their metadata
        """
        path = self._state_path(f"{self._safe_name(source_name)}.json")
        temp_path = f"{path}.tmp"

        payload = {
            "version": 1,
            "source": source_name,
            "pages": pages,
        }

        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, sort_keys=True)

        os.replace(temp_path, path)

    def get_all_crawler_states(self) -> List[Dict]:
        """
        Load all crawler state files to recover cached pages.
        
        Returns:
            List of page dictionaries with source_name, url, raw_path
        """
        pages: List[Dict] = []

        if not os.path.isdir(self.state_dir):
            return pages

        for filename in sorted(os.listdir(self.state_dir)):
            if not filename.endswith(".json") or filename == "processing.json":
                continue

            state_path = os.path.join(self.state_dir, filename)
            try:
                with open(state_path, "r", encoding="utf-8") as f:
                    payload = json.load(f) or {}

                source_name = payload.get("source") or os.path.splitext(filename)[0]

                for url, meta in (payload.get("pages") or {}).items():
                    raw_file = (meta or {}).get("raw_file")
                    if not raw_file:
                        continue

                    html_path = os.path.join(self.cache_dir, raw_file)
                    if os.path.isfile(html_path):
                        pages.append({
                            "source_name": source_name,
                            "url": url,
                            "raw_path": html_path,
                        })

            except Exception as exc:
                print(f"⚠️ Could not read crawler state {state_path}: {exc}")

        return pages

    def discover_local_files(self, supported_extensions: Optional[List[str]] = None) -> List[str]:
        """
        Find manually supplied raw documents in cache directory.
        
        Args:
            supported_extensions: List of file extensions to include (e.g., ['.pdf', '.md'])
                                 Defaults to ['.pdf', '.md', '.txt', '.json']
        
        Returns:
            List of absolute file paths
        """
        if supported_extensions is None:
            supported_extensions = [".pdf", ".md", ".txt", ".json"]

        supported = set(supported_extensions)
        files = []

        if not os.path.isdir(self.cache_dir):
            return files

        for root, _, filenames in os.walk(self.cache_dir):
            # Skip state directory and crawler HTML subdirectories
            if ".state" in Path(root).parts:
                continue

            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in supported:
                    files.append(os.path.join(root, filename))

        return sorted(files)

    def get_changed_files(self, previous_state: Optional[Dict] = None) -> Tuple[List[str], Dict]:
        """
        Identify files that changed since the previous run.
        
        Args:
            previous_state: Previous state dict, or None to load from disk
            
        Returns:
            Tuple of (changed_file_paths, updated_state)
        """
        if previous_state is None:
            previous_state = self.load_processing_state()

        previous_files = previous_state.setdefault("files", {})
        changed_files = []
        current_files = set()

        for path in self.discover_local_files():
            relative_path = os.path.relpath(path, self.cache_dir)
            current_files.add(relative_path)

            content_hash = self._file_hash(path)
            previous = previous_files.get(relative_path, {})

            if previous.get("content_hash") != content_hash:
                changed_files.append(path)

        # Remove state entries for files that no longer exist
        for relative_path in list(previous_files):
            if relative_path not in current_files:
                del previous_files[relative_path]

        return changed_files, previous_state

    def update_file_state(self, file_path: str, okf_file: str, state: Optional[Dict] = None) -> Dict:
        """
        Update state for a processed file.
        
        Args:
            file_path: Absolute path to the source file
            okf_file: Name of the generated OKF file
            state: Current state dict, or None to load from disk
            
        Returns:
            Updated state dict
        """
        if state is None:
            state = self.load_processing_state()

        relative_path = os.path.relpath(file_path, self.cache_dir)
        state["files"][relative_path] = {
            "content_hash": self._file_hash(file_path),
            "okf_file": okf_file,
        }

        return state

    @staticmethod
    def _file_hash(path: str) -> str:
        """Compute SHA-256 hash of file content."""
        digest = hashlib.sha256()

        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                digest.update(chunk)

        return digest.hexdigest()

    @staticmethod
    def _safe_name(name: str) -> str:
        """Convert source name to filesystem-safe filename."""
        import re
        return re.sub(r"[^a-zA-Z0-9-_]+", "-", name).strip("-").lower() or "source"
