#!/usr/bin/env python3
"""
Simple runner script for Framer automation.
This script automatically loads settings from .env file.
"""

import sys
import os
from pathlib import Path
from config import Config

def main():
    # Load environment
    Config.load_environment()
    
    # Check if .env file exists
    if not Path('.env').exists():
        print("No .env file found!")
        print("Creating .env.example file...")
        
        example_content = """# Framer Project Configuration
FRAMER_PROJECT_URL=https://framer.com/projects/your-project-id

# Optional: Override default settings
# HEADLESS_MODE=false
# VERBOSE_LOGGING=false
"""
        with open('.env.example', 'w') as f:
            f.write(example_content)
        
        print("Please:")
        print("1. Copy .env.example to .env")
        print("2. Edit .env and set your FRAMER_PROJECT_URL")
        print("3. Run this script again")
        return False
    
    # Check if project URL is set
    project_url = Config.get_project_url()
    if not project_url:
        print("ERROR: FRAMER_PROJECT_URL not set in .env file!")
        return False
    
    # Check if auth data exists
    if not Config.AUTH_DATA_FILE.exists():
        print("No authentication data found.")
        print("Running setup first...")
        os.system("python setup_session.py")
        return True
    
    # Run publishing
    print("Starting automated publishing...")
    result = os.system("python publish.py")
    return result == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
