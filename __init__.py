# api/__init__.py

# Version of the package
__version__ = "0.1.0"

# Import models and CRUD functions for easy access
from .models import ItemSchema, UpdateItemSchema, ClockInSchema, UpdateClockInSchema
from .crud import (
    add_item,
    retrieve_item,
    filter_items,
    update_item,
    delete_item,
    add_clockin,
    retrieve_clockin,
    filter_clockins,
    update_clockin,
    delete_clockin,
)

# Optionally, you can define some package-level variables
PACKAGE_NAME = "My FastAPI Application"
