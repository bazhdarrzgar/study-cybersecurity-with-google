## 📌 What is a Join in SQL?

- A **join** combines data from two or more tables.
- It’s useful when you need to get information that exists across multiple tables.

### 🔍 Example (Cybersecurity Context):
You have:
- **`vulnerabilities` table**: Lists OS types and their known security issues.
- **`machines` table**: Lists company machines and their operating systems.

By joining these tables, you can find out:
> Which **machines are vulnerable** based on their OS.

---

## 🧠 Table Join Syntax Basics

When working with two tables that have columns with the same name (like `employee_id`), you must specify which table the column comes from using this format:

```
table_name.column_name
```

### ✅ Example:
- `employees.employee_id`
- `machines.employee_id`

This helps avoid confusion between similar column names in different tables.

---

## 🔗 INNER JOIN Explained

### 📝 Definition:
An **INNER JOIN** returns only the rows where there is a **match** in both tables on a specific column.

### 💡 Use Case (Security):
Find employees who have assigned machines and see what OS they are using — so you can check for vulnerabilities.

### 🧪 Example:
```sql
SELECT employees.username, employees.office, machines.operating_system
FROM employees
INNER JOIN machines
ON employees.employee_id = machines.employee_id;
```

### 📋 Result:
- Shows only **matching records**.
- Includes selected columns from **both tables**.
- Ignores rows without matches.

---

## ⚠️ What About NULL Values?

- In SQL, **NULL** means a value is **missing or unknown**.
- For example: A machine not assigned to any employee might have a **NULL** `employee_id`.

> **INNER JOIN ignores NULL values**. Only matching rows are returned.

---

## 🎯 Why This Matters in Cybersecurity?

- You often work with multiple data sources (users, devices, logs, vulnerabilities).
- **JOINs help combine** this data to answer questions like:
  - Which users are using outdated software?
  - What machines are missing security patches?
  - Who accessed a sensitive system?

---

## 📝 Summary of Key Points

| Concept             | Description |
|---------------------|-------------|
| **Join**            | Combines data from two or more tables |
| **INNER JOIN**      | Returns only matching rows from both tables |
| **Table.Column**    | Used to avoid confusion between duplicate column names |
| **NULL**            | Represents missing data; ignored by INNER JOIN |
| **Primary Key**     | Unique identifier in a table (e.g., `employee_id`) |
| **Foreign Key**     | Links one table to another (e.g., `employee_id` in `machines`) |

