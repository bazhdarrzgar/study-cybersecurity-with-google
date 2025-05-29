### 📋 **Accounting: Monitoring Access Logs**
- **Definition**:  
  - The third part of the **AAA framework** (Authentication, Authorization, Accounting).  
  - Tracks **who accessed a system**, **when**, and **what they did**.  
- **Purpose**:  
  - Detect suspicious activity (e.g., failed logins, data breaches).  
  - Investigate security incidents.  
  - Maintain accountability for users and systems.  

---

### 📒 **Access Logs: What They Record**
- **Key Details**:  
  - User identity (e.g., username).  
  - Timestamp (when access occurred).  
  - Resources accessed (e.g., files, databases).  
  - Session duration (start and end times).  
- **Why They Matter**:  
  - Help identify patterns (e.g., repeated login attempts).  
  - Reveal unauthorized access (e.g., hackers stealing data).  
  - Serve as evidence during audits or investigations.  

---

### 🔄 **Sessions: Tracking User Activity**
- **What is a Session?**:  
  - A temporary connection between a user and a system (e.g., logging into a website).  
- **Session ID**:  
  - A unique token generated when a session starts.  
  - Identifies the user/device during the session.  
  - Expires when the user logs out or the session times out.  
- **Session Cookie**:  
  - A small data file exchanged between the server and user’s device.  
  - Validates the session and controls its duration.  
  - Prevents sharing sensitive data (e.g., passwords) during the session.  

---

### ⚠️ **Session Hijacking: A Major Risk**
- **What It Is**:  
  - Attackers steal a valid **session ID or cookie** to impersonate a user.  
- **Consequences**:  
  - Steal money or private data.  
  - Gain access to linked systems (e.g., via Single Sign-On).  
- **How It Happens**:  
  - Intercepting unencrypted cookies (use **HTTPS** to prevent this).  
  - Exploiting vulnerabilities in poorly secured websites.  

---

### 🔍 **Security Best Practices**
1. **Monitor Access Logs**:  
   - Look for unusual activity (e.g., logins at odd hours, unauthorized resource access).  
2. **Secure Session Cookies**:  
   - Use **HTTPS** to encrypt cookie exchanges.  
   - Set cookies to expire after short periods.  
3. **Limit Session Lifespan**:  
   - Auto-log out inactive users.  
4. **Combine with MFA**:  
   - Even if a session is hijacked, MFA adds a second layer of protection.  

---

### 💡 **Takeaway for Students**
- **Accounting = Visibility**:  
  - Without logs, you can’t detect breaches or investigate incidents.  
- **Session Security Matters**:  
  - Protect cookies and session IDs to prevent impersonation attacks.  
- **Real-World Tip**:  
  - Always use HTTPS sites (check for the padlock icon in the address bar).  
- **Next Step**:  
  - Combine accounting with authentication/authorization for a layered defense (AAA framework).  
