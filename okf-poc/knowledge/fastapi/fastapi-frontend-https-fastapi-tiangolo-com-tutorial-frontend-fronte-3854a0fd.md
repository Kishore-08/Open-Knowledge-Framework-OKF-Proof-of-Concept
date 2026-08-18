---
id: fastapi-frontend-https-fastapi-tiangolo-com-tutorial-frontend-fronte-3854a0fd
type: concept
title: 'Frontend[¶](https://fastapi.tiangolo.com/tutorial/frontend/#frontend "Permanent '
description: You can serve static frontend apps with `app.frontend()` (or `router.frontend()`).
category: fastapi
tags: []
source:
  name: fastapi
  url: https://fastapi.tiangolo.com/tutorial/frontend/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Frontend[¶](https://fastapi.tiangolo.com/tutorial/frontend/#frontend "Permanent link")

You can serve static frontend apps with `app.frontend()` (or `router.frontend()`).

This is useful for frontend tools that generate static files, like React with Vite, TanStack Router, Astro, Vue, Svelte, Angular, Solid, and others.

With these tools, you normally have a step that builds the frontend, with a command like:

```
npm run build
```

That would generate a directory like `./dist/` with your frontend files.

You can use `app.frontend()` to serve that directory following the conventions needed by these frontend frameworks.

**FastAPI** checks *path operations* first. The frontend files are checked only if no normal route matched, so your API won't be affected.