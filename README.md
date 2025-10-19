# QuickBiteQR

QuickBiteQR - Django MVP for QR-based restaurant ordering.

Quickstart (local):

1. Create a venv and install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Create `.env` with DATABASE_URL or use sqlite default.
3. Run migrations and seed:

```bash
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Production via Docker: see `docker/` files.

Bumping version: update `VERSION` and `pyproject.toml` and create a tag.
# QuickBiteQR
Scan-to-order platform that lets guests scan a table QR, browse the menu, and place orders while staff manage tables and orders from a simple Django admin dashboard.
