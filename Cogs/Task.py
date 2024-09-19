import datetime
import discord
from discord.ext import commands
from DBtask import add_Task, view_Task

class TaskCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def addtask(self,ctx,time: str,title: str, details: str):
        #タスク追加
        try:
            # 時間のフォーマットを確認
            datetime.strptime(time, "%Y-%m-%d %H:%M")
            
            #筆者を取得
            userid = str(ctx.author.id)
            taskid = add_Task(userid,time,title,details)
            await ctx.send(f'タスクが追加されました:タスクID:{taskid}')
        except ValueError:
            await ctx.send('無効なフォーマットです')
    @commands.command()
    async def mytasks(self,ctx):
        userid = str(ctx.author.id)
        tasks = view_Task(userid)
        if tasks:
             task_list = "\n".join([f"ID: {task[0]}, 時間: {task[1]}, タイトル: {task[2]}" for task in tasks])
             await ctx.send(f'あなたのタスク:\n{task_list}')
        else:
            await ctx.send('タスクが登録されていません')    
    
async def setup(bot):
    await bot.add_cog(TaskCog(bot))
    