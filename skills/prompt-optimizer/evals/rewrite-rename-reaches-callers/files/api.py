from users import get_user, get_user_by_email


def show(user_id):
    user = get_user(user_id)
    return user or {"error": "not found"}


def lookup(email):
    return get_user_by_email(email) or {"error": "not found"}
