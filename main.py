import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "emo" in message.content:
        await message.channel.send("EMO CHICK https://open.spotify.com/album/37CqAwxTungNxKpIK5vSgE")

    if "post malone" in message.content:
        await message.reply("keep listening to him or :skull: ")

    if client.user.mentioned_in(message):
        await message.channel.send('ping=:rainbow_flag: ')

    if "tanvi" in message.content:
        await message.reply("One more time you say tanvi and ur banned:heart: ")

    if "patrick" in message.content:
        await message.reply("Yea its my bot")


client.run(TOKEN)
