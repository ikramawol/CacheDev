# backend/tests/test_routes.py
import unittest
from app import create_app, db
from flask_jwt_extended import create_access_token
from backend.models import User

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()
        self.create_user()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def create_user(self):
        self.user = User(email='test@example.com', name='Test User')
        self.user.set_password('testpassword')
        db.session.add(self.user)
        db.session.commit()
        self.access_token = create_access_token(identity=self.user.id)

    def test_register(self):
        response = self.client.post('/api/register', json={
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'name': 'New User'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('/api/login', json={
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)

    def test_create_conversation(self):
        response = self.client.post('/api/conversations', json={
            'message': 'This is a test message'
        }, headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 201)

    def test_get_conversation(self):
        # First create a conversation
        conversation_response = self.client.post('/api/conversations', json={
            'message': 'This is a test message'
        }, headers={'Authorization': f'Bearer {self.access_token}'})
        conversation_id = conversation_response.json['conversation_id']

        # Now retrieve the conversation
        response = self.client.get(f'/api/conversations/{conversation_id}', headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 200)

    def test_add_message(self):
        # First create a conversation
        conversation_response = self.client.post('/api/conversations', json={
            'message': 'Initial message'
        }, headers={'Authorization': f'Bearer {self.access_token}'})
        conversation_id = conversation_response.json['conversation_id']

        # Now add a new message
        response = self.client.post(f'/api/conversations/{conversation_id}/messages', json={
            'message': 'New message'
        }, headers={'Authorization': f'Bearer {self.access_token}'})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
