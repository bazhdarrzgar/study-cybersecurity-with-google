### **SQL Operators: AND, OR, NOT for Security Analysts**  

#### **1. Combining Conditions with `AND`**  
- **Purpose**: Filter rows where **all conditions** are true.  
- **Syntax**:  
  ```sql
  SELECT * FROM [table] WHERE [condition1] AND [condition2];
  ```  
- **Example**:  
  ```sql
  SELECT * FROM machines 
  WHERE os = 'OS 1' AND email_client = 'Email Client 1';
  ```  
  - Returns machines using both **OS 1** and **Email Client 1**.  

- **Security Use Case**:  
  - Identify systems with **multiple vulnerabilities** (e.g., outdated OS + unpatched software).  
  - Example:  
    ```sql
    SELECT hostname FROM systems 
    WHERE os_version = 'Windows 7' AND last_patch_date < '2023-01-01';
    ```  

---

#### **2. Expanding Filters with `OR`**  
- **Purpose**: Return rows where **any condition** is true.  
- **Syntax**:  
  ```sql
  SELECT * FROM [table] WHERE [condition1] OR [condition2];
  ```  
- **Example**:  
  ```sql
  SELECT * FROM machines 
  WHERE os = 'OS 1' OR os = 'OS 3';
  ```  
  - Finds machines using **either OS 1 or OS 3** (or both).  

- **Security Use Case**:  
  - Detect systems needing patches across multiple OS versions.  
  - Example:  
    ```sql
    SELECT ip_address FROM firewall_logs 
    WHERE action = 'blocked' OR status = 'unresolved';
    ```  

---

#### **3. Excluding Data with `NOT`**  
- **Purpose**: Return rows where a condition is **not met**.  
- **Syntax**:  
  ```sql
  SELECT * FROM [table] WHERE NOT [condition];
  ```  
  - Alternative: Use `!=` for direct comparisons.  
- **Example**:  
  ```sql
  SELECT * FROM machines 
  WHERE NOT os = 'OS 3';
  ```  
  - Returns all machines **not running OS 3**.  

- **Security Use Case**:  
  - Exclude trusted IPs from suspicious activity reports.  
  - Example:  
    ```sql
    SELECT * FROM login_attempts 
    WHERE NOT ip_address IN ('192.168.1.1', '192.168.1.2');
    ```  

---

#### **4. Combining Operators for Complex Filters**  
- **Use Parentheses** to group conditions and avoid ambiguity.  
- **Example**:  
  ```sql
  SELECT * FROM login_attempts 
  WHERE (country = 'Russia' OR country = 'China') 
  AND status = 'failed';
  ```  
  - Finds failed login attempts from specific countries.  

- **Security Use Case**:  
  - Prioritize threats with multiple criteria (e.g., failed logins + off-hours activity):  
    ```sql
    SELECT * FROM access_logs 
    WHERE status = 'failed' 
    AND timestamp > '18:00';
    ```  

---

#### **5. Security Analyst Workflow Examples**  
1. **Detecting Vulnerable Systems**:  
   ```sql
   SELECT hostname, os_version 
   FROM systems 
   WHERE (os_version = 'Windows 7' OR os_version = 'Ubuntu 18.04') 
   AND last_patch_date < '2023-01-01';
   ```  
   - Lists systems with outdated OS and missing patches.  

2. **Filtering Suspicious Logins**:  
   ```sql
   SELECT ip_address, username 
   FROM login_attempts 
   WHERE (country = 'Russia' OR country = 'China') 
   AND status = 'failed' 
   AND attempts > 10;
   ```  
   - Focuses on high-risk failed logins from specific regions.  

3. **Excluding Trusted IPs**:  
   ```sql
   SELECT * FROM firewall_logs 
   WHERE NOT ip_address IN ('192.168.1.0/24') 
   AND action = 'blocked';
   ```  
   - Identifies blocked traffic outside internal networks.  

---

#### **6. Key Tips**  
- **Order of Operations**:  
  - Use parentheses to group conditions (e.g., `(A OR B) AND C`).  
- **Case Sensitivity**:  
  - String comparisons may vary by SQL dialect (e.g., PostgreSQL is case-sensitive; use `ILIKE` for case-insensitive matches).  
- **Performance**:  
  - Avoid unnecessary complexity (e.g., `WHERE NOT status = 'blocked'` may be less efficient than `WHERE status = 'allowed'`).  

---

### **Key Takeaways**  
- **`AND`** narrows results (intersection of conditions).  
- **`OR`** broadens results (union of conditions).  
- **`NOT`** excludes specific conditions.  
- **Combine Operators** to refine security queries (e.g., detect multi-factor vulnerabilities).  
- **Practice**: Apply these operators to real-world datasets (e.g., firewall logs, endpoint data) to uncover threats.  

**Next Step**: Learn to combine data from multiple tables using **SQL Joins** to analyze relationships (e.g., linking users to suspicious login attempts). 🔍🔒