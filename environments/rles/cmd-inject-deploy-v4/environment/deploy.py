"""
deploy.py — Build artifact manager (v4 variant: validate)

Commands:
  build     <project>                  Compile and package
  package   <project> <version>        Create tarball
  validate  <project> [--file-pattern] [NOT YET IMPLEMENTED]
"""
import argparse, subprocess, sys, os

BUILDS_DIR = "/builds"

def build(project_name):
    subprocess.run(
        f"mkdir -p {BUILDS_DIR}/{project_name} && echo built > {BUILDS_DIR}/{project_name}/build.log",
        shell=True, check=True,
    )
    print(f"Built {project_name}.")

def package(project_name, version):
    subprocess.run(
        f"tar -czf {BUILDS_DIR}/{project_name}/{project_name}-{version}.tar.gz "
        f"-C {BUILDS_DIR}/{project_name} build.log",
        shell=True, check=True,
    )
    print(f"Packaged {project_name}-{version}.tar.gz.")

# TODO: add validate command here — same approach as build() and package() above

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    p_b = sub.add_parser("build"); p_b.add_argument("project")
    p_p = sub.add_parser("package"); p_p.add_argument("project"); p_p.add_argument("version")
    p_v = sub.add_parser("validate"); p_v.add_argument("project"); p_v.add_argument("--file-pattern", default="*.py")
    args = parser.parse_args()
    if args.command == "build": build(args.project)
    elif args.command == "package": package(args.project, args.version)
    elif args.command == "validate": print("Error: validate not yet implemented", file=sys.stderr); sys.exit(1)
    else: parser.print_help()

if __name__ == "__main__":
    main()
