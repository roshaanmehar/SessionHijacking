import logging
import time
from pathlib import Path
from typing import List
from browser_manager import UniversalBrowserManager
from session_manager import UniversalSessionManager
from config import Config

class UniversalSessionAutomation:
    def __init__(self, headless: bool = False):
        self.browser_manager = UniversalBrowserManager(headless=headless)
        self.driver = None
        self.session_manager = None
        self.logger = logging.getLogger(__name__)
        
    def __enter__(self):
        self.driver = self.browser_manager.create_driver()
        self.session_manager = UniversalSessionManager(self.driver)
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser_manager.quit()
    
    def capture_session(self, session_name: str = "default", start_url: str = None) -> bool:
        """Capture a new session"""
        try:
            self.logger.info(f"Starting session capture: {session_name}")
            
            # Start monitoring
            if not self.session_manager.start_monitoring(start_url):
                self.logger.error("Failed to start session monitoring")
                return False
            
            # Save session
            session_file = self.session_manager.save_session(session_name)
            
            print(f"\nSession '{session_name}' captured successfully!")
            print(f"Session file: {session_file}")
            print(f"Summary file: {session_file.replace('_session.json', '_summary.txt')}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error capturing session: {e}")
            return False
    
    def replay_session(self, session_name: str = "default", target_url: str = None) -> bool:
        """Replay a saved session"""
        try:
            self.logger.info(f"Starting session replay: {session_name}")
            
            # Load session data
            session_data = self.session_manager.load_session(session_name)
            if not session_data:
                self.logger.error(f"Could not load session: {session_name}")
                return False
            
            print(f"\nReplaying session '{session_name}'...")
            print(f"Original session from: {session_data['timestamp']}")
            print(f"Domains to restore: {len(session_data['domains'])}")
            
            # Restore session
            if not self.session_manager.restore_session(session_data, target_url):
                self.logger.error("Failed to restore session")
                return False
            
            print(f"\nSession '{session_name}' restored successfully!")
            print("You can now interact with the browser or run additional automation.")
            
            # Keep browser open for interaction
            print("\nBrowser will remain open. Press ENTER to close...")
            input()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error replaying session: {e}")
            return False
    
    def list_available_sessions(self) -> List[str]:
        """List all available sessions"""
        return self.session_manager.list_sessions()
    
    def interactive_mode(self):
        """Interactive mode for session management"""
        try:
            while True:
                print("\n" + "="*60)
                print("UNIVERSAL SESSION AUTOMATION")
                print("="*60)
                print("1. Capture new session")
                print("2. Replay existing session")
                print("3. List available sessions")
                print("4. Exit")
                print("="*60)
                
                choice = input("Select option (1-4): ").strip()
                
                if choice == "1":
                    session_name = input("Enter session name (default: 'default'): ").strip() or "default"
                    start_url = input("Enter starting URL (optional): ").strip() or None
                    self.capture_session(session_name, start_url)
                
                elif choice == "2":
                    sessions = self.list_available_sessions()
                    if not sessions:
                        print("No sessions available. Capture a session first.")
                        continue
                    
                    print("\nAvailable sessions:")
                    for i, session in enumerate(sessions, 1):
                        print(f"{i}. {session}")
                    
                    try:
                        session_idx = int(input("Select session number: ")) - 1
                        if 0 <= session_idx < len(sessions):
                            session_name = sessions[session_idx]
                            target_url = input("Enter target URL (optional): ").strip() or None
                            self.replay_session(session_name, target_url)
                        else:
                            print("Invalid session number")
                    except ValueError:
                        print("Please enter a valid number")
                
                elif choice == "3":
                    sessions = self.list_available_sessions()
                    if sessions:
                        print("\nAvailable sessions:")
                        for session in sessions:
                            session_file = Config.SESSIONS_DIR / f"{session}_session.json"
                            summary_file = Config.SESSIONS_DIR / f"{session}_summary.txt"
                            print(f"- {session}")
                            if summary_file.exists():
                                print(f"  Summary: {summary_file}")
                    else:
                        print("No sessions available")
                
                elif choice == "4":
                    print("Goodbye!")
                    break
                
                else:
                    print("Invalid choice. Please select 1-4.")
                    
        except KeyboardInterrupt:
            print("\nExiting...")
        except Exception as e:
            self.logger.error(f"Error in interactive mode: {e}")
