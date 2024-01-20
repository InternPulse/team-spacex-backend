# InvoicePilot Project

Welcome to the InvoicePilot project! This Django-based web application helps manage and track invoices efficiently.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- Django 5.0.1
- Other dependencies (see requirements.txt)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/InternPulse/team-spacex-backend.git
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Access the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage your application.
   
2. Explore the Invoice API at [http://127.0.0.1:8000/api/invoices/](http://127.0.0.1:8000/api/invoices/).

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch and make your changes.
3. Submit a pull request to the `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.