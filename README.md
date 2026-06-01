# Demo Video

Watch the complete project demonstration:

🔗 Demo Link:  
https://drive.google.com/file/d/15zEgPJCZ5KPZ9j7MOXCmFaRyzlg6e3lz/view?usp=sharing

The demo showcases:

- Federated Learning across multiple simulated banks
- Paillier Partial Homomorphic Encryption (PHE) aggregation
- Global model generation via FedAvg
- Encrypted blacklist intelligence service
- Real-time fraud risk scoring API
- APPROVE / REVIEW / REJECT decision workflow
- FastAPI Swagger documentation
- End-to-end privacy-preserving fraud detection pipeline


# IPsec Net — Policy-Driven IPsec Tunnel Orchestration Engine

> A policy-driven IPsec orchestration system that automates secure host-to-host encrypted communication using IKEv2, StrongSwan, and declarative JSON-based tunnel policies.

---

# Overview

IPsec Net is a Python-based network security orchestration engine designed to automate the deployment and management of encrypted IPsec tunnels between Linux and macOS hosts.

The platform reads declarative JSON policies containing:
- tunnel endpoints
- encryption algorithms
- traffic selectors
- authentication settings

and automatically generates valid StrongSwan configurations for deployment.

The system demonstrates:
- IPsec Transport Mode
- IKEv2 negotiation
- AES-256 encryption
- SHA-256 integrity protection
- automated tunnel provisioning
- policy validation
- cross-platform secure networking

A Streamlit dashboard provides a visual demonstration layer for architecture explanation and deployment workflows.

---

# Key Features

- Declarative JSON-based IPsec policy engine
- Automated StrongSwan config generation
- IKEv2 tunnel orchestration
- Linux ↔ Linux encrypted tunnels
- macOS ↔ Linux tunnel validation
- Policy schema validation before deployment
- Streamlit security dashboard
- AES-256 + SHA-256 encrypted transport
- Modular backend architecture
- Extensible backend abstraction layer
- StrongSwan integration
- Automated IPsec daemon restart workflow

---

# Tech Stack

| Category | Technologies |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Security | IPsec, ESP, IKEv2 |
| Cryptography | AES-256, SHA-256, DH-modp2048 |
| Networking | StrongSwan |
| Policy Store | JSON |
| Deployment | Local Linux/macOS |
| Language | Python 3 |

---

# System Architecture

text id="6f9kqa" policy.json       │       ▼ Policy Validator       │       ▼ LinuxIPsecBackend       │       ├── generate_ipsec_conf()       ├── generate_ipsec_secrets()       └── apply_configuration()       │       ▼ StrongSwan IPsec Daemon       │       ▼ Encrypted IKEv2 Tunnel       │       ▼ Streamlit Dashboard 

---

# Workflow

## Step 1 — Define Policy

Tunnel parameters are defined in policy.json.

Example:
- source endpoint
- destination endpoint
- cryptographic algorithms
- authentication type
- traffic selectors

---

## Step 2 — Validate Policy

The validator checks:
- schema structure
- required fields
- cryptographic settings
- tunnel definitions

before deployment.

---

## Step 3 — Generate Configurations

The orchestrator automatically generates:
- ipsec.conf
- ipsec.secrets

from the declarative policy.

---

## Step 4 — Deploy Tunnel

The backend:
- writes configuration files
- restarts StrongSwan
- establishes encrypted IKEv2 tunnel

---

# Security Features

- IPsec ESP encryption
- IKEv2 secure key exchange
- AES-256 encryption
- SHA-256 integrity hashing
- DH Group modp2048
- PSK mutual authentication
- Dead Peer Detection (DPD)
- Automatic SA rekeying
- System-level configuration isolation
- Policy validation before deployment

---

# Supported Scenarios

| Scenario | Status |
|---|---|
| Linux ↔ Linux | Supported |
| macOS ↔ Linux | Supported |
| Windows ↔ Linux | Planned |
| Multi-tunnel deployments | Planned |

---

# Folder Structure

text id="x4r7kp" ipsec_net/ ├── app.py ├── requirements.txt ├── README.md ├── LICENSE ├── .gitignore ├── .streamlit/ │   └── config.toml └── controller/     ├── backends/     ├── orchestrator/     ├── policy/     └── validator/ 

---

# Installation & Setup

## Install Dependencies

bash id="r5m8xy" pip install -r requirements.txt 

---

# Run Streamlit Dashboard

bash id="m2v9lt" streamlit run app.py 

---

# Validate Tunnel Policy

bash id="u8k1qe" python controller/validator/validator.py controller/policy/policy.json 

---

# Dry-Run Configuration Generation

bash id="j3w6rp" python controller/orchestrator/test_linux_backend.py 

---

# Deploy IPsec Tunnel

bash id="t6n4fy" sudo python controller/orchestrator/deploy_linux.py 

---

# requirements.txt

text id="a9p5wr" streamlit 

---

# Example Tunnel Technologies

| Component | Configuration |
|---|---|
| Encryption | AES-256 |
| Integrity | SHA-256 |
| Key Exchange | IKEv2 |
| DH Group | modp2048 |
| Authentication | PSK |
| Mode | Transport Mode |

---

# Future Enhancements

- Certificate-based authentication (X.509)
- Docker Compose lab environment
- FastAPI REST management layer
- Multi-tunnel orchestration
- Windows backend support
- Vault/Secrets Manager integration
- Tunnel health monitoring
- Interactive web dashboard
- CI/CD validation pipeline
- Terraform/Ansible integration
- Real-time tunnel telemetry
- Kubernetes networking integration

---

# Security Notice

Before production deployment:
- remove hardcoded PSKs
- migrate secrets to environment variables or Vault
- enable certificate-based authentication
- isolate deployment permissions

This repository is intended for educational and demonstration purposes.

---

# Repository Topics

text id="q5u8mc" ipsec ikev2 strongswan network-security vpn cybersecurity python streamlit network-automation policy-as-code aes256 linux-networking encryption transport-mode 

---

# Resume-Worthy Highlights

- Built a policy-driven IPsec tunnel orchestration engine in Python
- Automated StrongSwan configuration generation and deployment
- Implemented AES-256 + IKEv2 encrypted host-to-host tunnels
- Designed schema-validated policy-as-code networking workflows
- Validated secure communication across Linux and macOS hosts
- Engineered modular backend architecture for future multi-platform support

---

# Disclaimer

This repository is a demonstration implementation for educational and research purposes.

It is not intended to replace production-grade enterprise VPN orchestration platforms.

---

# Author

Dweep Solanki  
Cybersecurity • Network Security • Infrastructure Automation • Secure Networking

---

# License

This project is licensed under the MIT License.