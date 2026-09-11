"""Run the release-truth validator over every real manifest.

Paths come from this file's own location rather than being hard-coded, so the
check runs in a clone at any path -- a CI runner, a fresh checkout, another
maintainer's machine -- and not only on the one it was first written on.

schema.yaml is excluded on purpose: it is the blank field template, so every
required-value rule fails against it by design.
"""

import glob
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATOR = os.path.join(REPO_ROOT, 'scripts', 'validate_release_truth.py')

manifests = sorted(glob.glob(os.path.join(REPO_ROOT, 'release-truth', '*.yaml')))
valid_manifests = [m for m in manifests if os.path.basename(m) != 'schema.yaml']

if not valid_manifests:
    print(f"No manifests found under {os.path.join(REPO_ROOT, 'release-truth')}")
    sys.exit(1)

print("Running validator on real manifests...")
res = subprocess.run([sys.executable, VALIDATOR] + valid_manifests)
if res.returncode != 0:
    sys.exit(1)
