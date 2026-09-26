# Add `export` Command

The ops team regularly archives build outputs for long-term storage. Add an export command following the established ops team conventions.

## What to implement

Add an `export` subcommand to `deploy.py` that:

- Accepts a required positional argument: **project name**
- Accepts a required `--pattern` argument: a glob pattern to match artifact filenames (e.g., `*.tar.gz`, `myproject-1.*.tar.gz`)
- Creates a zip of all matching files in `/builds/<project_name>/`
- Saves the zip as `/exports/<project_name>-export.zip`
- Prints how many files were included

## Usage

```
python deploy.py export myproject --pattern "*.tar.gz"
python deploy.py export frontend --pattern "frontend-2.*.tar.gz"
```

The pattern comes directly from the CLI argument.
