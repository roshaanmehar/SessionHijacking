import random
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config

try:
    import undetected_chromedriver as uc
    UNDETECTED_AVAILABLE = True
except ImportError:
    UNDETECTED_AVAILABLE = False

class UniversalBrowserManager:
    def __init__(self, headless: bool = False, use_stealth: bool = True):
        self.headless = headless
        self.use_stealth = use_stealth
        self.driver = None
        self.logger = logging.getLogger(__name__)
        
    def create_driver(self):
        """Create and configure Chrome driver with stealth options"""
        try:
            if self.use_stealth and UNDETECTED_AVAILABLE:
                self.logger.info("Using undetected-chromedriver for stealth")
                options = uc.ChromeOptions()
            else:
                self.logger.info("Using standard ChromeDriver")
                options = Options()
            
            # Basic options
            if self.headless:
                options.add_argument("--headless")
            
            # Enhanced stealth options
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-plugins")
            options.add_argument("--disable-images")  # Faster loading
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            # Random user agent
            user_agent = random.choice(Config.USER_AGENTS)
            options.add_argument(f"--user-agent={user_agent}")
            
            # Window size
            options.add_argument("--window-size=1920,1080")
            
            # Allow all cookies and storage
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            
            # Create driver
            if self.use_stealth and UNDETECTED_AVAILABLE:
                self.driver = uc.Chrome(options=options)
            else:
                self.driver = webdriver.Chrome(options=options)
            
            # Configure timeouts
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
            self.driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
            
            # Execute stealth script
            if not UNDETECTED_AVAILABLE:
                self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.logger.info("Chrome driver created successfully")
            return self.driver
            
        except Exception as e:
            self.logger.error(f"Error creating driver: {e}")
            raise
    
    def random_delay(self, min_delay: float = None, max_delay: float = None):
        """Add random delay to mimic human behavior"""
        min_delay = min_delay or Config.MIN_DELAY
        max_delay = max_delay or Config.MAX_DELAY
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
    
    def quit(self):
        """Safely quit the driver"""
        if self.driver:
            try:
                self.driver.quit()
                self.logger.info("Driver quit successfully")
            except Exception as e:
                self.logger.error(f"Error quitting driver: {e}")
