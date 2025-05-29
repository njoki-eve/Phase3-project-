
"""
contains database configuration
"""

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://njoki-eve:2025@localhost:5432/health_simplified_db")