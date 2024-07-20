# backend/tests/test_models.py
import unittest
from backend.models import User
from app import db

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
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

    def test_password_hashing(self):
        user = User.query.first()
        self.assertTrue(user.check_password('testpassword'))

    def test_user_creation(self):
        user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(user)

if __name__ == '__main__':
    unittest.main()
