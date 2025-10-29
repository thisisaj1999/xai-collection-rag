cd app

uv sync

source .venv/bin/activate

uvicorn main:app --reload