import json
import time
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

class AuthManager:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        
    def extract_auth_data(self) -> Dict[str, Any]:
        """Extract all authentication data from current browser session"""
        try:
            auth_data = {
                "timestamp": datetime.now().isoformat(),
                "cookies": [],
                "localStorage": {},
                "sessionStorage": {},
                "current_url": self.driver.current_url
            }
            
            # Extract cookies
            cookies = self.driver.get_cookies()
            auth_data["cookies"] = cookies
            self.logger.info(f"Extracted {len(cookies)} cookies")
            
            # Extract localStorage
            try:
                local_storage = self.driver.execute_script(
                    "return Object.keys(localStorage).reduce((obj, key) => { obj[key] = localStorage.getItem(key); return obj; }, {});"
                )
                auth_data["localStorage"] = local_storage
                self.logger.info(f"Extracted {len(local_storage)} localStorage items")
            except Exception as e:
                self.logger.warning(f"Could not extract localStorage: {e}")
            
            # Extract sessionStorage
            try:
                session_storage = self.driver.execute_script(
                    "return Object.keys(sessionStorage).reduce((obj, key) => { obj[key] = sessionStorage.getItem(key); return obj; }, {});"
                )
                auth_data["sessionStorage"] = session_storage
                self.logger.info(f"Extracted {len(session_storage)} sessionStorage items")
            except Exception as e:
                self.logger.warning(f"Could not extract sessionStorage: {e}")
            
            return auth_data
            
        except Exception as e:
            self.logger.error(f"Error extracting auth data: {e}")
            raise
    
    def save_auth_data(self, auth_data: Dict[str, Any]) -> None:
        """Save authentication data to file"""
        try:
            with open(Config.AUTH_DATA_FILE, 'w') as f:
                json.dump(auth_data, f, indent=2)
            self.logger.info(f"Auth data saved to {Config.AUTH_DATA_FILE}")
        except Exception as e:
            self.logger.error(f"Error saving auth data: {e}")
            raise
    
    def load_auth_data(self) -> Optional[Dict[str, Any]]:
        """Load authentication data from file"""
        try:
            if not Config.AUTH_DATA_FILE.exists():
                self.logger.warning("Auth data file not found")
                return None
                
            with open(Config.AUTH_DATA_FILE, 'r') as f:
                auth_data = json.load(f)
            
            # Check if data is too old
            timestamp = datetime.fromisoformat(auth_data["timestamp"])
            if datetime.now() - timestamp > timedelta(hours=Config.SESSION_TIMEOUT_HOURS):
                self.logger.warning("Auth data is too old, may be expired")
                
            self.logger.info("Auth data loaded successfully")
            return auth_data
            
        except Exception as e:
            self.logger.error(f"Error loading auth data: {e}")
            return None
    
    def restore_session(self, auth_data: Dict[str, Any]) -> bool:
        """Restore browser session from auth data"""
        try:
            # First navigate to the domain to set cookies
            self.driver.get(Config.FRAMER_BASE_URL)
            time.sleep(2)
            
            # Clear existing cookies
            self.driver.delete_all_cookies()
            
            # Set cookies
            for cookie in auth_data.get("cookies", []):
                try:
                    # Remove problematic keys that Selenium doesn't accept
                    clean_cookie = {k: v for k, v in cookie.items() 
                                  if k not in ['sameSite', 'storeId']}
                    self.driver.add_cookie(clean_cookie)
                except Exception as e:
                    self.logger.warning(f"Could not set cookie {cookie.get('name', 'unknown')}: {e}")
            
            # Restore localStorage
            for key, value in auth_data.get("localStorage", {}).items():
                try:
                    self.driver.execute_script(f"localStorage.setItem('{key}', '{value}');")
                except Exception as e:
                    self.logger.warning(f"Could not set localStorage item {key}: {e}")
            
            # Restore sessionStorage
            for key, value in auth_data.get("sessionStorage", {}).items():
                try:
                    self.driver.execute_script(f"sessionStorage.setItem('{key}', '{value}');")
                except Exception as e:
                    self.logger.warning(f"Could not set sessionStorage item {key}: {e}")
            
            # Refresh page to apply session
            self.driver.refresh()
            time.sleep(3)
            
            self.logger.info("Session restored successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error restoring session: {e}")
            return False
    
    def is_logged_in(self) -> bool:
        """Check if user is currently logged in"""
        try:
            # Check for elements that only appear when logged in
            # This might need adjustment based on Framer's actual UI
            indicators = [
                "//button[@id='toolbar-publish-button']",  # Publish button
                "//div[contains(@class, 'avatar')]",       # User avatar
                "//button[contains(@aria-label, 'Account')]", # Account menu
            ]
            
            for indicator in indicators:
                try:
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, indicator))
                    )
                    if element:
                        self.logger.info("User appears to be logged in")
                        return True
                except:
                    continue
            
            # Check if we're on login page
            if "signin" in self.driver.current_url.lower():
                self.logger.info("Currently on login page - not logged in")
                return False
                
            self.logger.warning("Could not determine login status")
            return False
            
        except Exception as e:
            self.logger.error(f"Error checking login status: {e}")
            return False
