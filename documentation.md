````markdown
# InvoicePilot API Documentation

## Introduction
InvoicePilot is an API designed to manage invoices, customers, and user authentication. This document outlines all the available endpoints in the InvoicePilot API along with their functionalities.

## Authentication
InvoicePilot API uses JSON Web Tokens (JWT) for authentication. Users can sign up, log in, log out, and refresh their tokens using the provided endpoints.

### Endpoints:
- `/auth/signup`: Allows users to sign up by providing their email, username, password, first name, and last name.
  ```javascript
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
- `/auth/login`: Allows users to log in by providing their email/username and password.
  ```javascript
  const logInUser = async (userData) => {
    try {
      const response = await axios.post('/auth/login', userData);
      return response.data;
    } catch (error) {
      console.error('Error logging in:', error);
      throw error;
    }
  };
  ```
- `/auth/logout`: Logs out the authenticated user.
  ```javascript
  const logOutUser = async () => {
    try {
      const response = await axios.post('/auth/logout');
      return response.data;
    } catch (error) {
      console.error('Error logging out:', error);
      throw error;
    }
  };
  ```
- `/auth/refresh-token`: Refreshes the JWT access token.
  ```javascript
  const refreshToken = async () => {
    try {
      const response = await axios.post('/auth/refresh-token');
      return response.data;
    } catch (error) {
      console.error('Error refreshing token:', error);
      throw error;
    }
  };
  ```

## Customers
InvoicePilot allows users to manage their customers, including creating and listing customers.

### Endpoints:
- `/api/create-customer/`: Creates a new customer.
  ```javascript
  const createCustomer = async (customerData) => {
    try {
      const response = await axios.post('/api/create-customer/', customerData);
      return response.data;
    } catch (error) {
      console.error('Error creating customer:', error);
      throw error;
    }
  };
  ```
- `/api/list-customers/`: Retrieves a list of customers.
  ```javascript
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
  ```javascript
  const getInvoices = async () => {
    try {
      const response = await axios.get('/api/invoices/');
      return response.data;
    } catch (error) {
      console.error('Error retrieving invoices:', error);
      throw error;
    }
  };

  const createInvoice = async (invoiceData) => {
    try {
      const response = await axios.post('/api/invoices/', invoiceData);
      return response.data;
    } catch (error) {
      console.error('Error creating invoice:', error);
      throw error;
    }
  };
  ```
- `/api/invoices/add-item/<invoice_id>/`: Adds an item to a specific invoice.
  ```javascript
  const addItemToInvoice = async (invoiceId, itemData) => {
    try {
      const response = await axios.post(`/api/invoices/add-item/${invoiceId}/`, itemData);
      return response.data;
    } catch (error) {
      console.error('Error adding item to invoice:', error);
      throw error;
    }
  };
  ```
- `/api/invoices/generate-pdf/<invoice_id>/`: Generates a PDF for a specific invoice.
  ```javascript
  const generatePDF = async (invoiceId) => {
    try {
      const response = await axios.get(`/api/invoices/generate-pdf/${invoiceId}/`, { responseType: 'blob' });
      return response.data;
    } catch (error) {
      console.error('Error generating PDF:', error);
      throw error;
    }
  };
  ```
- `/api/invoices/send-email/<invoice_id>/`: Sends an email with a PDF attachment for a specific invoice.
  ```javascript
  const sendEmailWithPDF = async (invoiceId, emailData) => {
    try {
      const response = await axios.post(`/api/invoices/send-email/${invoiceId}/`, emailData);
      return response.data;
    } catch (error) {
      console.error('Error sending email with PDF:', error);
      throw error;
    }
  };
  ```

## User Profile
InvoicePilot allows users to manage their profiles.

### Endpoints:
- `/auth/create-profile/`: Creates a profile for the authenticated user.

## Password Management
InvoicePilot allows users to request password resets and confirm password changes.

### Endpoints:
- `/auth/request-password-reset/`: Sends a password reset email to the user.
  ```javascript
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
- `/auth/reset_password/<token>/`: Resets the user's password using the provided token.

## User Management
InvoicePilot allows users to view, update, and delete their accounts.

### Endpoints:
- `/auth/user/me`: Retrieves the authenticated user's information.
- `/auth/user/me`: Updates the authenticated user's information.
- `/auth/user/me`: Deletes the authenticated user's account.

## Swagger Documentation
InvoicePilot API documentation is also available through Swagger.

### Endpoint:
- `/swagger/`: Accesses the Swagger UI for exploring the API endpoints.

## Conclusion
This documentation provides an overview of all the endpoints available in the InvoicePilot API. Developers can use these endpoints to integrate invoice management, customer management, authentication, password management, and user profile functionalities into their applications.
````markdown
