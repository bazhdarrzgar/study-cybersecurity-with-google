### 🔐 **Authorization: Defining Access Rights**
- **Definition**:  
  - Determines what a user or system **can do** after authentication (e.g., view files, edit data, delete records).  
- **Key Difference from Authentication**:  
  - **Authentication** = "Who are you?"  
  - **Authorization** = "What can you access?"  

---

### 🧱 **Core Principles of Authorization**
1. **Principle of Least Privilege**  
   - Users/systems should only have **minimum access needed** to perform their role.  
   - Example: A customer service rep shouldn’t have admin-level access to financial records.  

2. **Separation of Duties**  
   - Prevents misuse by dividing critical tasks among multiple people/systems.  
   - Example:  
     - One person develops a system; another tests it.  
     - A manager can’t approve their own performance review.  

---

### 🛠️ **Common Authorization Methods**
#### 1. **HTTP Basic Auth**  
- **How It Works**:  
  - Sends username/password in plaintext with every request.  
- **Security Risk**:  
  - Credentials are exposed during transmission (use only over HTTPS).  

#### 2. **OAuth**  
- **Purpose**:  
  - Securely shares access between apps without sharing passwords.  
- **How It Works**:  
  - Uses **API tokens** (encrypted code with user identity/permissions) for authorization.  
- **Example**:  
  - Logging into a website using your Google account without sharing your Google password.  
  - Google sends an API token to verify your identity securely.  

#### 3. **HTTPS**  
- **Improvement Over HTTP**:  
  - Encrypts communication (including credentials/tokens) to prevent eavesdropping.  

---

### 🧩 **Real-World Authorization Risks**
- **Overprivileged Users**:  
  - Employees with excessive access can accidentally or intentionally misuse data.  
- **Lack of Separation**:  
  - One person controlling too many roles increases risk of errors or fraud.  

---

### 💡 **Takeaway for Students**
- **Authorization ≠ Authentication**:  
  - Authentication confirms identity; authorization defines permissions.  
- **Security Best Practices**:  
  - Use **OAuth** (token-based) instead of HTTP Basic Auth (plaintext risks).  
  - Always enforce **HTTPS** for encrypted data transfer.  
  - Apply **least privilege** and **separation of duties** to users, systems, and processes.  
- **Monitor Access**:  
  - Track who accesses what (next topic: **Accounting** in the AAA framework).  
