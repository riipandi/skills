from api import lookup, show
from users import get_user

assert get_user(1)["email"] == "ayu@example.com"
assert show(2) == {"error": "not found"}
assert lookup("ayu@example.com")["id"] == 1
print("ok")
