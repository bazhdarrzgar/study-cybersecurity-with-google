### **Linux Commands for Security Analysts**  

#### **1. Linux File System Navigation & Management**  
- **Core Commands**:  
  - `ls` – List files/directories in the current directory.  
    Example: `ls -la` (shows hidden files + permissions).  
  - `cd` – Change directory.  
    Example: `cd /home/user/Documents` (navigate to a specific folder).  
  - `pwd` – Print working directory (show current location in the file system).  
  - `mkdir` – Create a new directory.  
    Example: `mkdir reports` (create a folder named "reports").  
  - `touch` – Create an empty file or update a file’s timestamp.  
    Example: `touch notes.txt` (create a new file).  
  - `cp` – Copy files/directories.  
    Example: `cp file.txt backup/` (copy "file.txt" to the "backup" folder).  
  - `mv` – Move or rename files.  
    Example: `mv oldname.txt newname.txt` (rename a file).  
  - `rm` – Remove/delete files or directories.  
    Example: `rm -r folder/` (delete a folder and its contents).  

---

#### **2. User Authentication & Authorization**  
- **User Management**:  
  - `useradd` – Add a new user.  
    Example: `sudo useradd john` (create a user named "john").  
  - `passwd` – Set or change a user’s password.  
    Example: `sudo passwd john` (set a password for "john").  
  - `userdel` – Delete a user.  
    Example: `sudo userdel john` (remove the user "john").  

- **Permissions Management**:  
  - `chmod` – Change file/directory permissions.  
    Example: `chmod 755 script.sh` (set read/write/execute for owner, read/execute for others).  
  - `chown` – Change file/directory ownership.  
    Example: `sudo chown john:users file.txt` (assign "file.txt" to user "john" and group "users").  
  - `sudo` – Execute commands with administrative privileges.  
    Example: `sudo apt update` (update software packages with elevated rights).  

- **User Groups**:  
  - `groups` – Show groups a user belongs to.  
    Example: `groups john` (list groups for user "john").  

---

#### **3. Learning Resources for Linux Commands**  
- **Built-in Help**:  
  - `man [command]` – View the manual for a command.  
    Example: `man ls` (learn options for listing files).  
  - `[command] --help` – Quick reference for command syntax.  
    Example: `grep --help` (see options for searching text).  

- **Online Documentation**:  
  - Official distro guides (e.g., Kali Linux documentation, Ubuntu help).  
  - Cybersecurity forums (e.g., Stack Overflow, Reddit’s r/linux).  

- **Practice Environments**:  
  - Use **virtual machines** (e.g., VirtualBox, VMware) to safely experiment.  
  - Online platforms like **OverTheWire** or **TryHackMe** for hands-on challenges.  

---

### **Summary**  
- **File System Commands**: Essential for navigating, managing, and manipulating files/directories.  
- **User & Permissions Commands**: Critical for securing systems, controlling access, and auditing accounts.  
- **Security Analyst Use Cases**:  
  - Analyze logs with `cat`, `grep`, or `less`.  
  - Secure sensitive files using `chmod` and `chown`.  
  - Automate tasks with scripts combining multiple commands.  
- Mastering these commands empowers you to perform forensic analysis, penetration testing, and system hardening effectively.  

**Next Step**: Practice these commands in a controlled environment (e.g., Kali Linux VM) to build confidence and efficiency.