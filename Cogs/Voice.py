import discord
from discord.ext import commands

class VoiceNotificationCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.sendroom_id = 00000000000000000
        self.voiceroom_ids = [000000000000]
        print("check")
        
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        if(before.channel != after.channel):#チャンネルの入室ステータスが変更されたとき
            sendroom = self.bot.get_channel(self.sendroom_id)
            
            if not sendroom:
                print(f"Error: Channel with ID {self.sendroom_id} not found")
                return

            if before.channel and before.channel.id in self.voiceroom_ids:
                print(f"Sending exit message for {member.name}")
                try:
                    await sendroom.send(f"{member.name}が{before.channel.name}から退室しました")
                except Exception as e:
                    print(f"Error sending exit message: {e}")
            
            # 入室通知
            if after.channel and after.channel.id in self.voiceroom_ids:
                print(f"Sending enter message for {member.name}")
                try:
                    await sendroom.send(f"@everyone {member.name}が{after.channel.name}に入室しました")
                except Exception as e:
                    print(f"Error sending enter message: {e}")
            
async def setup(bot):
    await bot.add_cog(VoiceNotificationCog(bot))
    print('VoiceNotificationCog has been added to the bot')
