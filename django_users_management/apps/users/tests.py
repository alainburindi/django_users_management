from django.test import TestCase

from django_users_management.apps.users.models import User


class UsersTest(TestCase):
    def test_get_users(self):
        User.objects.bulk_create([
            User(name="John Doe", email="john@test.com",
                 password="test", role="admin"),
            User(name="Jane Doe", email="jane@test.com",
                 password="test", role="user"),
        ])
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['name'], "John Doe")

    def test_create_user(self):
        response = self.client.post('/users', {
            'name': 'John Doe',
            'email': 'john@test.com',
            'password': 'test',
            'role': 'admin'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], "John Doe")

    def test_create_user_with_existing_email(self):
        user_data = {
            'name': 'John Doe',
            'email': 'john@test.com',
            'password': 'test',
            'role': 'admin'
        }
        User.objects.create(**user_data)
        response = self.client.post('/users', user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email'], [
                         "user with this email already exists."])

    def test_create_user_with_invalid_email(self):
        user_data = {
            'name': 'John Doe',
            'email': 'john',
            'password': 'test',
            'role': 'admin'
        }
        response = self.client.post('/users', user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email'], [
                         "Enter a valid email address."])

    def test_create_user_with_missing_role(self):
        user_data = {
            'name': 'John Doe',
            'email': 'john',
            'password': 'test',
        }
        response = self.client.post('/users', user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['role'], ['This field is required.'])

    def test_create_user_with_missing_name(self):
        user_data = {
            'email': 'john',
            'password': 'test',
            'role': 'admin'
        }
        response = self.client.post('/users', user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['name'], ['This field is required.'])

    def test_create_user_with_missing_email(self):
        user_data = {
            'name': 'John Doe',
            'password': 'test',
            'role': 'admin'
        }
        response = self.client.post('/users', user_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['email'], ['This field is required.'])

    def test_delete_user(self):
        user = User.objects.create(
            name="John Doe", email="test@test.com",
            password="test", role="admin")
        response = self.client.delete(f'/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "User deleted")

    def test_delete_unexisting_user(self):
        response = self.client.delete('/users/00021212')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "User not found")

    def test_user_model_str(self):
        user = User.objects.create(
            name="John Doe", email="al@test.com",
            password="test", role="admin")
        self.assertEqual(str(user), "al@test.com")

    # unit testing for the create_user_method
    def test_create_super_user_method(self):
        user_data = {
            'name': 'John Doe',
            'email': 'admin@test.com',
            'password': 'test',
        }
        user = User.objects.create_superuser(**user_data)
        self.assertEqual(user.role, "admin")
        self.assertEqual(user.is_admin, True)

    def test_create_user_method_with_already_used_email(self):
        user_data = {
            'name': 'John Doe',
            'email': 'al@test.com',
            'password': 'test',
        }
        User.objects.create_user(**user_data)
        # response = User.objects.create_user(**user_data)
        # self.assertRaises(ValueError)

        with self.assertRaisesRegex(ValueError,
                                    "User with given email already exists"):
            User.objects.create_user(**user_data)
