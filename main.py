import asyncio
import os
import re
from datetime import timedelta

import discord
import requests

# Set Intents
intents = discord.Intents.default()
intents.message_content = True
# Client
client = discord.Client(intents=intents)
# API KEY
api_key = os.environ['API_KEY']


async def send_virus_total_request(link):
    params = {"apikey": api_key}
    scan_id = link
    response = requests.post("https://www.virustotal.com/vtapi/v2/url/report",
                             params=params, data={"resource": scan_id}, timeout=10)

    return response.json()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    links = re.findall(r"(https?://\S+)", message.content)
    attachments = [attachment.url for attachment in message.attachments]
    links_and_attachments = links + attachments
    for link in links_and_attachments:

        async def rate_limit_discord():
            # Add rate limiting for Discord messages
            async with message.channel.typing():
                # rate limit of 45 messages per second
                await asyncio.sleep(1 / 45)

        await rate_limit_discord()

        # Add rate limiting for VirusTotal API
        data = await send_virus_total_request(link)
        if data["response_code"] != 1:
            continue

        scan_id = data["scan_id"]
        params = {"apikey": api_key}
        response = requests.post("https://www.virustotal.com/vtapi/v2/url/report",
                                 params=params, data={"resource": scan_id}, timeout=10)
        data = response.json()
        if data["positives"] > 2: #number of venders to detect (2)
            # Reply to message w/ no mention, tag role, pm message author.
            role = discord.utils.get(
                message.guild.roles, name="ServerDefenderPings")
            await message.reply(f"{role.mention} Detected As Malicious, Do Not Click ! 24 Hour Timeout Has Been Applied.", mention_author=False)
            await message.author.send("You have been timed out for 24 hours because of the malicious link/file you sent. https://media.tenor.com/p5Qmh_2RT9YAAAAC/your-tactics-dont-work-on-me-eric-cartman.gif")
            await message.author.send("If you think this was done in error, please contact an administrator.")

            # Log the message content and the reason for the timeout in text channel.
            log_channel = discord.utils.get(
                message.guild.text_channels, name="serverdefenderlogs")
            log = f"User {message.author} sent a malicious message: {message.content}. Reason: Malicious links/attachments."
            await log_channel.send(log)
# Apply 24 Hour Timeout
            await message.author.timeout(timedelta(days=1), reason="Malicious links/attachments")

# Bot Token
client.run(os.environ['BOT_TOKEN'])
