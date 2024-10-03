import subprocess
import time
import os
import logging
from aiogram import Bot
import asyncio


API_TOKEN = '7537334155:AAH-ZKG1JXupeUoJtxsSeLhNnI-kNcbeQqI'
from pymongo import MongoClient
import certifi
MONGO_URI = 'mongodb+srv://Soul:JYAuvlizhw7wqLOb@soul.tsga4.mongodb.net'


client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['soul']
users_collection = db.users
    
ADMIN_ID = "1854133299 , 6444153490 , 1742327897 , 1798209383"
FORWARD_CHANNEL_ID = -1002181162852
CHANNEL_ID = -1002181162852
error_channel_id = -1002181162852
MAX_RESTARTS = 5
RESTART_PERIOD = 60  # Seconds

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
bot = Bot(API_TOKEN)

def start_bot():
    """Start the bot script as a subprocess."""
    return subprocess.Popen(['python', 'Gumnaam.py'])

async def notify_admin(message):
    """Send a notification message to the admin via Telegram."""
    try:
        await bot.send_message(ADMIN_ID, message)
        logging.info("Admin notified: %s", message)
    except Exception as e:
        logging.error("Failed to send message to admin: %s", e)

async def main():
    """Main function to manage bot process lifecycle."""
    restart_count = 0
    last_restart_time = time.time()
    
    while True:
        if restart_count >= MAX_RESTARTS:
            current_time = time.time()
            if current_time - last_restart_time < RESTART_PERIOD:
                wait_time = RESTART_PERIOD - (current_time - last_restart_time)
                logging.warning("Maximum restart limit reached. Waiting for %.2f seconds...", wait_time)
                await notify_admin(f"⚠️ Maximum restart limit reached. Waiting for {int(wait_time)} seconds before retrying.")
                await asyncio.sleep(wait_time)
            restart_count = 0
            last_restart_time = time.time()

        logging.info("Starting the bot...")
        process = start_bot()
        await notify_admin("🚀 Bot is starting...")

        while process.poll() is None:
            await asyncio.sleep(5)
        
        logging.warning("Bot process terminated. Restarting in 10 seconds...")
        await notify_admin("⚠️ The bot has crashed and will be restarted in 10 seconds.")
        restart_count += 1
        await asyncio.sleep(10)
        

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Watcher script terminated by user.")
