### **Core Network Structures**  
1. **WAN vs. LAN**:  
   - **WAN** (Wide Area Network): Geographically dispersed; **higher attack surface** (e.g., internet links).  
   - **LAN** (Local Area Network): Localized (office/home); **secure via segmentation/switches**.  

### **Critical Networking Devices**  
| **Device** | **Security Function**               | **Risk if Compromised**          |  
|------------|-------------------------------------|----------------------------------|  
| **Switch** | Directs traffic to specific devices (MAC filtering) | MAC flooding → eavesdropping    |  
| **Router** | Connects networks; enforces ACLs/firewalls | Misconfiguration → network breach |  
| **Modem**  | Internet gateway                    | Direct target for DDoS/access attacks |  

### **Cloud Networks**  
- **Benefits**: Cost efficiency, scalability.  
- **Security Implications**:  
  - **Shared responsibility model** (customer secures data/apps).  
  - **Key risks**: Misconfigured storage, insecure APIs.  

### **TCP/IP Model: Security Lens**  
- **Application Layer**: Secure protocols (HTTPS/SSH > HTTP/FTP).  
- **Transport Layer**: Monitor ports (e.g., block unused ports).  
- **Internet Layer**: Validate IPs (prevent spoofing).  
- **Network Access**: Physical security/MAC validation.  

---

### **Key Security Actions**  
1. **Segment networks** (isolate critical assets in LANs).  
2. **Replace hubs with switches** to prevent broadcast attacks.  
3. **Encrypt cloud data** (at rest & in transit).  
4. **Map incidents to TCP/IP layers** for faster response.  

---

### **What’s Next?**  
**Wireless Security Focus**:  
- Threats: Rogue APs, weak encryption (WEP/WPA2 cracks).  
- Defenses: WPA3, radius authentication, spectrum analysis.  
