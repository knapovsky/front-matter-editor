# Front Matter Editor

A small Python utility for bulk-editing YAML front matter in Markdown/Jekyll-style posts. It was used to normalise metadata for a selected folder of Markdown files, especially note/chord sheets.

> Status: personal utility / archived script.
>
> The script overwrites files in place. Always run it on a temporary copy first.

## Features

- loads Markdown files with YAML front matter
- rewrites the `title` from the filename
- adds or removes tags
- adds a `Chords` tag for chord-sheet files
- sets date, dateCreated, description, editor, and slug fields
- writes the modified Markdown back as UTF-8

## Repository structure

```text
.
├── fix-front-matter.py   # Bulk front-matter editing script
├── .vscode/              # Local editor settings
└── .gitignore
```

## Requirements

- Python 3
- `python-frontmatter`

Install dependency:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install python-frontmatter
```

## Usage

1. Create a temporary `input/` folder.
2. Copy only the Markdown files you want to modify into that folder.
3. Edit the input parameters near the top of `fix-front-matter.py`:

   ```python
   folder = 'input/'
   add_tag = 'Notesheet'
   remove_tag = ''
   ```

4. Run the script:

   ```bash
   python3 fix-front-matter.py
   ```

5. Review the changed files before copying them back to the original collection.

## Safety notes

The script is intentionally simple and destructive:

- it overwrites every file in the configured folder
- it assumes Markdown filenames ending in `.md`
- it assumes `tags` is a list-like metadata field when present
- it has hard-coded dates and metadata values

Use git or a separate backup folder before running it.

## License

No explicit license is included. Treat the code as all rights reserved unless a license is added by the repository owner.
