import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
import yaml


def _utc_now() -> str:
    """Return an unambiguous, timezone-aware timestamp with microseconds."""
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _read_frontmatter(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            raw = handle.read()
        if not raw.startswith("---"):
            return {}
        _, frontmatter, _body = raw.split("---", 2)
        parsed = yaml.safe_load(frontmatter)
        return parsed if isinstance(parsed, dict) else {}
    except (OSError, ValueError, yaml.YAMLError):
        return {}


def archive_okf_file(filepath: str, knowledge_dir: str | None = None) -> str | None:
    """Copy a live OKF file to the append-only ``.history`` repository."""
    if not os.path.isfile(filepath):
        return None

    live_path = Path(filepath).resolve()
    root = Path(knowledge_dir).resolve() if knowledge_dir else live_path.parent.parent
    try:
        relative = live_path.relative_to(root)
    except ValueError:
        relative = Path(live_path.name)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    archive_dir = root / ".history" / relative.parent / relative.stem
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path = archive_dir / f"{stamp}{relative.suffix}"
    shutil.copy2(live_path, archive_path)
    return str(archive_path)


def _metadata_for_write(metadata: dict, filepath: str) -> dict:
    """Preserve creation time and assign a precise time for this revision."""
    result = dict(metadata)
    previous = _read_frontmatter(filepath) if os.path.isfile(filepath) else {}
    now = _utc_now()
    result["created_at"] = previous.get("created_at") or result.get("created_at") or now
    result["updated_at"] = now
    return result

def format_okf_string(text: str, metadata: dict) -> str:
    """
    Takes raw text and a metadata dictionary and constructs a valid OKF string.
    OKF Standard = YAML frontmatter wrapped in '---' followed by Markdown body.
    """
    try:
        # Convert the dictionary to a YAML string. 
        # sort_keys=False preserves the order defined in our Pydantic model.
        frontmatter = yaml.dump(metadata, sort_keys=False, allow_unicode=True)
    except Exception as e:
        print(f"⚠️ Warning: Could not serialize metadata to YAML. Error: {e}")
        frontmatter = "title: Unknown\n"

    # Assemble the final OKF standard document
    okf_content = f"---\n{frontmatter}---\n\n{text}"
    return okf_content

def format_and_save_okf(text: str, metadata: dict, output_dir: str, filename: str) -> str:
    """
    Generates an OKF document and physically saves it to the disk.
    This fulfills the requirement of 'preventing vendor lock-in' by creating portable files.
    """
    # Ensure the target directory exists (e.g., 'knowledge/source_1/')
    os.makedirs(output_dir, exist_ok=True)
    
    # Construct the full file path
    filepath = os.path.join(output_dir, filename)

    metadata = _metadata_for_write(metadata, filepath)
    okf_content = format_okf_string(text, metadata)
    
    # Write the file to disk using UTF-8 to support diverse text characters
    try:
        archive_okf_file(filepath, knowledge_dir=output_dir)
        temp_path = f"{filepath}.tmp"
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(okf_content)
        os.replace(temp_path, filepath)
    except IOError as e:
        print(f"❌ Error writing OKF file to disk: {e}")
        raise
        
    return filepath
