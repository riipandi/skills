USERS = {1: {"id": 1, "email": "ayu@example.com"}}


def get_user(user_id):
    return USERS.get(user_id)


def get_user_by_email(email):
    return next((u for u in USERS.values() if u["email"] == email), None)
