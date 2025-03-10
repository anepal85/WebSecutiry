# CSRF Attack Demonstration in Flask

This project demonstrates how a **Cross-Site Request Forgery (CSRF)** attack can occur in a vulnerable Flask web application. It showcases how an attacker can exploit a lack of CSRF protection to perform unauthorized actions on behalf of an authenticated user.

---

## What is CSRF?

**Cross-Site Request Forgery (CSRF)** is an attack that tricks a user into performing actions they did not intend to perform. For example, an attacker can force a logged-in user to change their email address, transfer funds, or perform other sensitive actions without their knowledge.

---

## How This Project Demonstrates CSRF

### 1. **Vulnerable Flask Application**
The Flask application in this project has a **CSRF vulnerability** in the `/update-email` endpoint. This endpoint allows authenticated users to update their email address. However, it does not validate the source of the request, making it susceptible to CSRF attacks.

### 2. **Malicious Page**
The attacker hosts a malicious page (`malicious.html`) that contains JavaScript code to send a POST request to the `/update-email` endpoint. When the victim clicks a link on this page, the attacker's script sends a request to change the victim's email address to `attacker@hacked.com`.

### 3. **Exploitation**
- The victim logs into the Flask application and remains authenticated.
- The victim visits the malicious page (hosted by the attacker).
- The malicious page sends a POST request to the Flask application, changing the victim's email address without their consent.

---

## Disclaimer

This project is for **educational purposes only**. It demonstrates a security vulnerability to help developers understand and mitigate CSRF risks. Do not use this code in production or for malicious purposes.

---