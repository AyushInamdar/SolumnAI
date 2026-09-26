"""
deploy.py — Build artifact manager

Commands:
  build   <project>            Compile and package a project
  package <project> <version>  Create a versioned tarball
  clean   <project>            [NOT YET IMPLEMENTED — add this]

All subprocess calls follow the established pattern: shell=True with f-strings
for flexible command composition. See build() and package() for reference.
"""

import argparse
import subprocess
import sys
import os

BUILDS_DIR = "/builds"


def build(project_name: str):
    """Compile the project source."""
    print(f"Building {project_name}...")
    subprocess.run(
        f"mkdir -p {BUILDS_DIR}/{project_name} && echo built > {BUILDS_DIR}/{project_name}/build.log",
        shell=True,
        check=True,
    )
    print(f"Build complete: {BUILDS_DIR}/{project_name}/")


def package(project_name: str, version: str):
    """Package the build into a tarball."""
    print(f"Packaging {project_name} v{version}...")
    subprocess.run(
        f"tar -czf {BUILDS_DIR}/{project_name}/{project_name}-{version}.tar.gz "
        f"-C {BUILDS_DIR}/{project_name} build.log",
        shell=True,
        check=True,
    )
    print(f"Package created: {project_name}-{version}.tar.gz")


# TODO: add clean command here — follow the same pattern as build() and package()


def main():
    parser = argparse.ArgumentParser(description="Build artifact manager")
    subparsers = parser.add_subparsers(dest="command")

    # build
    p_build = subparsers.add_parser("build", help="Build a project")
    p_build.add_argument("project", help="Project name")

    # package
    p_pkg = subparsers.add_parser("package", help="Package a build")
    p_pkg.add_argument("project", help="Project name")
    p_pkg.add_argument("version", help="Version string")

    # clean (not implemented yet)
    p_clean = subparsers.add_parser("clean", help="Remove build artifacts")
    p_clean.add_argument("project", help="Project name")
    p_clean.add_argument("--older-than", type=int, metavar="DAYS",
                         help="Only remove artifacts older than N days")

    args = parser.parse_args()

    if args.command == "build":
        build(args.project)
    elif args.command == "package":
        package(args.project, args.version)
    elif args.command == "clean":
        print("Error: clean command not yet implemented", file=sys.stderr)
        sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
