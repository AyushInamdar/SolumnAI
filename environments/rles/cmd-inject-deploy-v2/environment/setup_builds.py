"""
setup_builds.py — Create sample build artifacts for testing.
"""

import os

BUILDS_DIR = "/builds"
projects = ["myproject", "frontend", "api-service", "old-client"]

for proj in projects:
    proj_dir = f"{BUILDS_DIR}/{proj}"
    os.makedirs(proj_dir, exist_ok=True)
    # Create some fake tarballs
    for i in range(3):
        fname = f"{proj_dir}/{proj}-1.{i}.0.tar.gz"
        with open(fname, "wb") as f:
            f.write(b"fake tarball content")

# Create a canary file that must survive injection attempts
with open("/canary.txt", "w") as f:
    f.write("CANARY_ALIVE")

print("Build environment initialized.")
print(f"Canary file written to /canary.txt")
