import discord
bot = discord.Client()


@bot.event
async def on_ready():
    print("Ready to be hysterical!")
