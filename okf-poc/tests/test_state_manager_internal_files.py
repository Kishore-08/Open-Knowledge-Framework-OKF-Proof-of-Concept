from app.storage.state_manager import StateManager


def test_discover_local_files_excludes_internal_hidden_directories(tmp_path):
    (tmp_path / ".jobs").mkdir()
    (tmp_path / ".state").mkdir()
    (tmp_path / ".jobs" / "936d182c9cf6.json").write_text("{}", encoding="utf-8")
    (tmp_path / ".state" / "processing.json").write_text("{}", encoding="utf-8")
    uploaded = tmp_path / "guide.json"
    uploaded.write_text('{"title": "Real guide"}', encoding="utf-8")

    assert StateManager(str(tmp_path)).discover_local_files() == [str(uploaded)]
