---
id: fastapi-ai-agent-skills-https-fastapi-tiangolo-com-tutorial-ai-agent-d77ca978
type: concept
title: AI Agent Skills[¶](https://fastapi.tiangolo.com/tutorial/#ai-agent-skills "Permanent
  link")
description: FastAPI includes an official skill for AI coding agents. It is bundled
  with the package, so its guidance stays aligned with the version of FastAPI installed
  in your project and updates when you update
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## AI Agent Skills[¶](https://fastapi.tiangolo.com/tutorial/#ai-agent-skills "Permanent link")

FastAPI includes an official skill for AI coding agents. It is bundled with the package, so its guidance stays aligned with the version of FastAPI installed in your project and updates when you update FastAPI.

After installing FastAPI in your project, you can install the skill with [Library Skills](https://library-skills.io):

```
uvx library-skills
```

Note

`uvx` is an alias for `uv tool run`. It runs Library Skills in a temporary, isolated environment while Library Skills scans the packages installed in your project.

The skill is compatible with Codex, Claude Code, Cursor, GitHub Copilot, Gemini CLI, Pi, OpenCode, and most other coding agents. For Claude Code, select `.claude/skills` when asked where to install the skill.