---
name: context-engineering
description: Scaffold new projects from context-engineering templates (Pydantic AI, MCP server, agent factory, template generator). Triggers on "nuevo proyecto pydantic ai", "scaffold mcp server", "crear agent factory", "context engineering template", "PRP".
---

# Context Engineering Templates

Prebuilt project templates installed at `~/.claude/templates/context-engineering/`. Use these when starting a new project that fits one of the patterns below.

## Available Templates

### `pydantic-ai/`
Build agents with Pydantic AI. Includes `CLAUDE.md` rules, PRPs, examples.
- Use when: starting a Python AI agent project with structured outputs / tool use.
- Copy: `cp -R ~/.claude/templates/context-engineering/pydantic-ai/* ./`

### `mcp-server/`
TypeScript MCP server template (Cloudflare Workers + Wrangler).
- Use when: building a new MCP server.
- Copy: `cp -R ~/.claude/templates/context-engineering/mcp-server/* ./`

### `agent-factory-with-subagents/`
Pattern for orchestrating multiple Claude Code subagents on a build.
- Use when: spinning up a multi-agent workflow with specialized roles.
- Copy: `cp -R ~/.claude/templates/context-engineering/agent-factory-with-subagents/* ./`

### `template-generator/`
Meta-template that generates new project templates.
- Use when: creating a reusable template for a recurring project shape.

### `ai-coding-workflows-foundation/`
Foundation pieces (already wired up globally as `/ce-*` commands and `ce-*` subagents).
- Source-only reference. The runtime pieces are already installed.

## Companion Pieces (Already Installed Globally)

- **Slash commands**: `/ce-create-plan`, `/ce-execute-plan`, `/ce-primer`
- **Subagents**: `ce-codebase-analyst`, `ce-validator`
- **Skill**: `build-with-agent-team` (Claude Code Agent Teams with tmux split panes)

## How to Use

1. Pick the template matching your project type.
2. Copy it into a fresh directory: `cp -R ~/.claude/templates/context-engineering/<template>/* /path/to/new-project/`
3. Edit the project's `CLAUDE.md` and `INITIAL.md` to describe the specific project.
4. Run `/ce-create-plan INITIAL.md` to generate an implementation plan (PRP).
5. Run `/ce-execute-plan <plan-path>` to execute it.

## Reference Material

- Full guide: `~/.claude/templates/context-engineering/claude-code-full-guide/`
- Sample PRP: `~/.claude/templates/context-engineering/PRPs/EXAMPLE_multi_agent_prp.md`
- Initial template: `~/.claude/templates/context-engineering/INITIAL.md`
