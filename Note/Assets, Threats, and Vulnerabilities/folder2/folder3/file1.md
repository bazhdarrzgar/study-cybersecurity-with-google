### 🔒 **Access Controls: Managing Who Gets In**
- **Purpose**:  
  - Protect data confidentiality, integrity, and availability.  
  - Ensure users get the right information quickly while keeping it secure.  
- **AAA Framework**:  
  1. **Authentication**: Verify identity ("Who are you?").  
  2. **Authorization**: Define access rights ("What can you do?").  
  3. **Accounting**: Track activity ("What did you do?").  

---

### 🧑‍💼 **Authentication: Proving Identity**
- **Definition**: The process of verifying who a user or system claims to be.  
- **3 Factors of Authentication**:  
  1. **Knowledge** (Something You Know):  
     - Passwords, PINs, security questions.  
  2. **Ownership** (Something You Have):  
     - One-Time Passwords (OTPs) via SMS/email, hardware tokens (e.g., YubiKey).  
  3. **Characteristic** (Something You Are):  
     - Biometrics (fingerprint, facial recognition, voice ID).  

---

### 🔐 **Single Sign-On (SSO)**
- **What It Is**:  
  - A system that lets users access multiple services with one login.  
- **Why It’s Useful**:  
  - Reduces password fatigue (no need to log in repeatedly).  
- **Security Risk**:  
  - If credentials are stolen, attackers gain access to all linked accounts.  
- **Best Practice**:  
  - Combine SSO with Multi-Factor Authentication (MFA) for stronger security.  

---

### 🛡️ **Multi-Factor Authentication (MFA)**
- **Definition**: Requires **two or more authentication factors** to verify identity.  
- **Example**:  
  - Password (knowledge) + OTP (ownership).  
  - Fingerprint (characteristic) + hardware token (ownership).  
- **Why It’s Stronger**:  
  - Even if one factor is compromised (e.g., password), the attacker still needs another factor.  
- **Common Use Cases**:  
  - Banking apps (password + SMS code).  
  - Corporate networks (smartcard + PIN).  

---

### ⚠️ **Authentication Risks**
- **False Rejection**:  
  - Legitimate users denied access (e.g., forgotten password).  
- **False Acceptance**:  
  - Unauthorized users granted access (e.g., stolen credentials).  
- **Mitigation**:  
  - Use MFA to reduce both risks.  

---

### 💡 **Takeaway for Students**
- **Authentication ≠ Authorization**:  
  - Authentication = Prove who you are.  
  - Authorization = Define what you can access (covered next!).  
- **Balance Convenience & Security**:  
  - SSO speeds up access but requires MFA to stay secure.  
- **Real-World Tip**:  
  - Enable MFA on personal accounts (email, banking) to prevent breaches.  
