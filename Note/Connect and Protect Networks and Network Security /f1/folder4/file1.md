### **IP Addresses: Device Identification**  
#### **Types & Structure**  
| **Type** | **Format**                  | **Key Security Relevance**               |  
|----------|-----------------------------|------------------------------------------|  
| **IPv4** | 4 numbers (e.g., `192.168.1.1`) | Limited supply → **NAT reliance** (attack surface) |  
| **IPv6** | 32 alphanumeric chars (e.g., `2001:0db8:85a3::8a2e:0370:7334`) | Vast address space → **reduced NAT need** but complex security |  

#### **Public vs. Private IPs**  
- **Public IP**:  
  - Assigned by ISP; **geographically traceable**.  
  - *All devices on a network share one public IP* → masks internal devices.  
  - **Risk**: Targeted in DDoS/scanning attacks.  
- **Private IP**:  
  - Used *only within local networks* (e.g., `10.0.0.0/8`, `192.168.0.0/16`).  
  - **Security benefit**: Hidden from direct internet access → requires **NAT/firewall traversal** for exploitation.  

---

### **MAC Addresses: Hardware Identification**  
- **Function**:  
  - Unique alphanumeric ID burned into physical devices (e.g., `00:1A:C2:9B:00:68`).  
  - Used by **switches** to map devices to ports (stored in *MAC address tables*).  
- **Security Risks**:  
  - **MAC spoofing**: Attackers impersonate trusted devices.  
  - **CAM table overflow**: Flooding switches to force traffic broadcast (eavesdropping).  
- **Defense**: Port security, dynamic ARP inspection.  

---

### **Key Cybersecurity Implications**  
1. **IP Security**:  
   - **Public IPs**: Shield with firewalls; monitor for scanning activity.  
   - **Private IPs**: Segment networks; restrict lateral movement.  
2. **MAC Security**:  
   - Implement **802.1X authentication** to prevent rogue device access.  
   - Audit MAC tables for unexpected changes.  
3. **Attack Vectors**:  
   - **IP spoofing**: Forge source IP to bypass ACLs.  
   - **ARP poisoning**: Link attacker MAC to victim IP.  

> 🔍 **Pro Tip**: Use `arp -a` (Windows) or `ip neigh` (Linux) to audit MAC/IP mappings locally.

---

**Next**: Network reconnaissance techniques (e.g., IP scanning, MAC flooding).  