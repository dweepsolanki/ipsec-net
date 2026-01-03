# Secure Host-to-Host Communication using IPsec  
### YellowSense Technologies

## 📌 Project Overview
This project demonstrates **secure host-to-host communication using IPsec** with the **IKEv2 protocol**.  
It focuses on **encrypted connectivity, security architecture, and verification** across multiple operating systems.

The solution includes:
- Linux ↔ Linux secure IPsec tunnel
- Mac ↔ Linux secure IPsec tunnel
- A Streamlit-based UI for **demonstration and status visualization**

---

## 🛡️ Security Architecture
- **IPsec Mode:** Transport Mode  
- **Key Exchange:** IKEv2  
- **Encryption:** Industry-standard cryptographic algorithms  
- **Authentication:** Pre-Shared Keys (PSK)  
- **Tunnel Type:** Host-to-host  

---

## ✅ Working Demonstrations
| Scenario | Status |
|--------|--------|
| Linux ↔ Linux | ✅ Working |
| Mac ↔ Linux | ✅ Working |
| Windows ↔ Linux | ❌ Intentionally excluded |

---

## 🔍 Scope Clarification
Windows ↔ Linux IPsec connectivity is **intentionally excluded** from live demonstration due to:
- Platform-specific IPsec policy handling
- PSK and configuration constraints on Windows

The **core encryption architecture, tunnel establishment, and validation**
are fully demonstrated using Linux ↔ Linux and Mac ↔ Linux scenarios.

---

## 🖥️ Streamlit UI
A Streamlit-based UI is included to:
- Present project overview
- Explain demo scope and architecture
- Display connectivity status

⚠️ **Note:**  
The UI is **read-only** and does **not perform live configuration changes**.

---

## 📂 Project Structure

IPSEC_NET/
├── app.py                 # Streamlit UI
├── backends/              # Backend helpers
├── orchestrator/          # Tunnel orchestration logic
├── validator/             # Validation and checks
├── logs/                  # IPsec logs and outputs
├── screenshots/           # UI & demo evidence
├── docs/                  # Technical documentation (PDFs)
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.9+
- IPsec implementation:
  - Linux: StrongSwan
  - macOS: Native IPsec / StrongSwan
- Streamlit

### Install Python dependencies
```bash
pip install -r requirements.txt

▶️ Running the UI
streamlit run app.py

Then open:
http://localhost:8501

🔐 Verifying Encrypted Connectivity
	•	Use ping between hosts to verify tunnel
	•	Check IPsec Security Associations (SAs)
	•	Validate encrypted traffic via logs


