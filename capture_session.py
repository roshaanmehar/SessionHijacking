#!/usr/bin/env python3
"""
Session capture script - captures login sessions from any website
"""

import logging
import sys
import argparse
from config import Config
from universal_automation import UniversalSessionAutomation

def setup_logging(verbose: bool = False):
    """Configure logging with proper encoding"""
    Config.ensure_directories()
    
    level = logging.DEBUG if verbose else logging.INFO
    
    # File handler
    file_handler = logging.FileHandler(Config.LOGS_DIR / 'capture.log', encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

def main():
    parser = argparse.ArgumentParser(description='Capture login session from any website')
    parser.add_argument('--session-name', default='default', help='Name for the captured session')
    parser.add_argument('--start-url', help='Starting URL (default: Google)')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    print("Universal Session Capture")
    print("=" * 40)
    print(f"Session name: {args.session_name}")
    print(f"Start URL: {args.start_url or 'Default (Google)'}")
    print("=" * 40)
    
    try:
        with UniversalSessionAutomation(headless=False) as automation:
            success = automation.capture_session(args.session_name, args.start_url)
            
            if success:
                print("\nSession capture completed successfully!")
                return True
            else:
                print("\nSession capture failed. Check logs for details.")
                return False
                
    except KeyboardInterrupt:
        print("\nSession capture cancelled by user")
        return False
    except Exception as e:
        logger.error(f"Session capture failed: {e}")
        print(f"\nSession capture failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
