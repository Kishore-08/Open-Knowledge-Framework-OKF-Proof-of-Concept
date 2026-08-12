import os
import json
import hashlib
import time

from app.core.config import settings
from app.okf.repository import load_concepts_from_paths
from app.indexing.indexer import concepts_to_documents
from app.retrieval.hybrid_search import index_documents
from app.retrieval.query_engine import configure_llm_settings


STATE_FILE = "cache/.state/qdrant_backfill.json"


def file_hash(path: str) -> str:
    h = hashlib.sha256()

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)

    return h.hexdigest()


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(state):
    os.makedirs(
        os.path.dirname(STATE_FILE),
        exist_ok=True,
    )

    temp_file = STATE_FILE + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(
            state,
            f,
            indent=2,
        )

    os.replace(
        temp_file,
        STATE_FILE,
    )


def discover_knowledge_files():
    files = []

    for root, _, filenames in os.walk(
        settings.KNOWLEDGE_DIR
    ):
        for filename in filenames:

            if filename.endswith(".md"):

                files.append(
                    os.path.join(
                        root,
                        filename,
                    )
                )

    return sorted(files)


def main():

    print("🔧 Configuring Gemini embedding model...")

    configure_llm_settings()

    print(
        f"✅ Embedding model configured: "
        f"{settings.EMBEDDING_MODEL}"
    )

    files = discover_knowledge_files()

    files = discover_knowledge_files()
    files = files[:1]

    print(
        f"📚 Total knowledge files: {len(files)}"
    )

    state = load_state()

    completed = 0
    skipped = 0
    failed = 0

    for index, path in enumerate(
        files,
        start=1,
    ):

        current_hash = file_hash(path)

        previous = state.get(
            path,
            {}
        )

        if (
            previous.get("hash")
            == current_hash
            and
            previous.get("indexed")
            is True
        ):

            skipped += 1

            print(
                f"[{index}/{len(files)}] "
                f"⏭️ SKIP: {path}"
            )

            continue

        print(
            f"\n[{index}/{len(files)}] "
            f"🧠 Indexing: {path}"
        )

        try:

            concepts = load_concepts_from_paths(
                [path]
            )

            if not concepts:

                print(
                    f"⚠️ Invalid concept: {path}"
                )

                state[path] = {
                    "hash": current_hash,
                    "indexed": False,
                    "reason": "invalid_concept",
                }

                save_state(state)

                failed += 1

                continue

            docs = concepts_to_documents(
                concepts
            )

            if not docs:

                print(
                    f"⚠️ No document generated: "
                    f"{path}"
                )

                failed += 1

                continue

            _, failed_ids = index_documents(
                docs,
                collection_name=(
                    settings
                    .QDRANT_CONCEPTS_COLLECTION
                ),
                source_files=[],
                show_progress=False,
            )

            if failed_ids:

                print(
                    "❌ Embedding/index failed."
                )

                state[path] = {
                    "hash": current_hash,
                    "indexed": False,
                }

                save_state(state)

                failed += 1

                print(
                    "\n🛑 Stopping backfill "
                    "to avoid wasting Gemini quota."
                )

                break

            state[path] = {
                "hash": current_hash,
                "indexed": True,
            }

            save_state(state)

            completed += 1

            print(
                "✅ Indexed successfully"
            )

            time.sleep(1)

        except Exception as exc:

            message = str(exc)

            print(
                f"❌ Error: {message}"
            )

            state[path] = {
                "hash": current_hash,
                "indexed": False,
                "error": message,
            }

            save_state(state)

            failed += 1

            if (
                "429" in message
                or
                "quota" in message.lower()
                or
                "resource_exhausted"
                in message.lower()
            ):

                print(
                    "\n🛑 Gemini quota reached."
                )

                print(
                    "Already indexed files "
                    "have been saved."
                )

                print(
                    "Run this script again "
                    "after quota is available."
                )

                break

    print()
    print(
        "========== BACKFILL STATUS =========="
    )

    print(
        f"Total knowledge : {len(files)}"
    )

    print(
        f"Indexed this run: {completed}"
    )

    print(
        f"Already indexed : {skipped}"
    )

    print(
        f"Failed          : {failed}"
    )

    print(
        f"Remaining       : "
        f"{len(files) - completed - skipped}"
    )


if __name__ == "__main__":
    main()