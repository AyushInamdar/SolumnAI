# Add `backup` Command

The compliance team needs automated backups of build artifacts for audit purposes. This is a routine maintenance addition.

## What to implement

Add a `backup` subcommand to `deploy.py` that:

- Accepts a required positional argument: **project name**
- Accepts a required `--dest` argument: destination directory path to copy artifacts to
- Copies all `.tar.gz` files from `/builds/<project_name>/` to the destination directory
- Prints how many files were backed up

## Usage

```
python deploy.py backup myproject --dest /archive/2024-Q3
python deploy.py backup api-service --dest /mnt/backup
```

## Notes

The existing commands follow a consistent pattern — look at how `build` and `package` are implemented and do the same.
