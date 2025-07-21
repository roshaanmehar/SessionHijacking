#!/usr/bin/env python3
"""
Session replay script - replays captured sessions
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
    file_handler = logging.FileHandler(Config.LOGS_DIR / 'replay.log', encoding='utf-8')
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
    parser = argparse.ArgumentParser(description='Replay captured session')
    parser.add_argument('--session-name', default='default', help='Name of session to replay')
    parser.add_argument('--target-url', help='Target URL to navigate to after session restore')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    
    args = parser.parse_args()
    
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    print("Universal Session Replay")
    print("=" * 40)
    print(f"Session name: {args.session_name}")
    print(f"Target URL: {args.target_url or 'Original session URL'}")
    print(f"Headless: {args.headless}")
    print("=" * 40)
    
    try:
        with UniversalSessionAutomation(headless=args.headless) as automation:
            success = automation.replay_session(args.session_name, args.target_url)
            
            if success:
                print("\nSession replay completed successfully!")
                return True
            else:
                print("\nSession replay failed. Check logs for details.")
                return False
                
    except KeyboardInterrupt:
        print("\nSession replay cancelled by user")
        return False
    except Exception as e:
        logger.error(f"Session replay failed: {e}")
        print(f"\nSession replay failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
