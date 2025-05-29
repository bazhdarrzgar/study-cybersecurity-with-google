# 🌐 Network Hardening – Key Concepts

---

## 🔐 What is Network Hardening?

* Network hardening is the process of **securing network systems** by reducing vulnerabilities.
* Focuses on:

  * 🔌 Port filtering
  * 🔒 Network access controls
  * 🔐 Encryption
  * 📊 Log analysis
  * 🔄 Regular patching and backups

---

## 🔁 Regular Network Hardening Tasks

### 🔥 1. Firewall Rules Maintenance

* Firewalls control what network traffic is allowed in or out.
* Rules should be reviewed and updated regularly.

### 📑 2. Network Log Analysis

* Logs track all network activity.
* **SIEM tools** (Security Information and Event Management) help analyze these logs.

  * Central dashboard = **“Single pane of glass”**
  * Prioritizes threats as **high**, **medium**, or **low**
  * Helps teams react quickly to high-priority issues

### 🩹 3. Patch Updates & 🔄 Server Backups

* Keeps network software secure
* Regular server backups help recover from attacks or failures

---

## ✅ One-Time or Periodic Network Hardening Tasks

### 🚪 4. Port Filtering

* Only **necessary ports** should be open
* Unused ports = risk = must be **blocked**
* Prevents unauthorized access via port vulnerabilities

### 🛡️ 5. Network Access Privileges

* **Least privilege principle**: Users only get access to what they need
* Prevents internal breaches and limits damage if a breach occurs

### 🧱 6. Network Segmentation

* Splits the network into **smaller subnets** (e.g., HR, Finance)
* Reduces spread of breaches and improves monitoring
* Special zones (e.g., confidential data) get **extra protection**

### 🔒 7. Encryption

* All data in transit should be **encrypted**
* **Restricted zones** use **stronger encryption standards**
* Protects data even if intercepted

---

## 🧠 Recap

| Category               | Task                      | Purpose                                  |
| ---------------------- | ------------------------- | ---------------------------------------- |
| Regular Task           | Firewall Rules            | Control network traffic                  |
| Regular Task           | Log Analysis (via SIEM)   | Detect suspicious behavior               |
| Regular Task           | Patch Updates, Backups    | Fix flaws and prepare for recovery       |
| One-time/Periodic Task | Port Filtering            | Block unnecessary communication ports    |
| One-time/Periodic Task | Network Access Privileges | Restrict access to necessary resources   |
| One-time/Periodic Task | Network Segmentation      | Limit impact of threats and isolate data |
| One-time/Periodic Task | Encryption                | Protect sensitive data during transit    |
