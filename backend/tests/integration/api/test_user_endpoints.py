import pytest
import requests
from app import app  # Assuming your Flask app is named 'app'

# Fixture for test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test user registration
def test_user_registration(client):
    response = client.post('/register', json={'username': 'testuser', 'password': 'password123'})
    assert response.status_code == 201
    assert 'testuser' in response.json['message']

# Test user login
def test_user_login(client):
    # Register user first (or use a pre-registered user)
    client.post('/register', json={'username': 'testuser', 'password': 'password123'})
    response = client.post('/login', json={'username': 'testuser', 'password': 'password123'})
    assert response.status_code == 200
    assert 'token' in response.json

# Test protected endpoint (requires authentication)
def test_protected_endpoint(client):
    # Get token first
    token = client.post('/login', json={'username': 'testuser', 'password': 'password123'}).json['token']
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get('/protected', headers=headers)
    assert response.status_code == 200

# Test database interaction (example using SQLAlchemy)
# Assuming you have a User model
def test_database_interaction(client, db_session): # db_session is a fixture for database session
    user = User(username='dbtestuser', password='dbpassword')
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(User).filter_by(username='dbtestuser').first()
    assert retrieved_user is not None
    assert retrieved_user.username == 'dbtestuser'

# Test file upload (requires file handling logic in your API)
def test_file_upload(client):
    with open('testfile.txt', 'rb') as f:
        response = client.post('/upload', data={'file': (f, 'testfile.txt')})
    assert response.status_code == 200
    # Assert file upload success (check database or file storage)

# Test cross-service communication (example using requests)
def test_cross_service_communication(client):
    response = client.post('/external_service') # Assumes an endpoint that interacts with external service
    assert response.status_code == 200
    # Assert successful communication with external service
