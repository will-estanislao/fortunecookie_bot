## Fortune Cookie bot
## Bot Token:
# MTExMjU0NTc5MDY5OTc2NTc2MQ.GJLbFg.hQBPF18XoQIStyIhtrvzMgYeQUALC-X1keNUQM

import random
import discord
import os # this library is for using data stored in .env file
from discord.ext import commands # To get extra bot features
from dotenv import load_dotenv # Need this to connect to .env file and get var

load_dotenv()
bot = commands.Bot(command_prefix='fc!')

# Bot is online
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('I\'m online ^w^!')

# Bot gives a fortune, and random numbers
@bot.command(name='cookie')
async def cookie(ctx):
    await ctx.send("Your fortune today is:\n\t [Fortune Here]\nYour lucky numbers are:\n\t [Numbers Here]")

@bot.command(name='numbers')
async def numbers(ctx):
    await ctx.send("Your lucky numbers today:\n [random num]")

@bot.command(name="")
# Commands: cookie, lucky, explode
# Lucky numbers - generate 7 random numbers
# Generate 5 random numbers 
# Get the fortunes from a json file, randomly select one
# Special option, EXPLODE - sends a yt vid of an explosion, says a final goodbye, and just quits lol
# Write descripts for commands

# Runs bot
bot.run(os.getenv('TOKEN'))

