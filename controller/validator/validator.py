import json
import sys
from pathlib import Path


class PolicyValidationError(Exception):
    pass


class PolicyValidator:
    REQUIRED_TOP_LEVEL_FIELDS = ["policy_name", "tunnels"]

    REQUIRED_TUNNEL_FIELDS = [
        "tunnel_id",
        "type",
        "mode",
        "protocol",
        "endpoints",
        "traffic_selectors",
        "crypto",
        "authentication"
    ]

    def __init__(self, policy_path: str):
        self.policy_path = Path(policy_path)
        self.policy_data = None

    def load_policy(self):
        if not self.policy_path.exists():
            raise PolicyValidationError(f"Policy file not found: {self.policy_path}")

        with open(self.policy_path, "r") as f:
            self.policy_data = json.load(f)

    def validate_top_level(self):
        for field in self.REQUIRED_TOP_LEVEL_FIELDS:
            if field not in self.policy_data:
                raise PolicyValidationError(f"Missing top-level field: {field}")

    def validate_tunnels(self):
        tunnels = self.policy_data.get("tunnels", [])
        if not tunnels:
            raise PolicyValidationError("No tunnels defined in policy")

        for tunnel in tunnels:
            for field in self.REQUIRED_TUNNEL_FIELDS:
                if field not in tunnel:
                    raise PolicyValidationError(
                        f"Tunnel '{tunnel.get('tunnel_id', 'UNKNOWN')}' missing field: {field}"
                    )

    def validate(self):
        self.load_policy()
        self.validate_top_level()
        self.validate_tunnels()
        return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validator.py <policy.json>")
        sys.exit(1)

    validator = PolicyValidator(sys.argv[1])
    try:
        validator.validate()
        print("Policy validation successful ✅")
    except PolicyValidationError as e:
        print(f"Policy validation failed ❌: {e}")
        sys.exit(1)