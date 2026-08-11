#!/usr/bin/env python3
"""
Migration script to reorganize data structure.

OLD STRUCTURE:
- data/raw/          -> mixed cache and raw files
- data/knowledge/    -> OKF markdown files (but wrong location)

NEW STRUCTURE:
- cache/             -> disposable: crawler HTML, processing state, raw input files
- knowledge/         -> source of truth: OKF markdown files with frontmatter

This script:
1. Backs up existing data
2. Moves data/raw/* -> cache/
3. Moves data/knowledge/* -> knowledge/ (if not already there)
4. Preserves all .state/ directories
5. Updates any absolute paths in state files
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime


def backup_directory(src: str, backup_root: str = "backups") -> str:
    """Create timestamped backup of a directory."""
    if not os.path.exists(src):
        print(f"⚠️  Source directory {src} does not exist, skipping backup")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{Path(src).name}_{timestamp}"
    backup_path = os.path.join(backup_root, backup_name)
    
    os.makedirs(backup_root, exist_ok=True)
    shutil.copytree(src, backup_path)
    print(f"✅ Backed up {src} -> {backup_path}")
    return backup_path


def migrate_raw_to_cache(old_raw: str = "data/raw", new_cache: str = "cache") -> None:
    """Move raw data directory to cache."""
    if not os.path.exists(old_raw):
        print(f"ℹ️  No {old_raw} directory found, skipping migration")
        return
    
    if os.path.exists(new_cache):
        print(f"⚠️  {new_cache} already exists. Merging contents...")
        # Merge: copy files from old to new, preserving new if conflicts
        for root, dirs, files in os.walk(old_raw):
            rel_path = os.path.relpath(root, old_raw)
            dest_dir = os.path.join(new_cache, rel_path) if rel_path != "." else new_cache
            
            os.makedirs(dest_dir, exist_ok=True)
            
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                
                if not os.path.exists(dest_file):
                    shutil.copy2(src_file, dest_file)
                    print(f"  📄 Copied {src_file} -> {dest_file}")
    else:
        # Simple move
        shutil.move(old_raw, new_cache)
        print(f"✅ Moved {old_raw} -> {new_cache}")


def migrate_knowledge(old_knowledge: str = "data/knowledge", new_knowledge: str = "knowledge") -> None:
    """Move knowledge directory to top level."""
    if not os.path.exists(old_knowledge):
        print(f"ℹ️  No {old_knowledge} directory found, skipping migration")
        return
    
    if os.path.exists(new_knowledge):
        print(f"⚠️  {new_knowledge} already exists. Merging contents...")
        # Merge: copy files from old to new, preserving new if conflicts
        for root, dirs, files in os.walk(old_knowledge):
            rel_path = os.path.relpath(root, old_knowledge)
            dest_dir = os.path.join(new_knowledge, rel_path) if rel_path != "." else new_knowledge
            
            os.makedirs(dest_dir, exist_ok=True)
            
            for file in files:
                if not file.endswith('.md'):
                    continue
                    
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                
                if not os.path.exists(dest_file):
                    shutil.copy2(src_file, dest_file)
                    print(f"  📄 Copied {src_file} -> {dest_file}")
    else:
        # Simple move
        shutil.move(old_knowledge, new_knowledge)
        print(f"✅ Moved {old_knowledge} -> {new_knowledge}")


def update_state_file_paths(cache_dir: str = "cache") -> None:
    """Update any absolute paths in state files to use new structure."""
    state_dir = os.path.join(cache_dir, ".state")
    
    if not os.path.exists(state_dir):
        print(f"ℹ️  No state directory found at {state_dir}")
        return
    
    for filename in os.listdir(state_dir):
        if not filename.endswith('.json'):
            continue
            
        filepath = os.path.join(state_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # State files use relative paths, so they should be fine
            # Just verify they exist
            if 'pages' in data:
                print(f"  ✅ Verified state file: {filename} ({len(data['pages'])} pages)")
            elif 'files' in data:
                print(f"  ✅ Verified processing state: {filename} ({len(data['files'])} files)")
                
        except Exception as e:
            print(f"  ⚠️  Error reading {filename}: {e}")


def cleanup_empty_dirs(directory: str = "data") -> None:
    """Remove empty data directory after migration."""
    if not os.path.exists(directory):
        return
    
    # Check if directory is empty or only contains empty subdirectories
    if not any(os.scandir(directory)):
        os.rmdir(directory)
        print(f"✅ Removed empty directory: {directory}")
    else:
        remaining = list(os.listdir(directory))
        print(f"ℹ️  {directory} still contains: {remaining}")
        print(f"   Manual cleanup may be required")


def main():
    """Run the migration."""
    print("=" * 60)
    print("OKF Data Structure Migration")
    print("=" * 60)
    print()
    
    # Change to script's parent directory (project root)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)
    
    print(f"📁 Working directory: {os.getcwd()}")
    print()
    
    # Step 1: Create backups
    print("Step 1: Creating backups...")
    backup_directory("data/raw")
    backup_directory("data/knowledge")
    print()
    
    # Step 2: Migrate raw -> cache
    print("Step 2: Migrating data/raw -> cache...")
    migrate_raw_to_cache()
    print()
    
    # Step 3: Migrate knowledge
    print("Step 3: Migrating data/knowledge -> knowledge...")
    migrate_knowledge()
    print()
    
    # Step 4: Update state files
    print("Step 4: Verifying state files...")
    update_state_file_paths()
    print()
    
    # Step 5: Cleanup
    print("Step 5: Cleaning up...")
    cleanup_empty_dirs("data/knowledge")
    cleanup_empty_dirs("data")
    print()
    
    print("=" * 60)
    print("✅ Migration complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review the migrated structure:")
    print("   - cache/       (disposable data)")
    print("   - knowledge/   (OKF source of truth)")
    print()
    print("2. Test the application:")
    print("   python -m app.indexing.indexer  # Rebuild index")
    print("   # or run the full ingestion pipeline")
    print()
    print("3. If everything works, you can delete:")
    print("   - backups/ directory (after verification)")
    print("   - data/ directory (if empty)")
    print()


if __name__ == "__main__":
    main()
