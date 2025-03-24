import os
from dotenv import load_dotenv
import discord
import asyncio

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

def replace_mentions(message):
    """Replaces user mentions with readable usernames."""
    for user in message.mentions:
        message.content = message.content.replace(f"<@{user.id}>", f"@{user.name}")
    return message.content

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)

    if channel:
        messages = []
        async for message in channel.history(limit=None, oldest_first=True):
            content = replace_mentions(message).strip()  # Convert mentions
            timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S")

            attachment_urls = [attachment.url for attachment in message.attachments]
            
            formatted_message = f"[{timestamp}] {message.author}: {content}"
            
            # Append image URLs if any exist
            if attachment_urls:
                formatted_message += " " + " ".join(attachment_urls)

            # print(formatted_message)  # Debugging output
            messages.append(formatted_message)

        channel_name = channel.name.replace(" ", "_")  
        filename = f"{channel_name}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(messages))

        print(f"Messages saved to {filename}")
        await client.close()

client.run(TOKEN)
