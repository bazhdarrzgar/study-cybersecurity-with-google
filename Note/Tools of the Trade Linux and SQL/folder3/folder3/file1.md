### **Linux File & Directory Permissions**  

#### **1. Permission Types**  
- **Read (`r`)**:  
  - **File**: Allows viewing contents.  
  - **Directory**: Allows listing files inside.  
- **Write (`w`)**:  
  - **File**: Allows modifying content.  
  - **Directory**: Allows creating/deleting files inside.  
- **Execute (`x`)**:  
  - **File**: Allows running the file (e.g., scripts, binaries).  
  - **Directory**: Allows accessing files inside (navigate into the directory).  

---

#### **2. Ownership Types**  
Permissions apply to three categories:  
1. **User (u)**: The **owner** of the file/directory.  
2. **Group (g)**: Users belonging to the **file’s group**.  
3. **Other (o)**: All other users on the system.  

---

#### **3. Permission Representation**  
- **10-character string**:  
  Example: `drwxrwxrwx`  
  - **1st character**: File type (`d` = directory, `-` = file).  
  - **Characters 2–4**: User permissions (e.g., `rwx`).  
  - **Characters 5–7**: Group permissions (e.g., `r--`).  
  - **Characters 8–10**: Other permissions (e.g., `---`).  

- **Example Breakdown**:  
  `drwxr-xr--` →  
  - Type: Directory (`d`).  
  - User: Read, write, execute (`rwx`).  
  - Group: Read, execute (`r-x`).  
  - Other: Read only (`r--`).  

---

#### **4. Checking Permissions**  
- **`ls -l`**: Shows permissions, owner, group, and file size.  
  Example output:  
  ```bash
  -rw-r--r-- analyst security project1.txt
  ```  
  - User (`analyst`) has read/write.  
  - Group (`security`) has read.  
  - Others have read.  

- **`ls -a`**: Lists hidden files (start with `.`).  
- **`ls -la`**: Combines both (`-l` + `-a`) to show permissions for all files, including hidden ones.  

---

#### **5. Security Implications**  
- **World-Writable Files**:  
  - Permissions like `-rwxrwxrwx` → Anyone can modify the file.  
  - **Risk**: Attackers could alter sensitive files (e.g., logs, configs).  

- **Best Practices**:  
  - Follow the **principle of least privilege** (grant only necessary access).  
  - Avoid overly permissive settings (e.g., `777` for directories).  
  - Secure sensitive data (e.g., payroll files should only be readable by authorized groups).  

---

#### **6. Commands to Modify Permissions**  
- **`chmod` (Change Mode)**:  
  - Adjust permissions using symbols or numeric codes.  
  - **Symbolic**: `chmod u+x script.sh` → Add execute permission for the user.  
  - **Numeric**: `chmod 755 folder/` → Set `rwxr-xr-x`.  
    - `7` = `rwx`, `5` = `r-x`, `0` = `---`.  

- **`chown` (Change Owner)**:  
  - Change file/directory ownership.  
  - Example: `sudo chown root:admin file.txt` → Assigns owner `root` and group `admin`.  

---

### **Summary**  
- **Permissions** control access to files/directories (read, write, execute).  
- **Ownership** defines access for the user, group, and others.  
- Use `ls -l` to audit permissions and identify security risks (e.g., world-writable files).  
- Secure systems by applying strict permissions and ownership rules (e.g., `chmod 600 sensitive.txt`).  
- **Security Analyst Use Case**: Monitor logs/configs for misconfigurations and enforce least privilege.  

**Next Step**: Practice adjusting permissions with `chmod` and ownership with `chown` to secure files in a test environment.