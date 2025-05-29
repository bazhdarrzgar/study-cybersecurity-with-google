# ☁️ Cloud Network Hardening – Key Concepts

---

## 🌐 What Is a Cloud Network?

* A **cloud network** stores data and runs applications on remote servers accessed via the **internet**.
* Used for:

  * 📁 Data storage
  * ⚙️ Application hosting
  * 📊 Processing and analytics

---

## 🔐 Why Harden Cloud Networks?

* Cloud providers manage the infrastructure but **can’t fully protect your data or services**.
* Organizations are responsible for **securing their cloud environments** from both **external and internal threats**.

---

## 🧰 Key Cloud Hardening Practices

### 🧱 1. Use a **Server Baseline Image**

* A **baseline image** is a standard reference of how a cloud server should be configured.
* Lets you **compare current settings** to the original to detect **unauthorized changes**.

  * Helps catch intrusions or configuration drift

### 🔄 2. Separation of Services

* Just like OS hardening:

  * **Older vs. newer apps** should be kept apart
  * **Internal apps** should be separated from **user-facing apps**
* Reduces risk of vulnerabilities spreading across systems

### 🤝 3. Understand **Shared Responsibility**

* **Cloud provider** secures the **infrastructure**
* **You (the organization)** secure:

  * 🔐 Your **data**
  * ⚙️ Your **apps**
  * 👥 Your **user access and settings**

### 🔄 4. Continue Traditional Security Practices

* Even in the cloud, continue:

  * ✅ Patch updates
  * 🔐 Access control
  * 🔒 Encryption
  * 🔍 Log monitoring

---

## 🧠 Recap Table

| Concept               | Description                                              |
| --------------------- | -------------------------------------------------------- |
| Cloud Network         | Servers accessed via internet to store/run resources     |
| Server Baseline Image | Standard config for comparison to detect changes         |
| Service Separation    | Dividing old/new and internal/user-facing apps           |
| Shared Responsibility | Cloud provider secures infra, org secures data/apps      |
| Traditional Practices | Still apply: patching, access controls, encryption, etc. |
