## ADDED Requirements

### Requirement: Check targets
The tool SHALL accept any number of paths. A directory MUST be checked note by note (every `*.md` directly inside it) and for orphans. A single Markdown file MUST be checked on its own, without the orphan check. Without arguments the tool SHALL check `notes/`.

#### Scenario: Directory given
- **WHEN** the tool is run with `notes/`
- **THEN** every note in `notes/` is checked, including the orphan check

#### Scenario: Single file given
- **WHEN** the tool is run with `notes/plan-mode.md` and that note is not linked anywhere
- **THEN** no orphan problem is reported

### Requirement: Frontmatter
Every note MUST start with YAML frontmatter delimited by `---` containing the non-empty fields `titel`, `typ`, `tags` and `stand`. `typ` MUST be one of `entscheidung`, `how-to`, `wissen`, `glossar`, `frage`. `tags` MUST be a list. `stand` MUST be a date in the form `YYYY-MM-DD`.

#### Scenario: Field missing
- **WHEN** a note has no `typ` field
- **THEN** the tool reports `Pflichtfeld 'typ' fehlt` for that note

#### Scenario: Invalid YAML
- **WHEN** the frontmatter cannot be parsed as YAML
- **THEN** the tool reports that the frontmatter is not valid YAML instead of failing

### Requirement: No H1 headings
A note SHALL NOT contain a level-one heading (`# `) outside fenced code blocks, because the title lives in the frontmatter.

#### Scenario: H1 in the body
- **WHEN** line 10 of a note starts with `# `
- **THEN** the tool reports an H1 problem for line 10

#### Scenario: Comment in a code block
- **WHEN** a line starting with `# ` is inside a fenced code block
- **THEN** no problem is reported

### Requirement: Wikilinks resolve
Every wikilink `[[target]]`, including the forms `[[target|alias]]` and `[[target#heading]]`, MUST point to a note in the same directory or to a Markdown file in the handbook root.

#### Scenario: Broken link
- **WHEN** a note links `[[gibt-es-nicht]]` and no such file exists
- **THEN** the tool reports `Wikilink [[gibt-es-nicht]] zeigt ins Leere` with the line number

### Requirement: No orphans
When a directory is checked, every note MUST be linked from `index.md` in the handbook root or from at least one other note. A link from a note to itself does not count.

#### Scenario: Unlinked note
- **WHEN** a note is linked neither from `index.md` nor from another note
- **THEN** the tool reports it as orphaned

### Requirement: Output and exit code
The tool SHALL print one line per problem in the form `path:line: message`, sorted by path and line, and exit with code 1. Without problems it SHALL print a confirmation with the number of checked notes and exit with code 0.

#### Scenario: Clean handbook
- **WHEN** no problems are found in four notes
- **THEN** the tool prints `OK — 4 Notiz(en) geprüft` and exits with 0
