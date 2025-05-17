#!/usr/bin/env bash
# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run webserver for uptime
python3 webserver.py &

# Run the bot
python3 app.py
