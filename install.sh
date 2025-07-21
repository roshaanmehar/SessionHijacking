#!/bin/bash

echo "🚀 Setting up Framer Auto Publisher..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Make scripts executable
chmod +x setup_session.py
chmod +x publish.py

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Copy .env.example to .env and set your project URL"
echo "2. Run: python run.py (this will handle setup and publishing)"
echo "   OR manually: python setup_session.py then python publish.py"
