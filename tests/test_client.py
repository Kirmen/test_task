import unittest
from json_placeholder.main import JSONPlaceholderClient
from json_placeholder.email_ver_serv import EmailVerificationService


class TestJSONPlaceholderClient(unittest.TestCase):

    def test_get_user(self):
        user_data = JSONPlaceholderClient.get_user(1)
        self.assertIsNotNone(user_data)
        self.assertIsInstance(user_data, dict)

    def test_create_post(self):
        post_data = JSONPlaceholderClient.create_post(1, "Test Post", "It's a test post.")
        self.assertIsNotNone(post_data)
        self.assertIsInstance(post_data, dict)


class TestEmailVerificationService(unittest.TestCase):

    def test_verify_and_store(self):
        email_to_verify = "example@gmail.com"
        EmailVerificationService.verify_and_store(email_to_verify)
        results = EmailVerificationService.get_results()

        self.assertIsNotNone(results)
        self.assertIsInstance(results, list)
        # self.assertGreaterEqual(len(results), 1)
        # self.assertIsInstance(results[0], dict)
        # self.assertEqual(results[0]["email"], email_to_verify)


if __name__ == "__main__":
    unittest.main()
