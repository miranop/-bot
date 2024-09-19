import discord
from discord.ext import commands

class LogicCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("おはようございます")
    
async def setup(bot):
    await bot.add_cog(LogicCog(bot))
    