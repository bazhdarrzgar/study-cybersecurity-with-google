### **Linux User Management for Security Analysts**  

#### **1. Authentication & User Management**  
- **Authentication**:  
  - Process of verifying a user’s identity (e.g., via username/password).  
  - Ensures only authorized users access the system.  

- **Add/Delete Users**:  
  - **Add**: When new employees join or roles change (e.g., `salesrep7` added to the sales team).  
  - **Delete**: When users leave the organization or no longer need access.  

---

#### **2. Root User vs. `sudo`**  
- **Root (Superuser)**:  
  - Has **full system privileges** (can modify/delete any file, run any command).  
  - **Risks**:  
    - High security risk (target for attackers).  
    - Easy to make irreversible mistakes (e.g., deleting critical files).  
    - Lack of accountability in multi-user environments.  

- **`sudo` (Super-User-Do)**:  
  - Grants **temporary elevated privileges** to specific users.  
  - **Advantages**:  
    - Tracks who ran which commands.  
    - Reduces accidental damage (users only elevate when needed).  
    - Configured via the **sudoers file** (`/etc/sudoers`).  

---

#### **3. Key Commands for User Management**  
- **`useradd` (Add a User)**:  
  - Syntax: `sudo useradd [username]`  
  - Example: `sudo useradd salesrep7` → Adds a new user named `salesrep7`.  
  - Requires **sudo privileges** to execute.  

- **`userdel` (Delete a User)**:  
  - Syntax: `sudo userdel [username]`  
  - Example: `sudo userdel salesrep7` → Removes `salesrep7` from the system.  
  - Also requires **sudo privileges**.  

- **Verify Changes**:  
  - Use `cat /etc/passwd` to check user existence (lists all users).  

---

#### **4. Security Best Practices**  
- **Principle of Least Privilege**:  
  - Grant users only the access they need (e.g., regular users should not have `sudo` rights unless required).  

- **Avoid Root Login**:  
  - Disable direct root login to reduce attack surface. Use `sudo` instead.  

- **Audit User Activity**:  
  - Track `sudo` commands via logs (`/var/log/auth.log`) to monitor privileged actions.  

- **Clean Up Unused Accounts**:  
  - Remove users who leave the organization to prevent unauthorized access.  

---

### **Summary**  
- **Authentication**: Control system access by adding/deleting users as roles change.  
- **`sudo`**: Safer alternative to root for privileged tasks (tracks accountability, reduces risks).  
- **Commands**:  
  - `sudo useradd [username]` → Add users.  
  - `sudo userdel [username]` → Remove users.  
- **Security Focus**: Follow least privilege, disable root login, and audit privileged actions.  
- **Next Step**: Learn to manage user groups (`groupadd`, `usermod`) and permissions (`chown`, `chmod`) for fine-grained access control.