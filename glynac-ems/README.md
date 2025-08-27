# Employee Management System (EMS) — Django REST API

This is the **full** Employee Management System built with Django & DRF for the Glynac AI internship task.

## Features
- Django 4.2 LTS + DRF
- JWT auth (SimpleJWT)
- Swagger UI & ReDoc
- Models: Department, Employee, Attendance, Performance
- Filtering, search, ordering, pagination
- Faker seed command
- Optional Chart.js page at `/charts/`
- Docker + docker-compose
- `.env.example`

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_data --count 50   # optional
python manage.py runserver
```
Docs: http://127.0.0.1:8000/swagger/

## Docker
```bash
docker compose up --build
```
