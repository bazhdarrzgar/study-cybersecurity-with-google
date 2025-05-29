### **SQL Data Types & Advanced Filtering for Security Analysts**  

#### **1. Common Data Types in SQL**  
- **String (Text)**:  
  - Ordered sequence of characters (letters, numbers, symbols).  
  - **Examples**: usernames (`analyst10`), IP addresses (`192.168.1.100`).  
  - **Operators**: `=`, `!=`, `LIKE`, `%` wildcard.  

- **Numeric**:  
  - Numbers used for mathematical operations (e.g., counts, IDs).  
  - **Examples**: failed login counts (`attempts = 5`), machine IDs (`device_id = 1234`).  
  - **Operators**: `=`, `>`, `<`, `BETWEEN`, `IN`.  

- **Date/Time**:  
  - Represents dates and timestamps (e.g., `2023-10-01`, `18:00`).  
  - **Examples**: patch dates (`OS_patch_date`), login timestamps (`timestamp`).  
  - **Operators**: `=`, `>`, `<`, `BETWEEN`, `EXTRACT`.  

---

#### **2. Filtering with Numeric & Date/Time Data**  
- **Numeric Filters**:  
  - **Example**: Find machines with over 100 failed login attempts:  
    ```sql
    SELECT * FROM endpoint_logs 
    WHERE failed_attempts > 100;
    ```  

- **Date/Time Filters**:  
  - **Example**: Find login attempts after 6 PM:  
    ```sql
    SELECT * FROM login_attempts 
    WHERE time > '18:00';
    ```  
  - **Range Filtering with `BETWEEN`**:  
    ```sql
    SELECT * FROM machines 
    WHERE OS_patch_date BETWEEN '2021-03-01' AND '2021-09-01';
    ```  
    - Returns machines patched between March 1, 2021, and September 1, 2021.  

- **Security Use Cases**:  
  - Identify unpatched systems:  
    ```sql
    SELECT hostname FROM systems 
    WHERE last_patch_date < '2023-09-01';
    ```  
  - Detect off-hours activity (potential insider threats):  
    ```sql
    SELECT * FROM access_logs 
    WHERE timestamp > '18:00' AND action = 'delete';
    ```  

---

#### **3. Syntax Rules & Best Practices**  
- **Quotation Marks**:  
  - Use quotes for **strings** and **dates** (e.g., `'USA'`, `'2023-01-01'`).  
  - Omit quotes for **numbers** (e.g., `attempts > 100`).  

- **Case Sensitivity**:  
  - SQL keywords (`SELECT`, `WHERE`) are case-insensitive, but best practice is to capitalize them.  
  - String comparisons may be case-sensitive depending on the database (e.g., PostgreSQL vs. MySQL).  

- **Performance Tips**:  
  - Avoid leading wildcards (`LIKE '%error'`) in large datasets.  
  - Use `BETWEEN` for efficient range queries (e.g., date ranges, numeric thresholds).  

---

#### **4. Security Analyst Workflow Examples**  
1. **Detecting Brute-Force Attacks**:  
   ```sql
   SELECT ip_address, COUNT(*) AS attempts 
   FROM login_attempts 
   WHERE status = 'failed' 
   GROUP BY ip_address 
   HAVING attempts > 100;
   ```  
   - Prioritize IPs with over 100 failed attempts.  

2. **Audit Patch Compliance**:  
   ```sql
   SELECT hostname, OS_patch_date 
   FROM systems 
   WHERE OS_patch_date < '2023-09-01';
   ```  
   - Flag systems not updated in the last 30 days.  

3. **Track Suspicious Logins**:  
   ```sql
   SELECT * FROM access_logs 
   WHERE timestamp > '18:00' AND username = 'admin';
   ```  
   - Identify admin logins outside business hours.  

---

#### **5. Key Takeaways**  
- **Data Types Matter**:  
  - Use `LIKE` for string patterns (e.g., `ip_address LIKE '192.168.1.%'`).  
  - Use `BETWEEN` for numeric ranges (e.g., failed attempts > 100) or date ranges.  
- **Security Focus**:  
  - Filter logs for anomalies (e.g., late-night logins, unpatched systems).  
  - Combine filters with `AND`/`OR` to prioritize high-risk events.  
- **Practice**:  
  - Apply these techniques to real-world datasets (e.g., firewall logs, endpoint activity).  

**Next Step**: Learn to sort and aggregate data (`ORDER BY`, `GROUP BY`, `COUNT`) to identify trends and generate actionable insights. 🔍🔒