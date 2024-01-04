"""A client for interacting with the JSONPlaceholder API."""

import requests
from typing import Dict, Any, Optional


class JSONPlaceholderClient:
    """
    Client for interacting with the JSONPlaceholder API.

    Attributes:
        base_url (str): The base URL of the JSONPlaceholder API.
    """

    base_url: str = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_user(user_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve user data from the API based on the given user ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing user information if successful,
                                       otherwise None.
        """
        response = requests.get(
            f"{JSONPlaceholderClient.base_url}/users/{user_id}")
        return response.json() if response.ok else None

    @staticmethod
    def verify_email(email: str) -> Optional[Dict[str, Any]]:
        """
        Validate an email address using the API.

        Args:
            email (str): Email address to validate.

        Returns:
            Dict[str, Any]: Verification result in a dictionary format.
        """
        endpoint = f"{JSONPlaceholderClient.base_url}/verify_email"
        data_payload = {"email": email}
        response = requests.post(endpoint, json=data_payload)
        return response.json() if response.ok else None

    @staticmethod
    def create_post(user_id: int, title: str, body: str) -> Optional[Dict[str, Any]]:
        """
        Create a post using the provided data.

        Args:
            user_id (int): ID of the user.
            title (str): Title of the post.
            body (str): Content of the post.

        Returns:
            Dict[str, Any]: Response data from the API.
        """
        payload = {
            "userId": user_id,
            "title": title,
            "body": body
        }
        response = requests.post(
            f"{JSONPlaceholderClient.base_url}/posts", json=payload)
        return response.json() if response.ok else None
