# Import each blueprint so they get registered
from .items import items_bp
from .users import users_bp

# Optionally expose them as a list for auto-registration
__all__ = [
    "items_bp",
    "users_bp",
]