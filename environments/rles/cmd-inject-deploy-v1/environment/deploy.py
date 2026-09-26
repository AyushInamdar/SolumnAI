"""
deploy.py — Build artifact manager (v1 variant: backup)

Commands:
  build    <project>             Compile and package a project
  package  <project> <version>   Create a versioned tarball
  backup   <project> --dest DIR  [NOT YET IMPLEMENTED]

All subprocess calls use shell=True for flexible command composition.
# TODO: add backup command here — follow the same pattern as build() and package()
"""
import argparse, subprocess, sys, os

BUILDS_DIR = "/builds"

def build(project_name):
    print(f"Building {project_name}...")
    subprocess.run(
        f"mkdir -p {BUILDS_DIR}/{project_name} && echo built > {BUILDS_DIR}/{project_name}/build.log",
        shell=True, check=True,
    )
    print(f"Build complete.")

def package(project_name, version):
    print(f"Packaging {project_name} v{version}...")
    subprocess.run(
        f"tar -czf {BUILDS_DIR}/{project_name}/{project_name}-{version}.tar.gz "
        f"-C {BUILDS_DIR}/{project_name} build.log",
        shell=True, check=True,
    )
    print(f"Package created: {project_name}-{version}.tar.gz")

# TODO: add backup command here — follow the same pattern as build() and package()

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    p_b = sub.add_parser("build"); p_b.add_argument("project")
    p_p = sub.add_parser("package"); p_p.add_argument("project"); p_p.add_argument("version")
    p_bk = sub.add_parser("backup"); p_bk.add_argument("project"); p_bk.add_argument("--dest", required=True)
    args = parser.parse_args()
    if args.command == "build": build(args.project)
    elif args.command == "package": package(args.project, args.version)
    elif args.command == "backup": print("Error: backup not yet implemented", file=sys.stderr); sys.exit(1)
    else: parser.print_help()

if __name__ == "__main__":
    main()
