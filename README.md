# Universal Session Automation System

> **Capture any website login session once, replay it forever**

A powerful browser automation system that captures your complete login sessions (cookies, localStorage, sessionStorage) from any website and perfectly recreates them later for automation.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)

---

## ✨ Features

- 🌐 **Universal** - Works with any website (Gmail, Facebook, banking, etc.)
- 🔄 **Complete Capture** - Saves cookies, localStorage, sessionStorage, and page states
- 🏢 **Multi-Domain** - Handles complex apps across multiple domains
- 👤 **Stealth Mode** - Advanced bot detection avoidance
- 📱 **Easy Interface** - Interactive menu or command-line options
- 🔒 **Secure** - Local storage with session validation

---

## 🚀 Quick Start

### 1. Install
\`\`\`bash
git clone https://github.com/your-repo/universal-session-automation.git
cd universal-session-automation
pip install -r requirements.txt
\`\`\`

### 2. Capture a Session
\`\`\`bash
python capture_session.py --session-name "gmail"
\`\`\`
- Browser opens → Login to Gmail → Browse around → Press ENTER
- Session automatically saved

### 3. Replay Session
\`\`\`bash
python replay_session.py --session-name "gmail"
\`\`\`
- Instantly logged back into Gmail
- Ready for automation

---

## 📖 Usage

### Interactive Mode (Recommended)
\`\`\`bash
python interactive.py
\`\`\`
Simple menu interface - no commands to remember!

### Command Line

**Capture Sessions:**
\`\`\`bash
# Basic capture
python capture_session.py --session-name "my-session"

# Start from specific URL
python capture_session.py --session-name "facebook" --start-url "https://facebook.com"
\`\`\`

**Replay Sessions:**
\`\`\`bash
# Basic replay
python replay_session.py --session-name "my-session"

# Go to specific page after login
python replay_session.py --session-name "gmail" --target-url "https://mail.google.com/mail/u/0/#inbox"

# Run without browser window
python replay_session.py --session-name "automation" --headless
\`\`\`

---

## 💡 Real Examples

### Social Media Management
\`\`\`bash
# Capture: Login to Facebook, Twitter, Instagram
python capture_session.py --session-name "social-media"

# Replay: All platforms logged in instantly
python replay_session.py --session-name "social-media"
\`\`\`

### E-commerce Automation
\`\`\`bash
# Capture: Login to Amazon, add items to cart
python capture_session.py --session-name "shopping"

# Replay: Cart and login preserved
python replay_session.py --session-name "shopping" --target-url "https://amazon.com/cart"
\`\`\`

### Development Workflow
\`\`\`bash
# Capture: Login to GitHub, AWS, monitoring tools
python capture_session.py --session-name "dev-tools"

# Replay: All dev tools ready instantly
python replay_session.py --session-name "dev-tools"
\`\`\`

---

## 🏗️ How It Works

\`\`\`
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   1. CAPTURE    │    │   2. STORE      │    │   3. REPLAY     │
│                 │    │                 │    │                 │
│ • Login manually│───▶│ • Save cookies  │───▶│ • Restore data  │
│ • Browse around │    │ • Save storage  │    │ • Auto login    │
│ • Press ENTER   │    │ • Save state    │    │ • Ready to use  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
\`\`\`

**What Gets Captured:**
- 🍪 All cookies (authentication tokens)
- 💾 localStorage (app preferences)
- 🔄 sessionStorage (temporary data)
- 🌐 All visited domains
- 📍 Page URLs and states

---

## 📁 Project Structure

\`\`\`
universal-session-automation/
├── 📄 README.md                 # You are here
├── 📄 requirements.txt          # Dependencies
├── 📄 .env.example             # Config template
│
├── 🎯 Main Scripts
│   ├── capture_session.py      # Capture sessions
│   ├── replay_session.py       # Replay sessions
│   └── interactive.py          # Easy menu interface
│
├── 🔧 Core System
│   ├── config.py               # Settings
│   ├── browser_manager.py      # Chrome control
│   ├── session_manager.py      # Session logic
│   └── universal_automation.py # Main controller
│
├── 🛠️ Setup
│   ├── setup.sh               # Linux/Mac setup
│   ├── setup.bat              # Windows setup
│   └── test_system.py         # Verify installation
│
└── 📊 Generated (auto-created)
    ├── sessions/              # Your saved sessions
    └── logs/                  # System logs
\`\`\`

---

## ⚙️ Configuration

Create `.env` file:
\`\`\`env
# Starting URL for captures
DEFAULT_START_URL=https://google.com

# Optional settings
HEADLESS_MODE=false
VERBOSE_LOGGING=false
SESSION_TIMEOUT_HOURS=24
\`\`\`

---

## 🔧 Installation

### Automatic Setup

**Windows:**
```batch
git clone https://github.com/your-repo/universal-session-automation.git
cd universal-session-automation
setup.bat
