import discord
import os
from DBtask import create_database
from discord.ext import commands
from dotenv import load_dotenv
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix='/',#コマンドを/に指定
    case_insensitive=True,#大文字小文字を判定
    intents=intents
)
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')


async def load_Cog():
    for filename in os.listdir('./Cogs'):
        if(filename.endswith(".py")):
            try:
                await bot.load_extension(f"Cogs.{filename[:-3]}")
                print(f"Loaded extension: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load extension {filename}: {e}")
        
        
@bot.event
async def on_ready():
    await load_Cog()
    create_database()
    print(f'{bot.user} has connected to Discord!')
bot.run(TOKEN)