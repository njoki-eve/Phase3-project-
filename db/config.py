"""
contains database configuration
"""

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/health_simplified_db")