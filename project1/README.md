Report  \- **Project 1** 

# **DETI SHOP**

| Course: | SIO \-  |
| :---- | :---- |
| Date: | Aveiro, 05/09/2024 |
| Student: | 106078 : João Vitor B. D. Ferreira  |

# **1- Introduction**

Deti Shop is a web application where users can buy memorabilia from DETI (Department of Electronics, Telecommunications, and Informatics) at the University of Aveiro.The online shop has a variety of items, including mugs, cups, t-shirts, hoodies

# **2- System description**

This project is a web-based e-commerce platform built using **Flask**. It enables users to register accounts, log in, manage shopping carts, place orders, manage user profiles, and upload profile images. The application employs **SQLite** as its database, and it follows the **blueprint architecture** and **application factory pattern** of Flask to organize the various modules of the system.

The system was structured to be modular, making it easier to maintain and scale. Several common web security vulnerabilities (CWEs) have been intentionally implemented or may exist due to a lack of proper security practices.

# **3- Security Weaknesses (CWEs)**

#### **1\. CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')**

#### **2\. CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')**

#### **3\. CWE-620: Unverified Password Change**

#### **4\. CWE-916: Use of Password Hash with Insufficient Computational Effort**

#### **5\. CWE-287: Improper Authentication**

#### **6\. CWE-521: Weak Password Requirements**

#### **7\. CWE-20: Improper Input Validation**

#### **8\. CWE-434: Unrestricted Upload of File with Dangerous Type**

#### **9\. CWE-22: Path Traversal**

#### **10\. CWE-285: Improper Authorization\*\*(Subtle Vulnerability)\*\***

#### **11\. CWE-352: Cross-Site Request Forgery (CSRF)** 

# **4- How to run the application**
