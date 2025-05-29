### 🔍 **Hash Functions: Detecting Tampering**
- **What is a Hash Function?**  
  - A one-way algorithm that converts data into a unique fixed-length string called a **hash value** (or digest).  
  - Cannot be reversed to retrieve original data (unlike encryption).  
- **Purpose**:  
  - Verify **data integrity** (accuracy and consistency of information).  
  - Detect unauthorized changes (e.g., malicious file modifications).  

---

### 🧪 **How Hashing Works (Example)**  
1. **Original File**:  
   - A company’s internal program is hashed using an algorithm like **MD5** or **SHA-256**.  
   - Output: A unique hash value (e.g., `a1b2c3d4e5`).  
2. **Modified File**:  
   - An attacker replaces the file with a malicious version.  
   - Even a single line of code change produces a **different hash** (e.g., `z9y8x7w6v5`).  
3. **Detection**:  
   - Compare hash values: Mismatch = tampering detected.  

---

### 🛡️ **Key Concepts**
1. **Data Integrity**  
   - Ensures data remains accurate and unchanged during storage/transmission.  
2. **Non-Repudiation**  
   - Proves authenticity of data; the originator cannot deny the validity of the information.  
3. **Common Hash Algorithms**:  
   - **MD5** (older, less secure due to collisions).  
   - **SHA-256** (modern, widely used for security).  

---

### 🛠️ **Practical Uses of Hashing**
- **Malware Detection**:  
  - Compare file hashes against databases like **VirusTotal** to identify malicious files.  
- **File Verification**:  
  - Use Linux commands like `sha256sum newfile.txt` to generate/check hash values.  
- **Password Storage**:  
  - Systems store password hashes (not plaintext) to protect credentials.  

---

### 💡 **Takeaway for Students**
- **Hashing ≠ Encryption**:  
  - Encryption is reversible (uses keys); hashing is irreversible (no decryption).  
- **Tamper Detection**:  
  - Even minor changes to data alter the hash, making it a powerful tool for security analysts.  
- **Real-World Tools**:  
  - Master basic hash commands (e.g., `sha256sum`) and platforms like VirusTotal for threat analysis.  
