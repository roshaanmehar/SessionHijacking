#!/usr/bin/env python3
"""
Test script to verify the universal session system works
"""

import sys
from pathlib import Path
from config import Config

def test_imports():
    """Test that all imports work correctly"""
    try:
        print("Testing imports...")
        
        from config import Config
        print("✓ Config imported")
        
        from browser_manager import UniversalBrowserManager
        print("✓ BrowserManager imported")
        
        from session_manager import UniversalSessionManager
        print("✓ SessionManager imported")
        
        from universal_automation import UniversalSessionAutomation
        print("✓ UniversalSessionAutomation imported")
        
        print("\n✅ All imports successful!")
        return True
        
    except Exception as e:
        print(f"\n❌ Import error: {e}")
        return False

def test_directories():
    """Test directory creation"""
    try:
        print("\nTesting directory creation...")
        Config.ensure_directories()
        
        if Config.SESSIONS_DIR.exists():
            print("✓ Sessions directory created")
        else:
            print("❌ Sessions directory not created")
            return False
            
        if Config.LOGS_DIR.exists():
            print("✓ Logs directory created")
        else:
            print("❌ Logs directory not created")
            return False
            
        print("\n✅ Directory creation successful!")
        return True
        
    except Exception as e:
        print(f"\n❌ Directory creation error: {e}")
        return False

def main():
    print("🧪 Universal Session System Test")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        return False
    
    # Test directories
    if not test_directories():
        return False
    
    print("\n🎉 All tests passed!")
    print("\nYou can now use:")
    print("- python capture_session.py --session-name 'test'")
    print("- python replay_session.py --session-name 'test'")
    print("- python interactive.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
