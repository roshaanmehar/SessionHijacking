import json
import time
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

class UniversalSessionManager:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.captured_domains = set()
        self.session_data = {
            "timestamp": None,
            "start_url": None,
            "final_url": None,
            "domains": {},
            "page_snapshots": []
        }
        
    def start_monitoring(self, start_url: str = None):
        """Start monitoring user session"""
        try:
            start_url = start_url or Config.get_default_start_url()
            self.session_data["start_url"] = start_url
            self.session_data["timestamp"] = datetime.now().isoformat()
            
            self.logger.info(f"Starting session monitoring from: {start_url}")
            self.driver.get(start_url)
            
            print("\n" + "="*80)
            print("UNIVERSAL SESSION CAPTURE STARTED")
            print("="*80)
            print("Instructions:")
            print("1. Navigate to any website and log in")
            print("2. Browse around, perform any actions you want to capture")
            print("3. When you're done, press ENTER in this terminal")
            print("4. The system will capture your complete session state")
            print("="*80)
            print(f"Starting URL: {start_url}")
            print("Monitoring session... (press ENTER when ready to capture)")
            
            # Wait for user to complete their session
            input()
            
            # Capture final session state
            self.capture_complete_session()
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error starting monitoring: {e}")
            return False
    
    def capture_complete_session(self):
        """Capture complete session state from all domains"""
        try:
            current_url = self.driver.current_url
            self.session_data["final_url"] = current_url
            
            print("\nCapturing session data...")
            
            # Get all domains from browser history (if possible)
            domains_to_capture = self._get_domains_from_current_session()
            
            # Capture data for each domain
            for domain in domains_to_capture:
                print(f"Capturing data for domain: {domain}")
                self._capture_domain_data(domain)
            
            # Capture current page snapshot
            self._capture_page_snapshot()
            
            self.logger.info(f"Captured session data for {len(domains_to_capture)} domains")
            
        except Exception as e:
            self.logger.error(f"Error capturing session: {e}")
            raise
    
    def _get_domains_from_current_session(self) -> Set[str]:
        """Get all domains from current browser session"""
        domains = set()
        
        try:
            # Add current domain
            current_domain = urlparse(self.driver.current_url).netloc
            if current_domain:
                domains.add(current_domain)
            
            # Try to get domains from cookies (they indicate visited sites)
            all_cookies = self.driver.get_cookies()
            for cookie in all_cookies:
                if 'domain' in cookie:
                    domain = cookie['domain'].lstrip('.')
                    domains.add(domain)
            
            # Add some common subdomains if main domain is present
            expanded_domains = set(domains)
            for domain in domains:
                if not domain.startswith('www.'):
                    expanded_domains.add(f"www.{domain}")
                if domain.startswith('www.'):
                    expanded_domains.add(domain[4:])
            
            return expanded_domains
            
        except Exception as e:
            self.logger.warning(f"Error getting domains: {e}")
            return {urlparse(self.driver.current_url).netloc}
    
    def _capture_domain_data(self, domain: str):
        """Capture all data for a specific domain"""
        try:
            # Navigate to domain to capture its data
            domain_url = f"https://{domain}"
            
            # Store current URL to return to later
            original_url = self.driver.current_url
            
            try:
                self.driver.get(domain_url)
                time.sleep(2)  # Wait for page load
            except Exception as e:
                self.logger.warning(f"Could not navigate to {domain}: {e}")
                return
            
            domain_data = {
                "cookies": [],
                "localStorage": {},
                "sessionStorage": {},
                "url": self.driver.current_url,
                "title": self.driver.title,
                "capture_time": datetime.now().isoformat()
            }
            
            # Capture cookies for this domain
            try:
                cookies = self.driver.get_cookies()
                domain_data["cookies"] = cookies
                self.logger.info(f"Captured {len(cookies)} cookies for {domain}")
            except Exception as e:
                self.logger.warning(f"Could not capture cookies for {domain}: {e}")
            
            # Capture localStorage
            try:
                local_storage = self.driver.execute_script(
                    "return Object.keys(localStorage).reduce((obj, key) => { obj[key] = localStorage.getItem(key); return obj; }, {});"
                )
                domain_data["localStorage"] = local_storage
                self.logger.info(f"Captured {len(local_storage)} localStorage items for {domain}")
            except Exception as e:
                self.logger.warning(f"Could not capture localStorage for {domain}: {e}")
            
            # Capture sessionStorage
            try:
                session_storage = self.driver.execute_script(
                    "return Object.keys(sessionStorage).reduce((obj, key) => { obj[key] = sessionStorage.getItem(key); return obj; }, {});"
                )
                domain_data["sessionStorage"] = session_storage
                self.logger.info(f"Captured {len(session_storage)} sessionStorage items for {domain}")
            except Exception as e:
                self.logger.warning(f"Could not capture sessionStorage for {domain}: {e}")
            
            # Store domain data
            self.session_data["domains"][domain] = domain_data
            
            # Return to original URL
            try:
                self.driver.get(original_url)
                time.sleep(1)
            except Exception as e:
                self.logger.warning(f"Could not return to original URL: {e}")
                
        except Exception as e:
            self.logger.error(f"Error capturing data for domain {domain}: {e}")
    
    def _capture_page_snapshot(self):
        """Capture current page state"""
        try:
            snapshot = {
                "url": self.driver.current_url,
                "title": self.driver.title,
                "timestamp": datetime.now().isoformat(),
                "page_source_length": len(self.driver.page_source),
                "window_size": self.driver.get_window_size(),
                "cookies_count": len(self.driver.get_cookies())
            }
            
            self.session_data["page_snapshots"].append(snapshot)
            self.logger.info(f"Captured page snapshot for: {snapshot['url']}")
            
        except Exception as e:
            self.logger.warning(f"Could not capture page snapshot: {e}")
    
    def save_session(self, session_name: str = "default") -> str:
        """Save captured session data to file"""
        try:
            session_file = Config.SESSIONS_DIR / f"{session_name}_session.json"
            
            with open(session_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_data, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Session saved to: {session_file}")
            
            # Also save a summary
            self._save_session_summary(session_name)
            
            return str(session_file)
            
        except Exception as e:
            self.logger.error(f"Error saving session: {e}")
            raise
    
    def _save_session_summary(self, session_name: str):
        """Save a human-readable summary of the session"""
        try:
            summary_file = Config.SESSIONS_DIR / f"{session_name}_summary.txt"
            
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(f"Session Summary: {session_name}\n")
                f.write("="*50 + "\n\n")
                f.write(f"Captured: {self.session_data['timestamp']}\n")
                f.write(f"Start URL: {self.session_data['start_url']}\n")
                f.write(f"Final URL: {self.session_data['final_url']}\n")
                f.write(f"Domains captured: {len(self.session_data['domains'])}\n\n")
                
                f.write("Domains:\n")
                for domain, data in self.session_data['domains'].items():
                    f.write(f"  - {domain}\n")
                    f.write(f"    Cookies: {len(data['cookies'])}\n")
                    f.write(f"    localStorage items: {len(data['localStorage'])}\n")
                    f.write(f"    sessionStorage items: {len(data['sessionStorage'])}\n")
                    f.write(f"    Final URL: {data['url']}\n\n")
            
            print(f"Session summary saved to: {summary_file}")
            
        except Exception as e:
            self.logger.warning(f"Could not save session summary: {e}")
    
    def load_session(self, session_name: str = "default") -> Optional[Dict[str, Any]]:
        """Load session data from file"""
        try:
            session_file = Config.SESSIONS_DIR / f"{session_name}_session.json"
            
            if not session_file.exists():
                self.logger.error(f"Session file not found: {session_file}")
                return None
            
            with open(session_file, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
            
            # Check if session is too old
            timestamp = datetime.fromisoformat(session_data["timestamp"])
            if datetime.now() - timestamp > timedelta(hours=Config.SESSION_TIMEOUT_HOURS):
                self.logger.warning(f"Session {session_name} is old, may be expired")
            
            self.logger.info(f"Loaded session: {session_name}")
            return session_data
            
        except Exception as e:
            self.logger.error(f"Error loading session {session_name}: {e}")
            return None
    
    def restore_session(self, session_data: Dict[str, Any], target_url: str = None) -> bool:
        """Restore complete session state"""
        try:
            print(f"Restoring session with {len(session_data['domains'])} domains...")
            
            # Determine target URL
            if not target_url:
                target_url = session_data.get('final_url') or session_data.get('start_url')
            
            target_domain = urlparse(target_url).netloc
            
            # First, restore the target domain's session
            if target_domain in session_data['domains']:
                print(f"Restoring primary domain: {target_domain}")
                self._restore_domain_session(target_domain, session_data['domains'][target_domain])
            
            # Then restore other domains
            for domain, domain_data in session_data['domains'].items():
                if domain != target_domain:
                    print(f"Restoring domain: {domain}")
                    self._restore_domain_session(domain, domain_data)
            
            # Finally navigate to target URL
            print(f"Navigating to target URL: {target_url}")
            self.driver.get(target_url)
            time.sleep(3)
            
            self.logger.info("Session restoration completed")
            return True
            
        except Exception as e:
            self.logger.error(f"Error restoring session: {e}")
            return False
    
    def _restore_domain_session(self, domain: str, domain_data: Dict[str, Any]):
        """Restore session for a specific domain"""
        try:
            # Navigate to domain
            domain_url = f"https://{domain}"
            self.driver.get(domain_url)
            time.sleep(2)
            
            # Clear existing data
            self.driver.delete_all_cookies()
            self.driver.execute_script("localStorage.clear();")
            self.driver.execute_script("sessionStorage.clear();")
            
            # Restore cookies
            for cookie in domain_data.get("cookies", []):
                try:
                    # Clean cookie data
                    clean_cookie = {k: v for k, v in cookie.items() 
                                  if k not in ['sameSite', 'storeId']}
                    self.driver.add_cookie(clean_cookie)
                except Exception as e:
                    self.logger.warning(f"Could not restore cookie {cookie.get('name', 'unknown')}: {e}")
            
            # Restore localStorage
            for key, value in domain_data.get("localStorage", {}).items():
                try:
                    # Escape quotes in the value
                    escaped_value = str(value).replace("'", "\\'").replace('"', '\\"')
                    self.driver.execute_script(f"localStorage.setItem('{key}', '{escaped_value}');")
                except Exception as e:
                    self.logger.warning(f"Could not restore localStorage item {key}: {e}")
            
            # Restore sessionStorage
            for key, value in domain_data.get("sessionStorage", {}).items():
                try:
                    escaped_value = str(value).replace("'", "\\'").replace('"', '\\"')
                    self.driver.execute_script(f"sessionStorage.setItem('{key}', '{escaped_value}');")
                except Exception as e:
                    self.logger.warning(f"Could not restore sessionStorage item {key}: {e}")
            
            # Refresh to apply changes
            self.driver.refresh()
            time.sleep(2)
            
            self.logger.info(f"Restored session for domain: {domain}")
            
        except Exception as e:
            self.logger.error(f"Error restoring session for domain {domain}: {e}")
    
    def list_sessions(self) -> List[str]:
        """List all available sessions"""
        try:
            sessions = []
            for file in Config.SESSIONS_DIR.glob("*_session.json"):
                session_name = file.stem.replace("_session", "")
                sessions.append(session_name)
            return sorted(sessions)
        except Exception as e:
            self.logger.error(f"Error listing sessions: {e}")
            return []
