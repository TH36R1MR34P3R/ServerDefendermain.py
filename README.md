Server Defender Bot
Overview
The Server Defender Bot is a Discord bot that helps protect servers from malicious links and attachments. The bot scans all messages sent in a server and checks if the links or attachments contained in the message are malicious. If a malicious link or attachment is detected, the bot will take action to protect the server and its users.

How it Works
The Server Defender Bot uses the VirusTotal API to scan all links and attachments contained in a message. If the VirusTotal API detects that the link or attachment is malicious, the bot will take action to protect the server and its users.

Features
Scan all links and attachments contained in a message.
Use the VirusTotal API to check if the links or attachments are malicious.
Reply to the message with a warning not to click the link.
Tag a specified role in the server with a warning not to click the link.
Send a private message to the author of the message with a warning and a 24-hour timeout.
Log the message and the reason for the timeout in a specified text channel.
Apply a 24-hour timeout to the author of the message.
Requirements
A Discord Bot Token
A VirusTotal API Key
The Python 3.7 or higher
The discord, asyncio, requests, re, and os packages.
How to Run
Install the required packages by running pip install discord asyncio requests re os.
Set the environment variables BOT_TOKEN and API_KEY with your Discord Bot Token and VirusTotal API Key, respectively.
Run the script with the command python server_defender_bot.py.
Configuration
The Server Defender Bot can be configured to meet the needs of your server.

Intents: The bot uses the default intents, with the message content intent enabled.
API Key: The VirusTotal API Key is set in the environment variable API_KEY.
Role: The role to tag in the reply to the message can be configured by changing the role name in the role variable to the desired role name.
Text Channel: The text channel to log the messages and the reason for the timeout can be configured by changing the channel name in the log_channel variable to the desired channel name.
Timeout: The length of the timeout can be changed by modifying the timedelta argument in the message.author.timeout function.
Limitations
The Server Defender Bot is limited by the accuracy of the VirusTotal API and the rate limits set by VirusTotal and Discord. The bot has been designed to handle these limitations, but the accuracy of the scans and the speed of the replies may be affected.

Things to note, to increase the capabiltys of the bot virus total api will need an upgrade the bot token and api key are set to pull from a secrets file it is recommend to store these in a env/secrets location if not you will need to change  api_key = os.environ['API_KEY'] to api_key = "actuall api key" and client.run(os.environ['BOT_TOKEN']) to client.run(" Actual Bot Token")  To reduc false positives you may change the ammount of venders that would need to detect the attachment as malicous here -if data["positives"] > 2: #number of venders to detect (2)- it is currently set at 2 venders but may be increased or set at one with 0. For questions and bugs please send me a message via discord user - TH3 6R1M R34P3R#0001