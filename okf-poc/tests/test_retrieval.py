import pytest
from unittest.mock import patch, MagicMock

# Import the function we want to test
from app.retrieval.query_engine import get_query_engine

# --- Test Retrieval Orchestration ---
# We use @patch to "mock" external services.
# This ensures our CI/CD pipeline won't fail just because Docker isn't running
# or an OpenAI API key isn't set during the unit test phase.

@patch("app.retrieval.query_engine.get_qdrant_vector_store")
@patch("app.retrieval.query_engine.VectorStoreIndex")
@patch("app.retrieval.query_engine.configure_llm_settings")
def test_query_engine_initialization(mock_configure, mock_index_class, mock_get_store):
    """
    Tests if the Query Engine constructs itself correctly,
    requesting Dense semantic search and applying our custom prompts.
    """

    # 1. Setup our fake/mocked returns
    mock_vector_store = MagicMock()
    mock_get_store.return_value = mock_vector_store

    mock_index_instance = MagicMock()
    mock_index_class.from_vector_store.return_value = mock_index_instance

    mock_query_engine = MagicMock()
    mock_index_instance.as_query_engine.return_value = mock_query_engine

    # 2. Execute the function
    engine = get_query_engine(similarity_top_k=3)

    # 3. Assert the exact internal calls were made correctly

    # Did it configure the LLMs?
    mock_configure.assert_called_once()

    # Did it connect to Qdrant?
    mock_get_store.assert_called_once()

    # Did it load the index from the store?
    mock_index_class.from_vector_store.assert_called_once_with(vector_store=mock_vector_store)

    # Did it request Dense search with the correct top-k value?
    mock_index_instance.as_query_engine.assert_called_once_with(
        similarity_top_k=3,
        vector_store_query_mode="default",
    )

    # Did it attempt to inject our custom OKF prompt?
    mock_query_engine.update_prompts.assert_called_once()
