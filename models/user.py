#!/usr/bin/pytho3
"""The module contains `user class`.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
