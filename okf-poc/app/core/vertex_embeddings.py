from typing import Any, List

from google import genai
from google.genai import types
from llama_index.core.base.embeddings.base import BaseEmbedding
from pydantic import PrivateAttr

from app.core.config import settings
from app.core.gcp_auth import get_vertex_credentials


class VertexAIEmbedding(BaseEmbedding):
    """LlamaIndex embedding adapter backed by Vertex AI."""

    model_name: str = settings.VERTEX_EMBEDDING_MODEL
    _vertex_client: genai.Client | None = PrivateAttr(default=None)

    def _client(self) -> genai.Client:
        """Return one long-lived client for this embedding-model instance."""
        if self._vertex_client is not None:
            return self._vertex_client

        settings.validate_vertex_config()
        self._vertex_client = genai.Client(
            vertexai=True,
            project=settings.VERTEX_AI_PROJECT_ID,
            location=settings.VERTEX_AI_LOCATION,
            credentials=get_vertex_credentials(),
            http_options=types.HttpOptions(api_version="v1"),
        )
        return self._vertex_client

    @staticmethod
    def _values(response: Any) -> List[List[float]]:
        embeddings = getattr(response, "embeddings", None) or []
        if not embeddings:
            raise RuntimeError("Vertex AI returned no embeddings")
        return [list(embedding.values) for embedding in embeddings]

    def _embed(self, texts: List[str], task_type: str) -> List[List[float]]:
        # Keep a strong reference to the client for the complete request. The
        # previous chained temporary (`self._client().models...`) could be
        # finalized early by google-genai, closing its HTTP transport.
        client = self._client()
        response = client.models.embed_content(
            model=self.model_name,
            contents=texts,
            config=types.EmbedContentConfig(task_type=task_type),
        )
        return self._values(response)

    def _get_query_embedding(self, query: str) -> List[float]:
        return self._embed([query], "RETRIEVAL_QUERY")[0]

    async def _aget_query_embedding(self, query: str) -> List[float]:
        return self._get_query_embedding(query)

    def _get_text_embedding(self, text: str) -> List[float]:
        return self._embed([text], "RETRIEVAL_DOCUMENT")[0]

    def _get_text_embeddings(self, texts: List[str]) -> List[List[float]]:
        return self._embed(texts, "RETRIEVAL_DOCUMENT")

    async def _aget_text_embedding(self, text: str) -> List[float]:
        return self._get_text_embedding(text)
