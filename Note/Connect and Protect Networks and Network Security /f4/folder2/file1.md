# 🖥️ OS Hardening – Key Concepts

---

## 💡 What is OS Hardening?

* **Definition**: The process of securing the **Operating System (OS)** to reduce vulnerabilities and protect the network.
* **Why It Matters**: One insecure OS can compromise the entire network.

---

## 🔁 Regular OS Hardening Tasks

### 🩹 1. Patch Updates

* Fix security vulnerabilities in software or the OS.
* Released by OS vendors (e.g., Microsoft, Apple, Linux distros).
* Must be applied **immediately**, because hackers monitor for systems that haven’t been patched.

> 📌 Example: A team had to **emergency patch** their systems due to a flaw in a widely used programming library.

---

### 📋 2. Maintain a Baseline Configuration

* A **baseline** is the standard, secure version of an OS.
* Used to detect unauthorized changes or issues.
* Includes settings like **firewall rules**, **open ports**, and more.

---

### 🗑️ 3. Hardware and Software Disposal

* Securely **wipe** and dispose of old hardware.
* **Remove unused software** to eliminate vulnerabilities (unused programs may contain old flaws).

---

## 🔐 One-Time or Periodic Hardening Tasks

### 🔐 4. Password Policy

* Enforce **strong password rules**, e.g.:

  * Minimum 8 characters
  * Must include uppercase, numbers, and symbols
* **Lock out** accounts after several failed attempts

---

### 🧾 5. Multi-Factor Authentication (MFA)

* Adds extra identity verification steps:

  * 🔑 Something you *know* (password)
  * 📱 Something you *have* (ID or phone)
  * 🧬 Something you *are* (fingerprint, face)

---

## 🧠 Recap

* OS hardening strengthens the OS to protect the **entire network**.
* Tasks include:

  * Patching vulnerabilities
  * Keeping secure configurations
  * Removing unused components
  * Enforcing strong password & MFA policies
