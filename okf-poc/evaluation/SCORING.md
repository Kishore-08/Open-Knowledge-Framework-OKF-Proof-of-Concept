# Evaluation scoring

The evaluation preserves each raw Ragas metric and uses a grounding-first
composite for the PoC's 80% success requirement:

| Metric | Weight |
|---|---:|
| Answer correctness | 25% |
| Faithfulness | 30% |
| Context recall | 25% |
| Context precision | 10% |
| Answer relevancy | 10% |

The score is:

`100 × Σ(metric mean × metric weight)`

This weighting reflects the PoC's stated goal of a hallucination-resistant
enterprise knowledge assistant: faithfulness and retrieval coverage are as
important as matching one concise reference answer. Raw answer correctness is
reported separately and is never replaced or relabeled.

Citation quality remains a separately reported deterministic diagnostic. It is
not part of the success composite because the current citation check requires a
verbatim source title or URL and can undercount valid numbered citations.
