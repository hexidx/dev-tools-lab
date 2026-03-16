# AGENT RULES

You are working in a public repository designed for safe autonomous micro-contributions.

## Main objective
Pick one small task from BACKLOG.md and complete it safely.

## Allowed work
- tests
- docs
- small CLI utilities
- validators
- parsers
- formatting helpers
- refactors limited to a few files
- developer scripts

## Not allowed
- secrets
- auth systems
- deployment/infrastructure changes
- destructive file deletions unless clearly required
- large architectural rewrites
- dependency churn without clear need

## Task size
Choose only tasks that can reasonably be completed in one session as a small PR.

## Workflow
1. Read BACKLOG.md
2. Pick one small task
3. Create a new branch
4. Implement the task
5. Run tests and lint
6. Update docs if needed
7. Commit with a clear message
8. Open a PR with a concise summary

## Quality bar
- keep changes small and localized
- preserve existing behavior unless task requires change
- add or update tests whenever possible
- do not submit empty or cosmetic-only changes

## Commit style
Use one of:
- feat(...)
- fix(...)
- refactor(...)
- test(...)
- docs(...)
- chore(...)

## PR requirements
Include:
- summary
- why
- validation
- risk
