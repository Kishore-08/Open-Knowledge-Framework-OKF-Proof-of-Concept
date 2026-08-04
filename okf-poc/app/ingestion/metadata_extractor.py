import json
from pydantic import BaseModel, Field
from llama_index.llms.gemini import Gemini

class OKFMetadata(BaseModel):
    """
    Pydantic schema defining the strict metadata we want to extract from every document.
    This will become the YAML frontmatter in our OKF documents.
    """
    title: str = Field(description="A clear, concise title for the document.")
    summary: str = Field(description="A 2-3 sentence summary of the document's content.")
    document_type: str = Field(description="The category of the document (e.g., 'Architecture', 'API Spec', 'FAQ', 'Tutorial').")
    topics: list[str] = Field(description="A list of 3-5 key technical tags or topics covered in the text.")
    trust_level: str = Field(description="Assign 'High' if it looks like official docs, 'Medium' if general text, 'Low' if ambiguous.")

def generate_okf_metadata(text: str) -> dict:
    """
    Passes a preview of the document to an LLM to generate structured metadata.
    This satisfies Requirement #2: Metadata Extraction.
    """
    # Initialize the LLM (using a fast, cheap model for metadata generation)
    llm = Gemini(model="gemini-2.5-flash", temperature=0.1)
    
    # We only send the first 3000 characters to save tokens and time. 
    # Usually, the beginning of a document has enough context to determine title/topics.
    text_preview = text[:3000]
    
    prompt = (
        "You are an expert technical librarian. Analyze the following document text "
        "and extract the requested metadata. Output valid JSON matching the schema.\n\n"
        f"Text Preview:\n{text_preview}\n"
    )

    try:
        print("🧠 Calling LLM to extract metadata...")
        # LlamaIndex supports structured output via Pydantic integration
        response = llm.structured_predict(OKFMetadata, prompt)
        
        # Convert the Pydantic model to a standard dictionary
        metadata_dict = response.model_dump()
        return metadata_dict
        
    except Exception as e:
        print(f"❌ Failed to extract metadata: {e}")
        # Fallback metadata to ensure the pipeline doesn't crash on a bad LLM call
        return {
            "title": "Unknown Document",
            "summary": "Metadata extraction failed.",
            "document_type": "Unknown",
            "topics": ["unclassified"],
            "trust_level": "Low"
        }