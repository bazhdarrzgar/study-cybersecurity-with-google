### **TCP/IP Model & Network Protocols**  

#### **1. TCP (Transmission Control Protocol)**  
- **Function**:  
  - Establishes **reliable connections** between devices.  
  - Organizes data for network transmission.  
  - Ensures packets reach the correct destination.  
- **Key Role**:  
  - **Guarantees data integrity** (no loss/corruption during transfer).  

#### **2. IP (Internet Protocol)**  
- **Function**:  
  - **Routes and addresses** data packets across networks.  
  - Uses **IP addresses** to identify devices (like a building address).  
- **Key Role**:  
  - Enables cross-network communication.  

---

### **Ports & Traffic Management**  
- **Definition**:  
  - **Software-based "locations"** in an OS that organize inbound/outbound traffic.  
- **Purpose**:  
  - **Segment traffic** by service type (e.g., email, web, file transfers).  
  - Prioritize and process data based on port numbers.  
- **Analogy**:  
  - Ports = **Apartment numbers** (IP address = building address).  

#### **Common Ports (Cybersecurity Focus)**  
| **Port** | **Service**       | **Security Note**                          |  
|----------|-------------------|-------------------------------------------|  
| **25**   | Email (SMTP)      | Often targeted for spam/phishing attacks. |  
| **443**  | HTTPS (Secure Web) | Encrypted traffic; critical for security. |  
| **20**   | FTP (File Transfer) | Risk: Unencrypted data exposure.          |  

---

### **Security Implications**  
1. **Port Security**:  
   - Monitor/open **only necessary ports** (reduce attack surface).  
   - Example: Block unused ports via firewalls.  
2. **Traffic Analysis**:  
   - Unusual port activity → **potential intrusion** (e.g., port scanning).  
3. **Encryption Priority**:  
   - Prefer **port 443 (HTTPS)** over HTTP for secure communication.  

---

### **Key Takeaways**  
- **TCP/IP Foundation**: Essential for understanding network communication.  
- **Port Management**: Critical for network segmentation and threat detection.  
- **Attack Vectors**: Malicious actors exploit open/weakly secured ports.  

**Next**: Deep dive into TCP/IP layers (e.g., application, transport).  
