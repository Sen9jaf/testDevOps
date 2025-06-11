import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app.program import app  # імпорт Flask app із program.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_data(as_text=True)
    assert ('✅ DB Connected' in data) or ('❌ Error' in data)

