"""Signup handler. Pure functions so it can be tested without a server."""

USERS: dict[str, dict] = {}


def signup(payload: dict) -> tuple[int, dict]:
    """Create a user. Returns (status code, body)."""
    email = payload.get("email")
    password = payload.get("password")
    if not email or not password:
        return 400, {"error": "email and password are required"}
    if email in USERS:
        return 409, {"error": "email already registered"}
    USERS[email] = {"email": email, "password": password}
    return 201, {"email": email}
