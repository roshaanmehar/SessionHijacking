# Universal Session Automation System

A powerful, universal browser session capture and replay system that works with **any website**. This system captures your complete login sessions (cookies, localStorage, sessionStorage, etc.) and can perfectly recreate them later for automation purposes.

## 🌟 Features

### Core Capabilities
- **Universal Compatibility**: Works with any website (Gmail, Facebook, Twitter, banking sites, etc.)
- **Complete Session Capture**: Captures cookies, localStorage, sessionStorage, and page states
- **Multi-Domain Support**: Handles complex applications that span multiple domains
- **Perfect Session Replay**: Recreates your exact login state with 100% accuracy
- **Stealth Technology**: Uses advanced techniques to avoid bot detection
- **Session Management**: Save, load, and manage multiple different sessions

### Advanced Features
- **Cross-Domain Authentication**: Captures sessions across unlimited websites simultaneously
- **Intelligent Domain Detection**: Automatically discovers all domains you visit
- **Session Validation**: Checks for expired sessions and warns users
- **Human-Like Behavior**: Random delays and realistic browsing patterns
- **Comprehensive Logging**: Detailed logs for debugging and monitoring
- **Interactive Interface**: Easy-to-use menu system for non-technical users

## 📋 Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Detailed Usage](#detailed-usage)
4. [System Architecture](#system-architecture)
5. [File Structure](#file-structure)
6. [Configuration](#configuration)
7. [API Reference](#api-reference)
8. [Examples](#examples)
9. [Troubleshooting](#troubleshooting)
10. [Advanced Usage](#advanced-usage)
11. [Security Considerations](#security-considerations)
12. [Contributing](#contributing)

## 🚀 Installation

### Prerequisites
- **Python 3.8+** (Python 3.9+ recommended)
- **Google Chrome** browser installed
- **Git** (for cloning the repository)

### Automatic Setup (Recommended)

#### Windows
\`\`\`batch
# Clone the repository
git clone https://github.com/your-username/universal-session-automation.git
cd universal-session-automation

# Run automatic setup
setup.bat
\`\`\`

#### Linux/Mac
\`\`\`bash
# Clone the repository
git clone https://github.com/your-username/universal-session-automation.git
cd universal-session-automation

# Make setup script executable and run
chmod +x setup.sh
./setup.sh
\`\`\`

### Manual Installation

1. **Clone Repository**
   \`\`\`bash
   git clone https://github.com/your-username/universal-session-automation.git
   cd universal-session-automation
   \`\`\`

2. **Create Virtual Environment**
   \`\`\`bash
   python -m venv venv
   
   # Activate (Windows)
   venv\\Scripts\\activate
   
   # Activate (Linux/Mac)
   source venv/bin/activate
   \`\`\`

3. **Install Dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Create Configuration**
   \`\`\`bash
   cp .env.example .env
   \`\`\`

5. **Test Installation**
   \`\`\`bash
   python test_system.py
   \`\`\`

## ⚡ Quick Start

### 1. Capture Your First Session

\`\`\`bash
# Start session capture
python capture_session.py --session-name "gmail-login"
\`\`\`

**What happens:**
1. Chrome browser opens
2. Navigate to Gmail and log in
3. Browse around, check emails, etc.
4. Press ENTER in terminal when done
5. System automatically captures all session data

### 2. Replay Your Session

\`\`\`bash
# Replay the captured session
python replay_session.py --session-name "gmail-login"
\`\`\`

**What happens:**
1. System loads your saved session
2. Restores all cookies and data
3. You're automatically logged into Gmail
4. Ready for automation or manual use

### 3. Interactive Mode (Easiest)

\`\`\`bash
# Launch interactive interface
python interactive.py
\`\`\`

**Features:**
- Menu-driven interface
- No command-line arguments needed
- Perfect for beginners
- Session management made easy

## 📖 Detailed Usage

### Session Capture

#### Basic Capture
\`\`\`bash
python capture_session.py --session-name "my-session"
\`\`\`

#### Advanced Capture Options
\`\`\`bash
# Capture with specific starting URL
python capture_session.py --session-name "facebook" --start-url "https://facebook.com"

# Capture with verbose logging
python capture_session.py --session-name "banking" --verbose
\`\`\`

#### What Gets Captured
- **Cookies**: All authentication tokens and preferences
- **localStorage**: Persistent application data
- **sessionStorage**: Temporary session data
- **Page States**: URLs, titles, and metadata
- **Domain Information**: All visited domains and subdomains

### Session Replay

#### Basic Replay
\`\`\`bash
python replay_session.py --session-name "my-session"
\`\`\`

#### Advanced Replay Options
\`\`\`bash
# Replay and navigate to specific URL
python replay_session.py --session-name "gmail" --target-url "https://mail.google.com/mail/u/0/#inbox"

# Replay in headless mode (no browser window)
python replay_session.py --session-name "automation" --headless

# Replay with verbose logging
python replay_session.py --session-name "debug-session" --verbose
\`\`\`

### Session Management

#### List Available Sessions
\`\`\`bash
# View all captured sessions
ls sessions/
\`\`\`

#### Session Files
Each session creates two files:
- \`sessionname_session.json\`: Complete session data
- \`sessionname_summary.txt\`: Human-readable summary

#### Delete Sessions
\`\`\`bash
# Remove session files
rm sessions/sessionname_*
\`\`\`

## 🏗️ System Architecture

### Component Overview

\`\`\`
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   config.py     │    │ browser_manager │    │ session_manager │
│ (Configuration) │    │   (Browser)     │    │ (Session Logic) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │universal_automation│
                    │  (Main Controller) │
                    └─────────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         │                       │                       │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│capture_session.py│   │replay_session.py│    │ interactive.py  │
│   (Capture)     │    │   (Replay)      │    │ (User Interface)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
\`\`\`

### Data Flow

\`\`\`
User Login → Browser Session → Session Capture → JSON Storage
     ↓              ↓              ↓              ↓
Manual Process → Automated → Multi-Domain → Persistent Storage
     ↓              ↓              ↓              ↓
Any Website → Chrome Driver → Complete State → File System
\`\`\`

### Session Restoration Flow

\`\`\`
JSON Storage → Session Manager → Browser Restoration → Active Session
     ↓              ↓              ↓                    ↓
Load Data → Parse Domains → Set Cookies/Storage → Ready for Use
\`\`\`

## 📁 File Structure

\`\`\`
universal-session-automation/
├── 📄 README.md                 # This comprehensive guide
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env.example             # Configuration template
├── 📄 .env                     # Your configuration (created)
│
├── 🔧 Core System Files
│   ├── config.py               # Central configuration management
│   ├── browser_manager.py      # Chrome browser control & stealth
│   ├── session_manager.py      # Session capture & restore logic
│   └── universal_automation.py # Main automation controller
│
├── 🎯 User Interface Scripts
│   ├── capture_session.py      # Command-line session capture
│   ├── replay_session.py       # Command-line session replay
│   └── interactive.py          # Interactive menu interface
│
├── 🛠️ Setup & Testing
│   ├── setup.sh               # Linux/Mac setup script
│   ├── setup.bat              # Windows setup script
│   └── test_system.py         # System verification tests
│
├── 📊 Generated Directories (created automatically)
│   ├── sessions/              # Stored session data
│   │   ├── session1_session.json
│   │   ├── session1_summary.txt
│   │   ├── session2_session.json
│   │   └── session2_summary.txt
│   │
│   ├── logs/                  # System logs
│   │   ├── capture.log        # Session capture logs
│   │   ├── replay.log         # Session replay logs
│   │   └── interactive.log    # Interactive mode logs
│   │
│   └── venv/                  # Python virtual environment
│       └── ...
\`\`\`

## ⚙️ Configuration

### Environment Variables (.env file)

\`\`\`env
# Default starting URL for session capture
DEFAULT_START_URL=https://google.com

# Optional: Override default settings
HEADLESS_MODE=false
VERBOSE_LOGGING=false

# Advanced: Browser settings
IMPLICIT_WAIT=10
EXPLICIT_WAIT=30
PAGE_LOAD_TIMEOUT=60

# Advanced: Session settings
SESSION_TIMEOUT_HOURS=24
CAPTURE_INTERVAL=2
\`\`\`

### Configuration Options

| Setting | Default | Description |
|---------|---------|-------------|
| \`DEFAULT_START_URL\` | \`https://google.com\` | Starting page for session capture |
| \`HEADLESS_MODE\` | \`false\` | Run browser without GUI |
| \`VERBOSE_LOGGING\` | \`false\` | Enable detailed logging |
| \`IMPLICIT_WAIT\` | \`10\` | Default element wait time (seconds) |
| \`EXPLICIT_WAIT\` | \`30\` | Maximum wait time for elements |
| \`PAGE_LOAD_TIMEOUT\` | \`60\` | Page load timeout (seconds) |
| \`SESSION_TIMEOUT_HOURS\` | \`24\` | Session expiration warning threshold |

## 📚 API Reference

### UniversalSessionAutomation Class

#### Constructor
\`\`\`python
automation = UniversalSessionAutomation(headless=False)
\`\`\`

**Parameters:**
- \`headless\` (bool): Run browser in headless mode

#### Methods

##### capture_session()
\`\`\`python
success = automation.capture_session(session_name="default", start_url=None)
\`\`\`

**Parameters:**
- \`session_name\` (str): Name for the captured session
- \`start_url\` (str, optional): Starting URL for capture

**Returns:**
- \`bool\`: True if capture successful, False otherwise

##### replay_session()
\`\`\`python
success = automation.replay_session(session_name="default", target_url=None)
\`\`\`

**Parameters:**
- \`session_name\` (str): Name of session to replay
- \`target_url\` (str, optional): URL to navigate to after restoration

**Returns:**
- \`bool\`: True if replay successful, False otherwise

##### list_available_sessions()
\`\`\`python
sessions = automation.list_available_sessions()
\`\`\`

**Returns:**
- \`List[str]\`: List of available session names

### UniversalSessionManager Class

#### Key Methods

##### start_monitoring()
\`\`\`python
success = session_manager.start_monitoring(start_url=None)
\`\`\`

Starts interactive session monitoring.

##### capture_complete_session()
\`\`\`python
session_manager.capture_complete_session()
\`\`\`

Captures session data from all visited domains.

##### restore_session()
\`\`\`python
success = session_manager.restore_session(session_data, target_url=None)
\`\`\`

Restores complete session state to browser.

### UniversalBrowserManager Class

#### Key Methods

##### create_driver()
\`\`\`python
driver = browser_manager.create_driver()
\`\`\`

Creates Chrome driver with stealth configuration.

##### random_delay()
\`\`\`python
browser_manager.random_delay(min_delay=1, max_delay=3)
\`\`\`

Adds human-like delays between actions.

## 💡 Examples

### Example 1: Social Media Management

\`\`\`bash
# Capture session with multiple social platforms
python capture_session.py --session-name "social-media"
# → Login to Facebook, Twitter, Instagram, LinkedIn
# → Press ENTER when done

# Later, replay for automation
python replay_session.py --session-name "social-media" --target-url "https://facebook.com"
# → All platforms are logged in and ready
\`\`\`

### Example 2: E-commerce Automation

\`\`\`bash
# Capture shopping session
python capture_session.py --session-name "shopping" --start-url "https://amazon.com"
# → Login to Amazon, add items to cart, save payment info
# → Press ENTER when ready

# Replay for automated purchasing
python replay_session.py --session-name "shopping" --target-url "https://amazon.com/cart"
# → Logged in with cart intact, ready for checkout automation
\`\`\`

### Example 3: Banking & Finance

\`\`\`bash
# Capture banking session (be careful with sensitive data!)
python capture_session.py --session-name "banking" --start-url "https://your-bank.com"
# → Login to bank, navigate to accounts
# → Press ENTER when done

# Replay for account monitoring
python replay_session.py --session-name "banking" --headless
# → Automated login for balance checking, transaction monitoring
\`\`\`

### Example 4: Development & Testing

\`\`\`bash
# Capture development environment session
python capture_session.py --session-name "dev-env"
# → Login to GitHub, AWS Console, monitoring tools
# → Press ENTER when done

# Replay for automated deployment
python replay_session.py --session-name "dev-env" --target-url "https://console.aws.amazon.com"
# → All development tools logged in and ready
\`\`\`

### Example 5: Content Management

\`\`\`bash
# Capture CMS session
python capture_session.py --session-name "cms" --start-url "https://wordpress.com"
# → Login to WordPress, Medium, other publishing platforms
# → Press ENTER when done

# Replay for content publishing
python replay_session.py --session-name "cms" --target-url "https://wordpress.com/post"
# → Ready for automated content publishing
\`\`\`

## 🔧 Troubleshooting

### Common Issues

#### 1. Import Errors
**Problem:** \`NameError: name 'List' is not defined\`

**Solution:**
\`\`\`bash
# Run the test system to verify installation
python test_system.py

# If issues persist, reinstall dependencies
pip install -r requirements.txt --force-reinstall
\`\`\`

#### 2. ChromeDriver Issues
**Problem:** Chrome driver not found or incompatible version

**Solution:**
\`\`\`bash
# The system uses undetected-chromedriver which handles this automatically
# If issues persist, update Chrome browser to latest version
# Or manually install ChromeDriver matching your Chrome version
\`\`\`

#### 3. Session Not Restoring
**Problem:** Session replay doesn't work, still shows login page

**Possible Causes & Solutions:**
- **Session Expired**: Capture a new session
- **Domain Changes**: Website changed domains, recapture session
- **Security Updates**: Site updated security, recapture session
- **Cookie Issues**: Clear browser data and recapture

#### 4. Permission Errors
**Problem:** Cannot create directories or save files

**Solution:**
\`\`\`bash
# Ensure you have write permissions in the project directory
chmod -R 755 .

# Or run with appropriate permissions
sudo python capture_session.py --session-name "test"
\`\`\`

#### 5. Browser Detection
**Problem:** Website detects automation and blocks access

**Solutions:**
- System uses stealth techniques, but some sites are very aggressive
- Try capturing session with different user agent
- Use residential proxy if needed
- Some sites may require manual intervention

### Debug Mode

Enable verbose logging for detailed troubleshooting:

\`\`\`bash
# Capture with debug info
python capture_session.py --session-name "debug" --verbose

# Replay with debug info
python replay_session.py --session-name "debug" --verbose
\`\`\`

### Log Files

Check log files for detailed error information:

\`\`\`bash
# View capture logs
cat logs/capture.log

# View replay logs
cat logs/replay.log

# View interactive logs
cat logs/interactive.log
\`\`\`

## 🚀 Advanced Usage

### Custom Automation Scripts

You can integrate the session system into your own automation scripts:

\`\`\`python
from universal_automation import UniversalSessionAutomation
from selenium.webdriver.common.by import By

# Create automation instance
with UniversalSessionAutomation(headless=True) as automation:
    # Replay existing session
    if automation.replay_session("gmail-session", "https://mail.google.com"):
        # Now you're logged in, perform automation
        driver = automation.driver
        
        # Example: Check for new emails
        unread_count = driver.find_element(By.CLASS_NAME, "unread-count").text
        print(f"Unread emails: {unread_count}")
        
        # Example: Send an email
        compose_button = driver.find_element(By.XPATH, "//div[text()='Compose']")
        compose_button.click()
        
        # ... more automation logic
\`\`\`

### Batch Session Management

\`\`\`python
# Example: Replay multiple sessions for different accounts
sessions = ["account1", "account2", "account3"]

for session_name in sessions:
    with UniversalSessionAutomation(headless=True) as automation:
        if automation.replay_session(session_name):
            # Perform automation for this account
            perform_account_automation(automation.driver)
\`\`\`

### Session Validation

\`\`\`python
from session_manager import UniversalSessionManager
from browser_manager import UniversalBrowserManager

# Check if session is still valid before using
def validate_session(session_name):
    with UniversalBrowserManager() as browser:
        session_manager = UniversalSessionManager(browser.driver)
        session_data = session_manager.load_session(session_name)
        
        if session_data:
            # Check session age
            from datetime import datetime, timedelta
            timestamp = datetime.fromisoformat(session_data["timestamp"])
            age = datetime.now() - timestamp
            
            if age > timedelta(hours=24):
                print(f"Session {session_name} is {age} old, may need refresh")
                return False
            return True
        return False
\`\`\`

### Scheduled Automation

\`\`\`bash
# Linux/Mac: Use cron for scheduled automation
# Edit crontab
crontab -e

# Add line for daily automation at 9 AM
0 9 * * * cd /path/to/project && python replay_session.py --session-name "daily-tasks" --headless

# Windows: Use Task Scheduler
# Create new task with action:
# Program: python
# Arguments: replay_session.py --session-name "daily-tasks" --headless
# Start in: C:\\path\\to\\project
\`\`\`

## 🔒 Security Considerations

### Data Security

#### What's Stored
- **Cookies**: May contain authentication tokens
- **localStorage**: Application data, potentially sensitive
- **sessionStorage**: Temporary data, usually less sensitive
- **URLs**: Pages visited during capture

#### Security Best Practices

1. **Secure Storage**
   \`\`\`bash
   # Encrypt session files (optional)
   gpg -c sessions/sensitive_session.json
   
   # Set restrictive permissions
   chmod 600 sessions/*.json
   \`\`\`

2. **Environment Security**
   - Use dedicated machine for automation
   - Keep system updated
   - Use antivirus software
   - Regular security scans

3. **Session Management**
   - Regularly refresh sessions
   - Delete old/unused sessions
   - Don't share session files
   - Use different sessions for different purposes

#### Sensitive Data Handling

\`\`\`bash
# For banking/financial sites, consider:
# 1. Use dedicated virtual machine
# 2. Enable full disk encryption
# 3. Use VPN for additional security
# 4. Regular session rotation
\`\`\`

### Legal Considerations

- **Terms of Service**: Ensure automation complies with website ToS
- **Rate Limiting**: Respect website rate limits
- **Data Privacy**: Handle personal data responsibly
- **Compliance**: Follow relevant regulations (GDPR, CCPA, etc.)

## 🤝 Contributing

### Development Setup

\`\`\`bash
# Clone repository
git clone https://github.com/your-username/universal-session-automation.git
cd universal-session-automation

# Create development environment
python -m venv dev-env
source dev-env/bin/activate  # Linux/Mac
# or
dev-env\\Scripts\\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Run tests
python test_system.py
pytest tests/  # If test suite exists
\`\`\`

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Type Hints**: Use type hints for all functions
- **Documentation**: Document all public methods
- **Logging**: Use appropriate logging levels

### Submitting Changes

1. Fork the repository
2. Create feature branch (\`git checkout -b feature/amazing-feature\`)
3. Commit changes (\`git commit -m 'Add amazing feature'\`)
4. Push to branch (\`git push origin feature/amazing-feature\`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Selenium**: Web automation framework
- **undetected-chromedriver**: Stealth browser automation
- **Chrome DevTools**: Browser control protocol

## 📞 Support

### Getting Help

1. **Check Documentation**: This README covers most use cases
2. **Check Logs**: Look in \`logs/\` directory for error details
3. **Run Tests**: Use \`python test_system.py\` to verify setup
4. **GitHub Issues**: Report bugs or request features

### Common Support Requests

#### "Session not working after website update"
- **Solution**: Recapture the session, websites change frequently

#### "Browser detected as bot"
- **Solution**: System uses stealth techniques, but some sites are aggressive. Try different user agents or manual intervention.

#### "Slow performance"
- **Solution**: Use headless mode (\`--headless\`) for better performance

#### "Session files too large"
- **Solution**: Normal for complex sites. Consider cleaning old sessions regularly.

## 🔄 Version History

### v1.0.0 (Current)
- Initial release
- Universal session capture and replay
- Multi-domain support
- Stealth browser automation
- Interactive interface
- Comprehensive logging

### Planned Features
- Session encryption
- Cloud storage integration
- Web-based interface
- Session sharing/export
- Advanced scheduling
- Performance optimizations

---

## 📊 Quick Reference

### Essential Commands

\`\`\`bash
# Setup
python test_system.py

# Capture session
python capture_session.py --session-name "my-session"

# Replay session
python replay_session.py --session-name "my-session"

# Interactive mode
python interactive.py

# List sessions
ls sessions/

# View logs
cat logs/capture.log
\`\`\`

### File Locations

| Type | Location | Purpose |
|------|----------|---------|
| Sessions | \`sessions/\` | Captured session data |
| Logs | \`logs/\` | System logs and debug info |
| Config | \`.env\` | Configuration settings |
| Scripts | Root directory | Main automation scripts |

### Key Features Summary

✅ **Universal Compatibility** - Works with any website  
✅ **Complete Session Capture** - Cookies, storage, state  
✅ **Multi-Domain Support** - Handle complex applications  
✅ **Stealth Technology** - Avoid bot detection  
✅ **Easy Interface** - Interactive and command-line modes  
✅ **Comprehensive Logging** - Debug and monitor everything  
✅ **Session Management** - Save, load, organize sessions  
✅ **Cross-Platform** - Windows, Mac, Linux support  

---

**Happy Automating! 🚀**

*This system opens up endless possibilities for web automation. From social media management to e-commerce automation, from development workflows to data collection - capture once, automate forever!*
