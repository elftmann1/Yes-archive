# Discord Message Saver

A simple tool that uses a Discord bot with message reading privileges to save messages from a specified channel.

## Features

- Saves messages from a specific Discord channel.
- Uses a bot token securely via `.env` file.
- Designed to run inside a Python virtual environment.

---

## Prerequisites

- Python 3.8+
- A Discord bot with access to the desired server and permission to **Read Message History** and **Read Messages**.
- The `channel_id` you want to save messages from.
- The bot token.

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/discord-msg-saver.git
   cd discord-msg-saver

Create a virtual environment:

On Windows:
```bash
python -m venv venv

python3 -m venv venv

pip install -r requirements.txt


Create a .env file in the project root and add the following:
DISCORD_TOKEN=your_bot_token_here
CHANNEL_ID=your_desired_channel_id

Run the script:
python yessave.py
