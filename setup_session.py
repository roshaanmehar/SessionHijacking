#!/usr/bin/env python3
"""
Setup script to perform initial login and save session data.
Run this once to set up authentication for automated publishing.
"""

import logging
import sys
from pathlib import Path
from config import Config
from framer_publisher import FramerPublisher

def setup_logging():
    """Configure logging with proper encoding"""
    Config.ensure_directories()
    
    # File handler
    file_handler = logging.FileHandler(Config.LOGS_DIR / 'setup.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Load environment variables
    Config.load_environment()
    
    print("Framer Authentication Setup")
    print("=" * 50)
    
    # Get project URL from environment or user input
    project_url = Config.get_project_url()
    if not project_url:
        project_url = input("Enter your Framer project URL: ").strip()
        if not project_url:
            print("ERROR: Project URL is required")
            return False
    else:
        print(f"Using project URL from .env: {project_url}")
    
    if not project_url.startswith('https://framer.com'):
        print("ERROR: Please enter a valid Framer project URL")
        return False
    
    try:
        with FramerPublisher(project_url, headless=False) as publisher:
            success = publisher.login_and_save_session()
            
            if success:
                print("\nSetup completed successfully!")
                print("You can now run 'python publish.py' to automate publishing.")
                return True
            else:
                print("\nSetup failed. Please try again.")
                return False
                
    except KeyboardInterrupt:
        print("\nSetup cancelled by user")
        return False
    except Exception as e:
        logger.error(f"Setup failed: {e}")
        print(f"\nSetup failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
