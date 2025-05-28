# 📦 Packet Sniffing – Key Cybersecurity Concepts

---

## ✅ What is Packet Sniffing?

* **Definition**: The practice of using tools to capture and observe data packets as they travel across a network.
* **Packet Contents**:

  * **Header**: Contains sender and receiver IP addresses.
  * **Body**: May include personal or sensitive info (e.g., names, dates of birth, credit card numbers).

---

## 🧑‍💻 Who Uses Packet Sniffing?

### 🔍 Security Analysts:

* Investigate incidents.
* Debug network issues.
* Use sniffing **legally and ethically**.

### 🚨 Malicious Actors:

* Use it **illegally** to:

  * Spy on private data.
  * Alter packet content.
  * Gain unauthorized access.

---

## 🛠️ How Malicious Packet Sniffing Works

* **Man-in-the-middle attacks**: Hacker places themselves between two devices to intercept data.
* Can use **software** or **hardware sniffers**.
* Can **read** or **change** packet data.

---

## 🔁 Types of Packet Sniffing Attacks

### 1. **Passive Packet Sniffing**

* **Reads** data without changing it.
* Compares to **a mailman reading your letters**.
* Common on networks using **hubs** (everyone sees the traffic).

### 2. **Active Packet Sniffing**

* **Modifies** data in transit.
* Example: Changing a bank account number in a packet.
* Compares to **a neighbor intercepting and changing your mail**.

---

## 🔐 How to Prevent Packet Sniffing

### 1. **Use a VPN (Virtual Private Network)**

* Encrypts your data.
* Even if sniffed, data can’t be read.
* Useful on public or unsecured networks.

### 2. **Use HTTPS Websites**

* Encrypts data with **SSL/TLS**.
* Look for `https://` at the beginning of URLs.
* Prevents spying during data transmission.

### 3. **Avoid Unprotected WiFi**

* Common in public places (cafes, airports, etc.).
* These networks usually lack encryption.
* Use a VPN if you must use public WiFi.

---

## 📝 Summary – Important Points to Remember

* Packet sniffing can be used for good (security) or bad (hacking).
* Malicious actors may:

  * **Spy on** or **alter** sensitive data.
  * **Intercept** data using man-in-the-middle techniques.
* Defend against attacks with:

  * **VPNs**
  * **HTTPS**
  * **Avoiding public WiFi without protection**
