import streamlit as st

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="IPsec Net Demo",
    layout="wide"
)

# ============================================================================
# HEADER SECTION
# ============================================================================
st.title("Secure Host-to-Host Communication using IPsec — YellowSense Technologies")
st.markdown(
    "Demonstration of encrypted Mac ↔ Linux and Linux ↔ Linux connectivity using IKEv2"
)

# ============================================================================
# INTRODUCTION SECTION
# Brief overview of what this demonstration showcases
# ============================================================================
st.markdown("""
This project demonstrates **secure IPsec communication** using:

- Mac → Linux
- Linux → Linux

The UI shows:
- Project overview
- Demo explanation
- Connectivity status
""")

st.divider()

# ============================================================================
# PROJECT OVERVIEW SECTION
# Explains the security model, working demonstrations, and scope
# ============================================================================
st.header("📘 Project Overview")

st.markdown("""
This project demonstrates **secure host-to-host communication using IPsec** with the **IKEv2** protocol.

### Security Model
- Host-to-host IPsec (Transport Mode)
- Encrypted communication using industry-standard cryptographic algorithms
- Key exchange handled via IKEv2

### ✅ Working Demonstrations
- **Mac ↔ Linux** secure connectivity
- **Linux ↔ Linux** secure connectivity

### 🔍 Scope Clarification
- **Windows ↔ Linux connectivity is intentionally skipped** as per project scope and discussion.
- The focus is on demonstrating encryption, architecture, and verification — not OS-specific limitations.

### 🎯 UI Purpose
- This UI is designed for **demonstration and explanation**
- It shows **connectivity status, architecture, and logs**
- No live configuration changes are performed from the UI
""")

# ============================================================================
# DEMO STATUS SECTION
# Displays the current working state of each connectivity scenario
# ============================================================================
st.header("✅ Demo Status")

# Working connectivity scenarios
st.success("Mac → Linux connectivity: WORKING")
st.success("Linux → Linux connectivity: WORKING")

# Intentionally excluded scenario with explanation
st.info("Windows → Linux skipped as per project scope")

st.subheader("Why Windows ↔ Linux is not demonstrated")

st.markdown("""
- The project focuses on **host-to-host IPsec encryption using IKEv2**.
- **Mac ↔ Linux** and **Linux ↔ Linux** tunnels were successfully configured and validated.
- During testing, **Windows ↔ Linux IPsec** introduced platform-specific limitations
  (policy handling and PSK constraints).
- As per guidance and project scope, Windows ↔ Linux is **intentionally excluded**
  from live demonstration.
- The design, architecture, and encryption concepts remain fully demonstrated
  through the working scenarios.
""")

st.divider()

# ============================================================================
# FOOTER
# ============================================================================
st.caption("IPsec Net — Secure Networking Demo")