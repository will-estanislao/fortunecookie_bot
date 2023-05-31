## Fortune Cookie bot

import random
import discord
import os # this library is for using data stored in .env file
from discord.ext import commands # To get extra bot features
from dotenv import load_dotenv # Need this to connect to .env file and get var

random.seed()
load_dotenv()
bot = commands.Bot(command_prefix='fc!')


# Functions
def get_fortune():
    text_file = open("fortune-cookie-generator.txt", "r")
    fortune = []

    for x in text_file:
        fortune.append(x)

    text_file.close()

    your_fortune = fortune[random.randint(0, len(fortune))]

    print(your_fortune)

    return your_fortune

def get_lucky_numbers():
    lucky_nums = []

    for x in range(7):
        random_num = random.randint(1, 100)
        
        if(len(lucky_nums)>0):
            num_index = len(lucky_nums)-1
            if(lucky_nums[num_index] == random_num):
                random_num = random.randint(1,100)
            
        
        lucky_nums.append(random_num)

    return lucky_nums

# Bot is online
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('I\'m online ^w^!')

# Bot gives a fortune, and random numbers
@bot.command(name='cookie')
async def cookie(ctx):
    
    your_fortune = get_fortune()
    your_numbers = get_lucky_numbers()

    await ctx.send("Your fortune today is:\n{}\nYour lucky numbers are:\n\t{}".format(your_fortune, your_numbers))

@bot.command(name='numbers')
async def numbers(ctx):

    your_numbers = get_lucky_numbers()

    await ctx.send("Your new lucky numbers are:\n {}".format(your_numbers))

@bot.command(name="explode")
async def explode(ctx):
    await ctx.send("I guess this it... :\'^[. Goodbye cruel world...")
    # Send wario audio attachment
    # leave server
    # go offline

# Special option, EXPLODE - sends a yt vid of an explosion, says a final goodbye, and just quits lol
# Write descripts for commands

# Runs bot
bot.run(os.getenv('TOKEN'))

