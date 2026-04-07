---
name: session-start
description: Start or resume a work session by loading context from previous sessions and creating a new session log file. Use when the user says "start a session", "resume work", "pick up where I left off", "new session", "continue from last time", or begins work on the Adventure TTRPG project.
allowed-tools: Read, Write, Bash, Glob
---

# Start New Session

Resume work by loading context from the previous session and creating a new session log file.

## Workflow

### 1. Determine Session Number

List existing session files and pick the next sequential number:

```bash
ls -1 docs/sessions/session-*-notes.md 2>/dev/null | sort -t- -k2 -n | tail -5
```

The new session is N+1 where N is the highest existing session number.

### 2. Read Previous Session Notes

Read `docs/sessions/session-{N}-notes.md` (the most recent one) for immediate context on what was done last and any open items.

### 3. Read Pending Tasks

Read `docs/pending-tasks.md` to see queued work (Next Up) and backlog.

### 4. Read Continuation Prompt

Read `docs/continuation-prompt.md` to understand the current project state, key references, and where things left off.

### 5. Create New Session Notes File

Create `docs/sessions/session-{N}-notes.md` with the standard template:

```markdown
# Session {N}: {Title TBD}

**Date:** {today's date, YYYY-MM-DD}
**Goal:** {to be filled in once user states their objective}

## Overview

{to be filled in as work progresses}

---

## Changes Made

{sections added as work progresses}

---

## Files Modified

| File | Change |
|------|--------|

## Key Design Decisions

## Open Issues

## Next Session
```

### 6. Brief the User

Provide a concise summary:
- **Last session** highlights (1-3 sentences from session notes)
- **Current state** from the continuation prompt (2-3 sentences)
- **Next Up** from `docs/pending-tasks.md` (what's queued)
- Ask the user what they'd like to work on this session

Then update the session notes file with the goal once the user responds.

## Notes

- Do NOT update `docs/continuation-prompt.md` at session start — that happens at session end
- The session title in the notes file can be updated later once the work direction is clear
- If the user jumps straight into work without invoking this skill, still create the session file when you notice
