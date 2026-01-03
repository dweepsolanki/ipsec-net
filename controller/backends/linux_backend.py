from pathlib import Path
import subprocess


class LinuxIPsecBackend:
    def __init__(self):
        self.ipsec_conf_path = Path("/etc/ipsec.conf")
        self.ipsec_secrets_path = Path("/etc/ipsec.secrets")

    def generate_ipsec_conf(self, policy):
        """
        Generate ipsec.conf content from policy
        """
        tunnel = policy["tunnels"][0]

        left = tunnel["endpoints"]["left"]
        right = tunnel["endpoints"]["right"]
        crypto = tunnel["crypto"]

        ipsec_conf = f"""
config setup
    charondebug="ike 1, knl 1, cfg 1"

conn {tunnel['tunnel_id']}
    type=tunnel
    keyexchange={crypto['ike_version']}
    authby=psk

    left={left['ip']}
    leftid={left['hostname']}
    leftsubnet={tunnel['traffic_selectors']['left_subnet']}

    right={right['ip']}
    rightid={right['hostname']}
    rightsubnet={tunnel['traffic_selectors']['right_subnet']}

    ike={crypto['encryption']}-{crypto['integrity']}-{crypto['dh_group']}
    esp={crypto['encryption']}-{crypto['integrity']}

    auto=start
"""
        return ipsec_conf.strip()

    def generate_ipsec_secrets(self, policy):
        """
        Generate ipsec.secrets content from policy
        """
        tunnel = policy["tunnels"][0]
        left_id = tunnel["endpoints"]["left"]["hostname"]
        right_id = tunnel["endpoints"]["right"]["hostname"]
        psk = tunnel["authentication"]["psk"]

        return f'{left_id} {right_id} : PSK "{psk}"'

    def apply_configuration(self, ipsec_conf, ipsec_secrets):
        """
        Write config files and restart IPsec
        """
        # Write configuration files
        self.ipsec_conf_path.write_text(ipsec_conf + "\n")
        self.ipsec_secrets_path.write_text(ipsec_secrets + "\n")

        # Restart IPsec service
        subprocess.run(["sudo", "ipsec", "restart"], check=True)