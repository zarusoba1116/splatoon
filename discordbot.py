from ctypes.wintypes import WORD
import re
import random
from re import purge
from sqlite3 import Timestamp
import discord
from discord import message
from discord import channel
from discord.ext import commands
from discord.utils import get
from os import getenv
import traceback
import asyncio
import datetime
import humanfriendly
import os
import schedule

intents = discord.Intents.all()
intents.typing = False
guild = 852145141909159947

token = getenv('token')
bot = commands.Bot(command_prefix='$',help_command=None,case_insensitive=True,intents=intents)

@bot.command(name = 'embed1')
async def embed1(ctx):
    embed1 = discord.Embed( # Embedを定義する
                          title="```📜 ルール```",# タイトル
                          color=0x53a9e9, # フレーム色指定(今回は緑)
                          description="メンバーは、すべてのルールに従うことが求められます。\nこれに従わない場合は、適切な措置が取られる可能性があります。", inline = False)
    embed1.add_field(name="🔹 **ベルリン行動規範**",value="このサーバーでは「ベルリン行動規範」と呼ばれるインターネットコミュニティに最適化されたルールを適用させて頂いています。\n`🔗`[ベルリン行動規範](https://berlincodeofconduct.org/ja/)", inline = False) # フィールドを追加。
    embed1.add_field(name="🔹 **Discordの利用規約とコミュニティ・ガイドライン、も遵守されます**",value="`🔗`[利用規約](https://discord.com/terms)\n`🔗`[コミュニティ・ガイドライン](https://discord.com/guidelines)", inline = False) # フィールドを追加。
    embed1.add_field(name="🔹 **トピックを守り、チャンネルを正しく使って下さい**",value="トピックに沿ってチャンネルを正しく使用して下さい", inline = False) # フィールドを追加。
    embed1.add_field(name="🔹 **いかなる種類の広告、自己宣伝、一般的な勧誘の禁止**",value="第三者のサービスを宣伝しないでください。", inline = False) # フィールドを追加。
    await ctx.send(embed=embed1) # embedの送信には、embed={定義したembed名}

bot.run(token)
