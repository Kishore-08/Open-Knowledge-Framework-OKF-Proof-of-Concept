from app.okf.repository import search_concepts


def test_short_query_token_does_not_match_inside_unrelated_words(tmp_path):
    concept = tmp_path / "linux" / "autoscaler.md"
    concept.parent.mkdir()
    concept.write_text(
        """---
id: autoscaler
type: concept
title: Autoscaler
description: Host autoscaler implementation
category: linux
source:
  name: test
  url: https://example.com/autoscaler
---
Host autoscaler implementation.
""",
        encoding="utf-8",
    )

    assert search_concepts("OS", knowledge_dir=str(tmp_path)) == []
