import os
import yaml

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
    
    # Generate the OKF formatted string
    okf_content = format_okf_string(text, metadata)
    
    # Construct the full file path
    filepath = os.path.join(output_dir, filename)
    
    # Write the file to disk using UTF-8 to support diverse text characters
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(okf_content)
    except IOError as e:
        print(f"❌ Error writing OKF file to disk: {e}")
        raise
        
    return filepath