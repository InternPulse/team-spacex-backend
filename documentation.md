# Invoice Pilot API Documentation

## Introduction

Welcome to the Invoice Pilot API documentation. This API provides functionality for creating, managing, and sending invoices. Below is an overview of the available endpoints and their functionalities.

## Authentication

The API uses token-based authentication. To authenticate, obtain a token by calling the `login` endpoint with valid credentials. Include the token in the Authorization header for subsequent requests.

### Sign Up

- **Endpoint:** `POST /signup/`
- **Description:** Create a new user account.
- **Request:**
  - Body:
    ```json
    {
      "username": "new_user",
      "password": "password123"
    }
    ```
- **Response:**
  - Successful:
    ```json
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```

### Login

- **Endpoint:** `POST /login/`
- **Description:** Obtain a token for authentication.
- **Request:**
  - Body:
    ```json
    {
      "username": "existing_user",
      "password": "password123"
    }
    ```
- **Response:**
  - Successful:
    ```json
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```

## User Account

### My Account

- **Endpoint:** `GET /myaccount/`
- **Description:** Retrieve user account details.
- **Authentication:** Required (Token)
- **Response:**
  - User profile details.

## Invoices

### Invoice List and Creation

- **Endpoint:** `GET /invoices/`
- **Description:** Retrieve a list of invoices or create a new invoice.
- **Authentication:** Required (Token)
- **Request (Creation):**
  - Body:
    ```json
    {
      "title": "Invoice Title",
      "amount": 100.50,
      "recipent": 1
      // Additional fields as needed
    }
    ```
- **Response (List):**
  - List of invoices.

### Dashboard

- **Endpoint:** `GET /dashboard/`
- **Description:** Retrieve the user's dashboard with the latest invoices.
- **Authentication:** Required (Token)
- **Response:**
  - Latest invoices.

...

# Additional Endpoints

You can include additional endpoints and their documentation as needed.
