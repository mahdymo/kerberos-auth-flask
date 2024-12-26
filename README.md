# Kerberos Authentication Flask App

This repository provides a Flask-based application to handle Kerberos authentication, supporting both a web GUI and API calls for flexibility.

## Features
- **GUI**: A web interface for users to input their credentials.
- **API**: REST endpoints to authenticate users and list Kerberos tickets programmatically.
- **Kerberos Integration**: Uses `kinit` and `klist` to manage tickets.

## Requirements
- Python 3.8+
- Kerberos installed and configured on the host system.

## Installation
1. Install kerberos package 

- sudo apt-get update
- sudo apt-get install -y krb5-user

2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/kerberos-auth-flask.git
   cd kerberos-auth-flask
3. pip install -r requirements.txt

4. python app.py

5. Access the app:

GUI: http://<Server-IP>:5000
API: Use endpoints at http://<Server-IP>:5000


### **API Endpoints**

#### **1. Authenticate User**
- **Endpoint**: `POST /authenticate`
- **Request**:
  - Content-Type: `application/json`
  - Body:
    ```json
    {
        "user_principal": "user@REALM.COM",
        "password": "yourpassword"
    }
    ```
- **Response**:
  - **Success**:
    ```json
    {
        "status": "success",
        "message": "Authentication successful!"
    }
    ```
  - **Error**:
    ```json
    {
        "status": "error",
        "message": "Authentication failed"
    }
    ```

#### **2. List Tickets**
- **Endpoint**: `GET /list_tickets`
- **Request**: No body required.
- **Response**:
  - **Success**:
    ```json
    {
        "status": "success",
        "tickets": "<output of klist>"
    }
    ```
  - **Error**:
    ```json
    {
        "status": "error",
        "message": "<error message>"
    }
    ```

