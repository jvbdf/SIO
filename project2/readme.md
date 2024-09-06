Report  \- **Project 2** 

# **DETI SHOP**

| Course: | SIO   |
| :---- | :---- |
| Date: | Aveiro, 05/09/2024 |
| Student: | 106078 : João Vitor B. D. Ferreira  |


## 1. Introduction

Deti Shop is a web application where users can buy memorabilia from DETI (Department of Electronics Telecommunications and Informatics) at the University of Aveiro. 

The Deti Shop web application allows users to purchase various DETI-themed items, such as mugs, t-shirts, and hoodies, via a secure and user-friendly platform. Developed for the Department of Electronics, Telecommunications, and Informatics (DETI) at the University of Aveiro, the platform serves both students and faculty. Its goal is to provide a seamless online shopping experience, including user registration, profile management, shopping cart features, and a checkout system.

**Example:** A student who wants to buy a hoodie can register an account, browse available items, add the hoodie to their cart, and complete the purchase using their preferred payment method.

## 2. System Description

Deti Shop is built using the Flask web framework, utilizing its modular architecture. The system handles various functions such as account registration, login, shopping cart management, and order processing. SQLite is used as the database system, and the project follows Flask’s application factory pattern to enhance scalability and maintainability.

**Example:** When a user registers, the system creates a new record in the SQLite database and allows the user to upload a profile picture, which is stored securely. This picture is later displayed in the user’s account section.

## 3. Project Overview

The project was centered around conducting a comprehensive security audit using the OWASP Application Security Verification Standard (ASVS). After identifying various vulnerabilities, we rectified issues to meet 50 out of the 78 Level 1 ASVS criteria. This significantly improved the system's overall security posture, addressing sensitive aspects like password management, file uploads, and multi-factor authentication (MFA).

**Example:** Post-audit, a user who tries to register with a weak password like "12345" will be prompted to create a stronger password due to the new password policy enforcement.

## 4. Overcome Vulnerabilities

### 4.1 Password Security Credentials

We implemented stringent password policies to meet the ASVS standards, including checking for minimum password length and preventing password truncation.

**Example:** A user entering a password like "  Pass word123 " would have all excess spaces stripped, ensuring that the password is "Password123" without affecting its length or complexity.

### 4.2 File Upload Requirements

We imposed a 1MB limit on file uploads to prevent abuse and potential denial-of-service attacks.

**Example:** A user uploading a profile image larger than 1MB receives an error message explaining the file exceeds the allowable size, prompting them to resize their image.

### 4.3 General Authenticator Requirements

To mitigate brute-force attacks, CAPTCHA was integrated into both the login and registration processes. This prevents automated scripts from exploiting the system.

**Example:** After several failed login attempts, the user must solve a CAPTCHA challenge to proceed, slowing down any automated attacks.

### 4.4 Password Breach Check

We integrated the "Have I Been Pwned" API to check if a user's chosen password has been compromised in any known data breaches.

**Example:** If a user attempts to set their password as "password123," they are notified that this password has been breached and must choose a different one.

### 4.5 Password Strength Meter

We added a password strength meter, offering users real-time feedback as they type their password.

**Example:** A visual progress bar dynamically changes as the user types, indicating the strength of their password, from "Very Weak" to "Very Strong."

### 4.6 TOTP-based Multi-Factor Authentication (MFA)

The system now supports time-based one-time passwords (TOTP) as a secondary authentication method using pyotp.

**Example:** After entering their username and password, a user scans a QR code with their authenticator app to complete the login using a time-sensitive six-digit code.

# **4- How to run the application**



#### Create Virtual environment
You must be in the correct directory, either app_org or app_sec folder

```bash
python -m venv env
```

#### Activate the environment and then install requirements
```bash
pip install -r requirements.txt
```
#### Create the Database

In the activated terminal execute the following commands in the /app folder (important):

```bash
flask shell
```
Within the flask shell type:
```bash
db.create_all()
from app.populate_db import create_all
create all()
quit()
```
#### Execute the application
```bash
flask- run -p <desired port here>
```
