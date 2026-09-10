import subprocess
import sys
import glob

manifests = glob.glob('/Users/mert/StudioZIO-Releases/release-truth/*.yaml')
valid_manifests = [m for m in manifests if not m.endswith('schema.yaml')]

print("Running validator on real manifests...")
res = subprocess.run(['python3', '/Users/mert/StudioZIO-Releases/scripts/validate_release_truth.py'] + valid_manifests)
if res.returncode != 0:
    sys.exit(1)
