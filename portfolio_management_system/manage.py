import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Detect if running in conda environment
CONDA_PREFIX = os.environ.get('CONDA_PREFIX')
if CONDA_PREFIX:
    print(f"Running in conda environment: {os.path.basename(CONDA_PREFIX)}")

# Load environment variables
load_dotenv()

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Use environment variable for SECRET_KEY with fallback
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key-for-development')

# Use environment variable for DEBUG
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# Rest of your settings file...

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_management_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
