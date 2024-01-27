# InvoicePilot API Documentation

## Introduction
InvoicePilot is an API designed to manage invoices, customers, and user authentication. This document outlines all the available endpoints in the InvoicePilot API along with their functionalities.

## Authentication
InvoicePilot API uses JSON Web Tokens (JWT) for authentication. Users can sign up, log in, log out, and refresh their tokens using the provided endpoints.

### Endpoints:
- `/auth/signup`: Allows users to sign up by providing their email, username, password, first name, and last name.
- `/auth/login`: Allows users to log in by providing their email/username and password.
- `/auth/logout`: Logs out the authenticated user.
- `/auth/refresh-token`: Refreshes the JWT access token.

```javascript
// Example of signing up a new user in React
const signUpUser = async (userData) => {
  try {
    const response = await axios.post('/auth/signup', userData);
    return response.data;
  } catch (error) {
    console.error('Error signing up:', error);
    throw error;
  }
};
```

## Customers
InvoicePilot allows users to manage their customers, including creating and listing customers.

### Endpoints:
- `/api/create-customer/`: Creates a new customer.
- `/api/list-customers/`: Retrieves a list of customers.

```javascript
// Example of listing customers in React
const listCustomers = async () => {
  try {
    const response = await axios.get('/api/list-customers/');
    return response.data;
  } catch (error) {
    console.error('Error listing customers:', error);
    throw error;
  }
};
```

## Invoices
InvoicePilot allows users to manage their invoices, including creating, listing, adding items, generating PDFs, and sending emails.

### Endpoints:
- `/api/invoices/`: Retrieves a list of invoices or creates a new invoice.
- `/api/invoices/add-item/<invoice_id>/`: Adds an item to a specific invoice.
- `/api/invoices/create-invoice/`: Creates a new invoice.
- `/api/invoices/generate-pdf/<invoice_id>/`: Generates a PDF for a specific invoice.
- `/api/invoices/send-email/<invoice_id>/`: Sends an email with a PDF attachment for a specific invoice.

```javascript
// Example of creating a new invoice in React
const createInvoice = async (invoiceData) => {
  try {
    const response = await axios.post('/api/invoices/create-invoice/', invoiceData);
    return response.data;
  } catch (error) {
    console.error('Error creating invoice:', error);
    throw error;
  }
};
```

## User Profile
InvoicePilot allows users to manage their profiles.

### Endpoints:
- `/auth/create-profile/`: Creates a profile for the authenticated user.

```javascript
// Example of creating a user profile in React
const createProfile = async (profileData) => {
  try {
    const response = await axios.post('/auth/create-profile/', profileData);
    return response.data;
  } catch (error) {
    console.error('Error creating profile:', error);
    throw error;
  }
};
```

## Password Management
InvoicePilot allows users to request password resets and confirm password changes.

### Endpoints:
- `/auth/request-password-reset/`: Sends a password reset email to the user.
- `/auth/reset_password/<token>/`: Resets the user's password using the provided token.

```javascript
// Example of requesting a password reset in React
const requestPasswordReset = async (email) => {
  try {
    const response = await axios.post('/auth/request-password-reset/', { email });
    return response.data;
  } catch (error) {
    console.error('Error requesting password reset:', error);
    throw error;
  }
};
```

## User Management
InvoicePilot allows users to view, update, and delete their accounts.

### Endpoints:
- `/auth/user/me`: Retrieves the authenticated user's information.
- `/auth/user/me`: Updates the authenticated user's information.
- `/auth/user/me`: Deletes the authenticated user's account.

```javascript
// Example of retrieving user information in React
const getUserInfo = async () => {
  try {
    const response = await axios.get('/auth/user/me');
    return response.data;
  } catch (error) {
    console.error('Error getting user info:', error);
    throw error;
  }
};

// Example of updating user information in React
const updateUserInfo = async (userData) => {
  try {
    const response = await axios.put('/auth/user/me', userData);
    return response.data;
  } catch (error) {
    console.error('Error updating user info:', error);
    throw error;
  }
};

// Example of deleting user account in React
const deleteUserAccount = async () => {
  try {
    const response = await axios.delete('/auth/user/me');
    return response.data;
  } catch (error) {
    console.error('Error deleting user account:', error);
    throw error;
  }
};
```

## Swagger Documentation
InvoicePilot API documentation is also available through Swagger.

### Endpoint:
- `/swagger/`: Accesses the Swagger UI for exploring the API endpoints.

## Conclusion
This documentation provides an overview of all the endpoints available in the InvoicePilot API. Developers can use these endpoints to integrate invoice management, customer management, authentication, password management, and user profile functionalities into their applications.
