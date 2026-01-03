import json
import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from backends.linux_backend import LinuxIPsecBackend


def load_policy():
    policy_path = PROJECT_ROOT / "policy" / "policy.json"
    with open(policy_path, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    policy = load_policy()

    backend = LinuxIPsecBackend()

    ipsec_conf = backend.generate_ipsec_conf(policy)
    ipsec_secrets = backend.generate_ipsec_secrets(policy)

    print("=== Generated ipsec.conf ===")
    print(ipsec_conf)
    print("\n=== Generated ipsec.secrets ===")
    print(ipsec_secrets)