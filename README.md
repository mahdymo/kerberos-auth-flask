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
- from within the folder run `docker-compose build`.
- Then use `docker-compose up -d`
- You should see two containers with ports 80, 443, 5000 exposed.



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

## Ongoing enhancements 
- Use HTTPS by default
- Block access to backend except from NGINX
- Allow more authentication methods. 
