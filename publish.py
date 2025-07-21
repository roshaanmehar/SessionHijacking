#!/usr/bin/env python3
"""
Main automation script for Framer publishing.
This script uses saved authentication data to automatically publish your Framer project.
"""

import logging
import sys
import argparse
import os
from config import Config
from framer_publisher import FramerPublisher

def setup_logging(verbose: bool = False):
    """Configure logging with proper encoding"""
    Config.ensure_directories()
    
    level = logging.DEBUG if verbose else logging.INFO
    
    # Create formatters
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # File handler
    file_handler = logging.FileHandler(Config.LOGS_DIR / 'publish.log', encoding='utf-8')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(level)
    
    # Console handler with safe encoding
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(level)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

def main():
    # Load environment variables
    Config.load_environment()
    
    parser = argparse.ArgumentParser(description='Automate Framer project publishing')
    parser.add_argument('--project-url', help='Framer project URL (overrides .env file)')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    # Get project URL from args or environment
    project_url = args.project_url or Config.get_project_url()
    if not project_url:
        print("ERROR: No project URL provided!")
        print("Either:")
        print("1. Set FRAMER_PROJECT_URL in your .env file, or")
        print("2. Use --project-url argument")
        return False
    
    # Get settings from args or environment
    headless = args.headless or Config.get_headless_mode()
    verbose = args.verbose or Config.get_verbose_logging()
    
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    
    print("Framer Auto Publisher")
    print("=" * 30)
    print(f"Project: {project_url}")
    print(f"Headless: {headless}")
    print("=" * 30)
    
    # Check if auth data exists
    if not Config.AUTH_DATA_FILE.exists():
        print("ERROR: No authentication data found!")
        print("Please run 'python setup_session.py' first to set up authentication.")
        return False
    
    try:
        with FramerPublisher(project_url, headless=headless) as publisher:
            success = publisher.run_full_automation()
            
            if success:
                print("\nPublishing completed successfully!")
                return True
            else:
                print("\nPublishing failed. Check logs for details.")
                print("You may need to run 'python setup_session.py' again if your session expired.")
                return False
                
    except KeyboardInterrupt:
        print("\nPublishing cancelled by user")
        return False
    except Exception as e:
        logger.error(f"Publishing failed: {e}")
        print(f"\nPublishing failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
