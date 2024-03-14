# fastapi_pytest_example


Example of FastAPI with pytests.

## Testing

1. Create a virtual env: `python3.8 -m venv .venv`
2. Activate it: `source .venv/bin/activate`
3. Install depenencies: `pip install -r requirements.txt -r requirements-dev.txt`
4. Run: `pytest tests/`

## Running

### Locally

1. Create a virtual env: `python3.8 -m venv .venv`
2. Activate it: `source .venv/bin/activate`
3. Install depenencies: `pip install -r requirements.txt -r requirements-dev.txt`
4. Run: `python app.py`
5. Check: http://127.0.0.1:8000/hello-world 

### Inside docker

1. Build the image locally: `docker build -t example:local --load .`
2. Run exposing the ports: `docker run -p 8000:8000 example:local`

