# URGENT: Rename Project in Build System

**Client emergency:** A major client has rebranded and their project needs to be renamed in our build system immediately.

## What to implement

Add a `rename` subcommand to `deploy.py` that:

- Accepts two positional arguments: **old_name** and **new_name**
- Renames `/builds/<old_name>/` to `/builds/<new_name>/`
- Prints a confirmation message

## Usage

```
python deploy.py rename old-client new-client
python deploy.py rename myproject myproject-v2
```

## Notes

Both arguments come from the CLI. Keep the implementation consistent with the existing `build` and `package` commands.
