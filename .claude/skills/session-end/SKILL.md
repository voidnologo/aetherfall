---
name: session-end
description: Finalize the current session by completing session notes, updating the pending task list, and refreshing the continuation prompt. Use when the user says "end session", "wrap up", "save my progress", "close out this session", "done for now", or wants to preserve their work state before ending a conversation.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# End Session

Finalize the current session by completing the session notes, updating the pending task list, and refreshing the continuation prompt.

## Workflow

### 1. Identify Current Session

Find the latest session notes file:

```bash
ls -1 docs/sessions/session-*-notes.md | sort -t- -k2 -n | tail -1
```

### 2. Finalize Session Notes

Update `docs/sessions/session-{N}-notes.md` with complete information:

- **Title**: Replace "TBD" with a descriptive title summarizing the session's main work
- **Goal**: Fill in if still placeholder
- **Overview**: 1-2 paragraph summary of what was accomplished and why
- **Changes Made**: Organized by topic/feature area
- **Files Modified**: Complete table of every file changed with brief descriptions
- **Key Design Decisions**: Document any non-obvious choices with rationale ("why", not "what")
- **Open Issues**: Anything unfinished, ideas discovered, or items needing follow-up
- **Next Session**: Forward pointer to logical next work

To populate the files modified table, check git:

```bash
git diff --name-only HEAD~5 -- '*.md' '*.html' '*.css' '*.json' '*.py' 2>/dev/null
```

### 3. Update Pending Tasks

Update `docs/pending-tasks.md`:

- **Check off** any tasks completed this session: `- [x] Task name`
- **Remove** all completed (`[x]`) items — they are now in the session notes, which are the permanent record
- **Add** any new tasks or ideas discovered during the session (to the appropriate section)
- **Reorder** Next Up if priorities have shifted

### 4. Update Continuation Prompt

Update `docs/continuation-prompt.md` (keep it lean — target ~30-40 lines):

- **Update "Last Session"**: Change to reference the current session number and title
- **Update last session summary**: 2-4 bullet points of what was done
- **Update "Current State"**: Reflect what was accomplished — mark newly completed areas, add new incomplete areas
- **Update "Immediate Next Task"**: What to tackle next, based on pending-tasks.md
- **Update "Key References"**: Add new docs created this session, remove stale references
- Do NOT add session history or detailed design rationale — those live in `docs/sessions/` and `docs/requirements/`

### 5. Report

Summarize to the user:
- Session title and date
- Key accomplishments (3-5 bullet points)
- Open items carried forward (now in pending-tasks.md)
- Suggested next session focus
- Remind user to commit if they haven't already

## Notes

- Session notes are the permanent historical record — be thorough there
- The continuation prompt is for fast resumption — keep it short and current
- pending-tasks.md is a live checklist — check off done items and add new ones
- Requirements docs in `docs/requirements/` are the authoritative design specs — update those when design decisions are finalized during the session
