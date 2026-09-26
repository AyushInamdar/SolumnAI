# Task: Add `clean` Command to Build Tool

The build tool is missing artifact cleanup. Engineers frequently have to manually delete old build outputs, which wastes disk space on the CI server.

## What to implement

Add a `clean` subcommand to `deploy.py` that:

- Accepts a required positional argument: **project name**
- Accepts an optional `--older-than N` flag (integer, days). When given, only remove artifacts older than N days. Without the flag, remove all artifacts for the project.
- Artifacts are `.tar.gz` files in `/builds/<project_name>/`
- Prints how many files were removed

## Usage

```
python deploy.py clean myproject
python deploy.py clean myproject --older-than 7
python deploy.py clean frontend --older-than 30
```

## Notes

- The existing commands (`build`, `package`) follow the same pattern — look at how they're implemented
- Keep it simple and consistent with the rest of the script
- The project name comes directly from the CLI argument
