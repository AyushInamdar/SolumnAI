"""
deploy.py — Build artifact manager (v2 variant: rename)

Commands:
  build    <project>              Compile and package
  package  <project> <version>    Create tarball
  rename   <old> <new>            [NOT YET IMPLEMENTED]
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

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    p_b = sub.add_parser("build"); p_b.add_argument("project")
    p_p = sub.add_parser("package"); p_p.add_argument("project"); p_p.add_argument("version")
    p_r = sub.add_parser("rename"); p_r.add_argument("old_name"); p_r.add_argument("new_name")
    args = parser.parse_args()
    if args.command == "build": build(args.project)
    elif args.command == "package": package(args.project, args.version)
    elif args.command == "rename": print("Error: rename not yet implemented", file=sys.stderr); sys.exit(1)
    else: parser.print_help()

if __name__ == "__main__":
    main()
