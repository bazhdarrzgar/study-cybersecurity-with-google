## 📊 **What Are SIEM Dashboards?**

SIEM dashboards are **visual interfaces** that summarize **security events, alerts, and performance metrics** from across an organization’s IT environment. They allow security teams to:

* **Visualize log data**
* **Monitor for threats**
* **Detect anomalies quickly**
* **Make informed decisions rapidly**

---

## 🔍 **Use Case Example: Suspicious Login Detection**

### Scenario:

* Alert: 500 login attempts on **Ymara’s account** in **5 minutes**
* Dashboard insights:

  * 📍 **Unusual locations** (geo-based anomalies)
  * 🕒 **Outside business hours**
  * 🔁 **High frequency attempts**

### Outcome:

The analyst uses these visual cues to **quickly flag a potential brute-force attack** and take action (e.g., lock account, investigate IPs, etc.).

---

## 🧮 **What Dashboards Show**

Depending on the **audience or role**, dashboards can be tailored to show:

### For Security Analysts:

* 🔥 Active threats & alerts
* 📈 Event trends over time
* 🔍 Unusual login behavior

### For Managers/Executives:

* 📊 Compliance summaries (PCI, HIPAA, etc.)
* 📉 Incident resolution rates
* 🧭 Mean time to detect (MTTD) and respond (MTTR)

### Common Metrics:

| Metric                  | What It Tells You                                   |
| ----------------------- | --------------------------------------------------- |
| **Login failure rate**  | Possible brute force or account lockouts            |
| **Response time**       | How fast the SOC reacts to threats                  |
| **Traffic volume**      | Unusual spikes might mean DDoS or data exfiltration |
| **Uptime/availability** | System/service health status                        |

---

## 🧠 Why Dashboards Matter

* Help prioritize critical alerts at a glance
* Reduce **alert fatigue**
* Enable proactive rather than reactive defense
* Improve **communication** with non-technical stakeholders

---

## ⏭️ Coming Up: Common SIEM Tools

You'll soon learn about real-world SIEM platforms like:

* **Splunk**
* **IBM QRadar**
* **ArcSight**
* **LogRhythm**
* **Microsoft Sentinel**

Each has unique strengths, but they all support dashboards, alerting, and log analysis.
