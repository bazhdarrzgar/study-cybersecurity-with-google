## 🔍 **Key Log Sources**

As a security analyst, you’ll rely heavily on three main log types:

### 1. **Firewall Logs**

* Show **incoming and outgoing traffic**.
* Help detect:

  * Unauthorized access attempts
  * Port scanning
  * Blocked or allowed connections
* Example entry:
  `INBOUND DENY TCP 192.168.1.5:22 -> 10.0.0.1:80`

### 2. **Network Logs**

* Record **device activity** across the network.
* Useful for:

  * Identifying lateral movement
  * Device join/leave events
  * IP address assignments
* Example insight:
  A sudden spike in outbound traffic from a user machine — could indicate data exfiltration.

### 3. **Server Logs**

* Contain **authentication and service access events**.
* Track:

  * Logins (successful and failed)
  * Access to shared folders or databases
  * Password reset requests
* Example event:
  Multiple failed login attempts from a single IP = brute force alert.

---

## 🧠 **Why This Matters**

* Logs are **evidence**.
* They help you **trace attacker behavior**, **find vulnerabilities**, and **support incident response**.
* Reviewing logs manually is not scalable — that’s where SIEM comes in.

---

## ⚙️ **SIEM (Security Information and Event Management) Tools**

### Core Capabilities:

| Function           | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| **Log Collection** | Gathers logs from all sources (firewalls, servers, endpoints, etc.) |
| **Normalization**  | Converts logs into a standard format for easier analysis            |
| **Correlation**    | Connects events across multiple systems to detect patterns          |
| **Alerting**       | Triggers real-time alerts for suspicious behavior                   |
| **Visualization**  | Dashboards summarize and display trends and anomalies               |
| **Retention**      | Stores logs securely for compliance and forensics                   |

### Why Analysts Love SIEM:

* Cuts down **manual work**
* Offers **real-time insights**
* Enables **automated responses** (like isolating a machine after suspicious behavior)
* Helps ensure **compliance** (GDPR, HIPAA, PCI DSS)

---

## 🔜 What’s Next?

Coming up, you’ll learn how to:

* **Navigate SIEM dashboards**
* **Spot threats** like brute force attacks or unusual network spikes
* Use queries (like SPL in Splunk) to **filter log data efficiently**
