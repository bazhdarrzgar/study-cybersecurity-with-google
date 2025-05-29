# 🛡️ Network Attacks & Defenses – Review Notes

---

## 🔐 Network Security Overview

You’ve learned how to **secure networks** and how attackers try to **intrude** on them using different methods. As a **security analyst**, understanding these attacks and how to prevent them is critical.

---

## 🧪 Network Intrusion Techniques

### 1. **Packet Sniffing**

* **Definition**: Capturing data packets as they travel across a network.
* **Used by attackers** to read sensitive information (passwords, credit cards).
* **Types**:

  * **Passive Sniffing**: Just watching the data (like reading mail).
  * **Active Sniffing**: Changing or redirecting the data (like replacing mail).

### 🛡️ Prevention:

* Use **VPNs** (encrypts traffic).
* Only use **HTTPS websites**.
* Avoid **public Wi-Fi** without protection.

---

### 2. **IP Spoofing**

* **Definition**: Changing the source IP address in a data packet to impersonate a trusted device.
* **Purpose**: Bypass firewalls or impersonate users.

#### Attacks:

* **On-Path Attack**: Attacker intercepts and possibly changes data between two devices.
* **Replay Attack**: Captures a valid packet and reuses it later.
* **Smurf Attack**: Combines IP spoofing and DDoS to flood the network.

### 🛡️ Prevention:

* **Encrypt data**.
* Configure **firewalls** to block spoofed packets (with local IPs from outside).

---

## 🌊 DoS and DDoS Attacks

### 1. **DoS (Denial of Service)**

* One device floods the network/server with traffic.

### 2. **DDoS (Distributed DoS)**

* Many devices flood the network at the same time.

#### Common Types:

* **SYN Flood**: Exploits TCP handshake by sending many SYN requests.
* **ICMP Flood**: Sends too many ICMP (ping) requests to exhaust bandwidth.
* **Ping of Death**: Sends oversized packets that crash the system.

### 🛡️ General Defense Tips:

* Monitor traffic levels.
* Use **intrusion detection/prevention systems (IDS/IPS)**.
* Keep systems patched and firewalls strong.

---

## 🧠 Why This Matters

* These are **real-world attacks** security analysts deal with.
* Understanding these threats is **foundational** for protecting networks.
* You’re now prepared to move on to **security hardening techniques** to strengthen your defenses even more.
