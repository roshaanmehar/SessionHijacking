#!/usr/bin/env python3
"""
Interactive session management interface
"""

import logging
import sys
from config import Config
from universal_automation import UniversalSessionAutomation

def setup_logging():
    """Configure logging"""
    Config.ensure_directories()
    
    # File handler only for interactive mode
    file_handler = logging.FileHandler(Config.LOGS_DIR / 'interactive.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)

def main():
    setup_logging()
    
    try:
        with UniversalSessionAutomation(headless=False) as automation:
            automation.interactive_mode()
            
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"\nError: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
