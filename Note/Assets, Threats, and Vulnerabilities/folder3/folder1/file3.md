### 🛡️ **Defense in Depth: Layered Security Model**
- **Definition**: A **layered approach** to security that uses multiple defenses to protect assets.  
- **Analogy**: Like a medieval castle with moats, walls, and watchtowers—each layer reduces risk if one fails.  
- **Goal**: Minimize the chance of a successful attack by creating multiple barriers.  

---

### 🧱 **The 5 Layers of Defense in Depth**
1. **Perimeter Layer**  
   - **Purpose**: Control external access to the network.  
   - **Security Controls**:  
     - User authentication (e.g., usernames, passwords).  
     - Firewalls, intrusion detection systems (IDS).  
   - **Example**: Filtering unauthorized users at the network’s edge.  

2. **Network Layer**  
   - **Purpose**: Secure internal network traffic and segmentation.  
   - **Security Controls**:  
     - Network firewalls, VLANs (Virtual Local Area Networks).  
     - Encryption (e.g., TLS/SSL for data in transit).  
   - **Focus**: Authorization (who can access what within the network).  

3. **Endpoint Layer**  
   - **Purpose**: Protect individual devices (laptops, servers) connected to the network.  
   - **Security Controls**:  
     - Antivirus software, endpoint detection and response (EDR).  
     - Device encryption and patch management.  
   - **Example**: Blocking malware on a user’s laptop before it spreads.  

4. **Application Layer**  
   - **Purpose**: Secure software and services that users interact with.  
   - **Security Controls**:  
     - Multi-Factor Authentication (MFA).  
     - Secure coding practices, input validation (to prevent SQL injection, XSS).  
   - **Example**: Requiring a password + SMS code to log in to an app.  

5. **Data Layer**  
   - **Purpose**: Protect critical data (e.g., PII, financial records) at rest.  
   - **Security Controls**:  
     - Encryption (e.g., AES-256 for stored data).  
     - Asset classification (labeling data as public, internal, confidential).  
   - **Focus**: Ensuring confidentiality and integrity of sensitive information.  

---

### 🔒 **Why Defense in Depth Matters**
- **Redundancy**: If one layer fails (e.g., firewall bypassed), others still protect the asset.  
- **Risk Reduction**: Each layer addresses different vulnerabilities (e.g., weak passwords vs. unpatched software).  
- **Real-World Use**:  
  - Organizations combine all five layers to defend against threats like phishing, ransomware, and insider attacks.  

---

### 💡 **Takeaway for Students**
- **Layered Security = Stronger Defense**:  
  - No single tool (e.g., antivirus) can stop all threats—use a mix of controls.  
- **Think Like a Castle Architect**:  
  - Plan multiple barriers (e.g., firewalls, encryption, MFA) to protect assets.  
- **Stay Updated**:  
  - New vulnerabilities (e.g., zero-days) require constant vigilance across all layers.  
