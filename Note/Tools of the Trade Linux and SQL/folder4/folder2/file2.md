### **SQL Filtering with `WHERE` & `LIKE` for Security Analysts**  

#### **1. Basic Filtering with `WHERE`**  
- **Purpose**: Narrow down results to specific rows based on conditions.  
- **Syntax**:  
  ```sql
  SELECT [columns] FROM [table] WHERE [condition];
  ```  
- **Example**:  
  ```sql
  SELECT * FROM login_attempts WHERE country = 'USA';
  ```  
  - Returns all login attempts from the **United States**.  

- **Security Use Case**:  
  - Filter logs for specific threats (e.g., failed logins from a country).  
  - Example:  
    ```sql
    SELECT * FROM firewall_logs WHERE action = 'blocked' AND source_ip LIKE '192.168.1.%';
    ```  

---

#### **2. Pattern Matching with `LIKE`**  
- **Why Use It?**: Handle inconsistent data (e.g., "US" vs. "USA") or search for partial matches.  
- **Wildcards**:  
  - `%`: Matches **any number of characters**.  
  - `_`: Matches **one character**.  

- **Syntax**:  
  ```sql
  SELECT [columns] FROM [table] WHERE [column] LIKE [pattern];
  ```  
- **Examples**:  
  - **Match "US" or "USA"**:  
    ```sql
    SELECT * FROM login_attempts WHERE country LIKE 'US%';
    ```  
  - **Find offices in the East building**:  
    ```sql
    SELECT * FROM employees WHERE office LIKE 'East%';
    ```  
    - Matches "East-120", "East-290", etc.  

- **Security Use Case**:  
  - Detect suspicious URLs or IPs with partial matches:  
    ```sql
    SELECT * FROM web_requests WHERE url LIKE '%/admin%';
    ```  
    - Finds all accesses to admin pages (potential insider threats).  

---

#### **3. Combining Conditions**  
- **Multiple Filters**: Use `AND`, `OR`, `NOT` to refine queries.  
- **Example**:  
  ```sql
  SELECT * FROM login_attempts 
  WHERE country LIKE 'US%' AND status = 'failed';
  ```  
  - Returns failed login attempts from the U.S.  

- **Security Use Case**:  
  - Prioritize high-risk events:  
    ```sql
    SELECT * FROM endpoint_logs 
    WHERE process_name = 'malicious.exe' OR user = 'admin';
    ```  

---

#### **4. Key Tips for Security Analysts**  
- **Avoid Overly Broad Patterns**:  
  - `LIKE '%error%'` may return unintended matches. Be specific (e.g., `LIKE '404%'`).  
- **Case Sensitivity**:  
  - Some SQL dialects (e.g., PostgreSQL) treat `LIKE` as case-sensitive. Use `ILIKE` (in PostgreSQL) or `LOWER()` for case-insensitive searches.  
- **Performance**:  
  - Leading wildcards (`LIKE '%East'`) can slow queries. Avoid them for large datasets.  

---

### **Security Analyst Workflow Examples**  
1. **Detecting Brute-Force Attacks**:  
   ```sql
   SELECT ip_address, COUNT(*) AS attempts 
   FROM login_attempts 
   WHERE status = 'failed' 
   GROUP BY ip_address 
   HAVING COUNT(*) > 100;
   ```  
2. **Audit Unpatched Systems**:  
   ```sql
   SELECT hostname, last_patch_date 
   FROM systems 
   WHERE last_patch_date < '2023-09-01';
   ```  
3. **Track Suspicious Activity**:  
   ```sql
   SELECT timestamp, user, action 
   FROM access_logs 
   WHERE ip_address = '192.168.1.100' AND action = 'delete';
   ```  

---

### **Key Takeaways**  
- **Filtering** reduces noise and focuses on relevant data (e.g., failed logins, unpatched systems).  
- **`LIKE`** handles inconsistent data and partial matches (e.g., "US" vs. "USA").  
- **Combine Conditions** with `AND`/`OR` to prioritize threats (e.g., failed logins + suspicious IPs).  
- **Practice**: Use real-world datasets (e.g., exported logs) to refine your SQL skills.  

**Next Step**: Learn to sort and aggregate data with `ORDER BY`, `GROUP BY`, and `COUNT()` to identify trends in security events. 🔍🔒