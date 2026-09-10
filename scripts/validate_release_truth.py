import sys
import os
import yaml
import re

def validate_manifest(filepath):
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
        
    errors = []
    
    # 1. Required keys
    for key in ['product', 'artifact', 'formats', 'architecture', 'publication_status']:
        if key not in data:
            errors.append(f"Missing root key: {key}")
            return errors

    if not data['product'].get('version'):
        errors.append("Missing product.version")

    # 2. SHA is 64 hex
    sha = data['artifact'].get('sha256', '')
    if not isinstance(sha, str) or not re.match(r'^[0-9a-f]{64}$', sha):
        errors.append("Invalid or missing artifact.sha256 (must be 64-char hex string)")

    # 3. Present formats have bundle/executable/destination fields
    formats = data['formats']
    for fmt_name, fmt_data in formats.items():
        if not isinstance(fmt_data, dict):
            errors.append(f"Format {fmt_name} must be a dictionary")
            continue
        if fmt_data.get('present') is True:
            for fld in ['bundle', 'executable', 'destination', 'architectures', 'universal']:
                if fld not in fmt_data:
                    errors.append(f"Present format {fmt_name} missing '{fld}'")

            # 4. Architecture arrays contain allowed values
            archs = fmt_data.get('architectures', [])
            if not isinstance(archs, list):
                errors.append(f"Format {fmt_name} architectures must be a list")
            else:
                for a in archs:
                    if a not in ['arm64', 'x86_64']:
                        errors.append(f"Invalid architecture token '{a}' in {fmt_name}")

            # 5. universal=true requires BOTH arm64 and x86_64
            uni = fmt_data.get('universal')
            if uni is True:
                if 'arm64' not in archs or 'x86_64' not in archs:
                    errors.append(f"Format {fmt_name} claims universal but missing arm64 or x86_64")
            # 6. universal=false must not falsely contain both
            elif uni is False:
                if 'arm64' in archs and 'x86_64' in archs:
                    errors.append(f"Format {fmt_name} has both arm64 and x86_64 but universal is false")

    # 7. all_formats_identical matches actual architecture sets
    arch_sets = []
    for fmt_name, fmt_data in formats.items():
        if fmt_data.get('present') is True:
            archs = fmt_data.get('architectures', [])
            if archs is not None:
                arch_sets.append(set(archs))

    identical = all(s == arch_sets[0] for s in arch_sets) if arch_sets else True
    
    claimed_identical = data['architecture'].get('all_formats_identical')
    if claimed_identical is True and not identical:
        errors.append("Claims all_formats_identical=true but actual architectures differ")
    if claimed_identical is False and identical:
        errors.append("Claims all_formats_identical=false but actual architectures are identical")

    # 8. safe product-wide claim is absent when architectures differ
    safe_claim = data['architecture'].get('safe_product_wide_claim')
    if not identical and safe_claim:
        errors.append("safe_product_wide_claim is present but architectures differ (violates mixed-architecture rule)")

    # 9. capability_gate_passed=true requires no pending fields
    gate_passed = data['publication_status'].get('capability_gate_passed')
    if gate_passed is True:
        # check if any string value is 'pending_artifact_inspection'
        def check_pending(node):
            if isinstance(node, dict):
                for v in node.values():
                    if check_pending(v): return True
            elif isinstance(node, list):
                for v in node:
                    if check_pending(v): return True
            elif isinstance(node, str) and node == 'pending_artifact_inspection':
                return True
            return False
        
        if check_pending(data):
            errors.append("capability_gate_passed is true but contains 'pending_artifact_inspection'")

    return errors

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_release_truth.py <manifest.yaml>...")
        sys.exit(1)

    all_good = True
    for fp in sys.argv[1:]:
        print(f"Validating {fp}...")
        errs = validate_manifest(fp)
        if errs:
            all_good = False
            for e in errs:
                print(f"  [ERROR] {e}")
        else:
            print("  [PASS]")

    if not all_good:
        sys.exit(1)
