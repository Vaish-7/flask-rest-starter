# Flask REST Starter

Minimal Flask REST API with JWT demo, SQLAlchemy, Docker, tests, and CI.

## Quick start
1. Copy `.env.example` to `.env` and update values.
2. Create venv and install: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
3. Run: `python -m app.main`
4. Open: `http://127.0.0.1:8000/`

## Docker
Build: `docker build -t flask-rest-starter .`  
Run: `docker run -p 8000:8000 flask-rest-starter`

## Tests
`pytest -q`

## Notes
- This starter uses a demo auth and simple DB setup. Replace demo auth with real user management and add migrations (Alembic) for production.
- Do not commit secrets. Use GitHub Secrets for CI.
