# Foundation-Of-Computer
# ST4015CMD Coursework - Enhancing Secure Data Exchange

This repository contains my coursework for **ST4015CMD: Foundation of Computer Science**, focusing on secure data exchange, computational complexity, and database normalization.

## Task 1: Encoding Formats and Secure Transmission
In Task 1, I explored how different **encoding formats** are used to prepare data for transmission across networks. The main activities include:
- Studying **ASCII, Base64, Hex, and URL encoding** and how they represent data in safe formats.
- Evaluating the **strengths and weaknesses** of each encoding format.
- Explaining how **encoding is combined with encryption protocols** (HTTPS, TLS) to ensure secure communication.
- Demonstrating encoding in **HTTP requests**, protecting against injection attacks (SQL Injection, XSS).

**Purpose:** Show how data can be safely transmitted between systems while maintaining integrity and compatibility.

---

## Task 2: Computational Complexity and P vs NP
In Task 2, I analyzed **computational complexity** and its relevance to real-world cybersecurity problems. The main activities include:
- Explaining the **P vs NP problem** and NP-completeness.
- Using a **classroom seating arrangement example** to illustrate verification vs solution-finding:
  - Verification of a seating plan → Polynomial time (P)
  - Finding a correct seating arrangement → Factorial growth (NP)
- Demonstrating **brute-force vs heuristic methods**.
- Relating heuristics to **malware detection**, where real-time detection requires approximate solutions instead of exhaustive search.

**Purpose:** Highlight why heuristic approaches are necessary in cybersecurity applications and large-scale data problems.

---

## Task 3: Database Normalization and SQL Operations
In Task 3, I focused on **database design, normalization, and practical SQL queries**. The main activities include:
- Identifying **problems in an unnormalized table**, including redundancy and anomalies.
- Applying **First, Second, and Third Normal Form (1NF, 2NF, 3NF)** to restructure tables into:
  - **Student table**
  - **Club table**
  - **Membership table**
- Designing a **clean Entity-Relationship (ER) model**.
- Writing **SQL queries** to:
  - Insert students and clubs
  - Display data
  - Perform JOIN operations between tables
- Using **Z3 solver** (optional) to check constraints like uniqueness in memberships and validate logical rules.

**Purpose:** Ensure data integrity, eliminate redundancy, and demonstrate correct database operations with SQL.

---

**Overall**, this coursework demonstrates a combination of:
- Safe data transmission using encoding and encryption
- Understanding computational complexity and practical heuristics
- Designing a normalized relational database and implementing SQL operations
