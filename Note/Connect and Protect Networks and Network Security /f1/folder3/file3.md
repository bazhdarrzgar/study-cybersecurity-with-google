### **TCP/IP Model: 4-Layer Framework**  
*(Visualizes data organization/transmission for threat monitoring)*  

| **Layer**              | **Key Functions**                                                                 | **Security Focus**                                                                 |
|-------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **1. Network Access**   | Creates data packets; handles physical transmission (cables, switches, hardware) | **Physical security**: Unauthorized device access, MAC spoofing, cable tampering |
| **2. Internet**         | Attaches IP addresses (sender/receiver); routes packets between networks          | **IP spoofing**, route hijacking, firewall configuration risks                   |
| **3. Transport**        | Controls traffic flow via protocols (e.g., TCP); error control; connection status | **DDoS attacks**, port scanning, encryption gaps (e.g., unsecured TCP)           |
| **4. Application**      | Manages interaction with receiving devices (email, file transfers, APIs)          | **Malware delivery**, phishing, API vulnerabilities, insecure protocols (e.g., FTP) |

---

### **Key Security Applications**  
1. **Threat Identification**:  
   - Anomalies at **Network Access Layer** → Physical breach/MAC spoofing.  
   - Suspicious IP changes at **Internet Layer** → Spoofing/man-in-the-middle.  
   - Unusual traffic at **Transport Layer** → DDoS/port scanning.  
   - Exploits at **Application Layer** → Malware/phishing.  
2. **Layered Defense**:  
   - Apply controls at **each layer** (e.g., MAC filtering, IP firewalls, TLS encryption, app-layer antivirus).  
3. **Incident Response**:  
   - Pinpoint compromise layer to accelerate containment (e.g., transport layer floods → block malicious ports).  

> 🔍 **Pro Tip**: Map security tools to layers (e.g., Wireshark for Transport, NGFW for Internet/Application).

---

**Next**: Protocol-specific threats (e.g., TCP vs. UDP).  