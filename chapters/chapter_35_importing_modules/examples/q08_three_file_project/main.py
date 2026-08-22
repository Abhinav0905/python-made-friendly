"""Import helpers and models from neighboring files."""

import helpers
from models import User


user = User("Ada", "Lovelace", "ada@example.com")
print(helpers.format_name(user.first, user.last))
print(user)
