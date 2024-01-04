"""A service for verify email with the JSONPlaceholder API(conditionally)."""
from typing import Dict, List, Any

from json_plaseholder.main import JSONPlaceholderClient


class EmailVerificationService:
    """
    Service for checking and storing e-mail verification results.

    Attributes:
        results (List[Dict[str, Any]]): List of verification results.
    """
    results: List[Dict[str, Any]] = []

    @staticmethod
    def verify_and_store(email: str) -> None:
        """
        Verifies e-mail and saves results in results.

        Args:
            email (str): Email address to verify.

        Returns:
            None
        """
        verification_result = JSONPlaceholderClient.verify_email(email)
        if verification_result:
            EmailVerificationService.results.append({"email": email, "result": verification_result})

    @staticmethod
    def get_results() -> List[Dict[str, Any]]:
        """
        Returns a list of email verification results.

        Returns:
            List[Dict[str, Any]]: List of verification results.
        """
        return EmailVerificationService.results
