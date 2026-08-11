import os
import yaml
import re
from typing import Tuple, Dict, Any

def parse_okf_string(okf_content: str) -> Tuple[Dict[str, Any], str]:
    """
    Parses an OKF string, splitting it into a metadata dictionary and the Markdown body.
    Returns: (metadata_dict, markdown_text)
    """
    # Regex to match YAML frontmatter enclosed in exactly '---' on top and bottom
    pattern = r"^\s*---\s*\n(.*?)\n\s*---\s*\n(.*)$"
    match = re.search(pattern, okf_content, re.DOTALL)
    
    if not match:
        # If no valid frontmatter is found, return empty meta and the full text as fallback
        print("⚠️ No valid OKF YAML frontmatter found in the document.")
        return {}, okf_content
    
    yaml_str = match.group(1)
    body_text = match.group(2)
    
    try:
        metadata = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError as e:
        print(f"❌ Failed to parse YAML frontmatter: {e}")
        metadata = {}
        
    return metadata, body_text.strip()

def parse_okf_file(filepath: str) -> Tuple[Dict[str, Any], str]:
    """
    Reads an OKF file from disk and parses it.
    Demonstrates that OKF files are framework-agnostic and easily readable.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"OKF file not found at path: {filepath}")
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    return parse_okf_string(content)