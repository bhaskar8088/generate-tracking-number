# Tracking Number Generator API

This project implements a RESTful API using Django REST Framework to generate unique tracking numbers for parcels. The API ensures the generated tracking numbers follow a specified format, are unique, and can handle high concurrency and scalability.

## Features

- Generates unique tracking numbers that match the regex pattern `^[A-Z0-9]{1,16}$`
- Ensures no duplicate tracking numbers are generated (up to 10 attempts)
- Validates input fields using Django Rest Framework serializers
- API optimized for scalability and high concurrency

## Requirements

- Python 3.x
- Django 3.x or later
- Django REST Framework 3.x or later

## Setup

### 1. Clone the repository:

```bash
git clone git@github.com:bhaskar8088/generate-tracking-number.git

# Create a new virtual environment

python -m venv venv
source venv/bin/activate

cd generate_tn_django

### Virtualenv


# Install requirements

pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver

