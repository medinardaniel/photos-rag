# app.py
from app import create_app

backend = create_app()

if __name__ == '__main__':
    backend.run(host='localhost', port=5000, debug=True)