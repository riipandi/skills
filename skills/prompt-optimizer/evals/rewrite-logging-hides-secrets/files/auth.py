SESSIONS = {}
PASSWORDS = {"ayu@example.com": "s3cret-Pa55"}


def login(email, password):
    if PASSWORDS.get(email) != password:
        return None
    token = f"tok-{len(SESSIONS) + 1}"
    SESSIONS[token] = email
    return token


def logout(token):
    return SESSIONS.pop(token, None) is not None


def reset_password(email, new_password):
    if email not in PASSWORDS:
        return False
    PASSWORDS[email] = new_password
    return True
