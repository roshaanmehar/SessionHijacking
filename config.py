import os
from pathlib import Path
from dotenv import load_dotenv

class Config:
    # File paths
    BASE_DIR = Path(__file__).parent
    SESSIONS_DIR = BASE_DIR / "sessions"
    LOGS_DIR = BASE_DIR / "logs"
    
    # Default session file
    DEFAULT_SESSION_FILE = SESSIONS_DIR / "default_session.json"
    
    # Selenium settings
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 30
    PAGE_LOAD_TIMEOUT = 60
    
    # Stealth settings
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    
    # Timing settings (in seconds)
    MIN_DELAY = 1
    MAX_DELAY = 3
    CLICK_DELAY = 0.5
    
    # Session validation
    SESSION_TIMEOUT_HOURS = 24
    
    # Monitoring settings
    CAPTURE_INTERVAL = 2  # seconds between captures during monitoring
    
    @classmethod
    def load_environment(cls):
        """Load environment variables from .env file"""
        load_dotenv()
    
    @classmethod
    def get_default_start_url(cls) -> str:
        """Get default starting URL from environment"""
        return os.getenv('DEFAULT_START_URL', 'https://google.com')
    
    @classmethod
    def ensure_directories(cls):
        """Create necessary directories if they don't exist"""
        cls.SESSIONS_DIR.mkdir(exist_ok=True)
        cls.LOGS_DIR.mkdir(exist_ok=True)
