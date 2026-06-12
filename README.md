# Inmobiliaria

Rental Property Showcase Module built with Django MVT.

## Requirements

- Python 3.12+
- PostgreSQL

## Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate       # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your PostgreSQL credentials

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Usage

- Home page (`/`): Lists all available rental properties
- Property Detail (`/properties/<uuid>/`): Shows full property details
- Admin Panel (`/admin/`): Manage properties (admin user required)

## Testing

```bash
pytest
```

## Tech Stack

- Python 3.12+
- Django 6.0+
- PostgreSQL
- TailwindCSS (CDN)
- Pytest
