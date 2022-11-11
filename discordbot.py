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
import Word_list
import schedule

intents = discord.Intents.all()
intents.typing = False
guild = 852145141909159947

token = getenv('token')
bot = commands.Bot(command_prefix='$',help_command=None,case_insensitive=True,intents=intents)

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(852145141909159947)
    channel = guild.get_channel(852145141909159950)
    await channel.send(f"{member.mention}がサーバーに参加したゾ～\nハイ、ヨロシクゥ！")

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@bot.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=discord.Color.blue())
        em.set_footer(text = f"{snipe_message_author[channel.id]} が送信しました")

        await ctx.send(embed = em)
    except KeyError: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send("最近削除されたメッセージはありません")

@bot.command()
async def ping(ctx):
    raw_ping = bot.latency
    ping = round(raw_ping * 1000)
    embed_ping = discord.Embed(title="FF外から失礼するゾ～(謝罪)BOTの応答速度",description=f"```{ping}ms```",color=0xa1b3b5)
    embed_ping.set_author(name="Pong! This is the response speed.",icon_url="https://media.discordapp.net/attachments/889860265896722442/896781428350677022/084c6c1c62a26a59.png")
    await ctx.send(embed=embed_ping)

@bot.command()
async def syamu(ctx):
    guild = bot.get_guild(852145141909159947)
    channel = guild.get_channel(852145141909159950)
    await channel.send("https://pbs.twimg.com/media/FZyk185aUAALd7Q?format=jpg&name=900x900")

@bot.command()
@commands.has_permissions(ban_members=True)
async def delmsg(ctx, target:int):
    channel = ctx.message.channel
    deleted = await channel.purge(limit=target)
    delmsg = discord.Embed(title="メッセージの削除が完了しました。",description=f"```{len(deleted)}メッセージを削除しました。```",color=0xa1b3b5)
    delmsg.set_author(name="The message deletion is complete",icon_url="https://media.discordapp.net/attachments/889860265896722442/892047450754416650/Delete.png")
    await ctx.send(embed=delmsg)

@bot.listen("on_message")
async def on_message(message):
    pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
    url = message.content
    x = random.randint(0,10)
    ff = random.randint(0,10)
    if message.author.bot:
        return
    elif re.match(pattern, url):
        if x < 2.5:
            if ff < 0.5:
                await message.add_reaction('❤️')
                await message.add_reaction('♻️')
                async with message.channel.typing():
                    await asyncio.sleep(1)
                    await message.channel.send("FF外から失礼するゾ～（突撃）この乱戦面白スギィ！！！！！")
                    await asyncio.sleep(0.5)
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                        await message.channel.send("自分、漁夫いいっすか？ 秘密知ってそうだから収容所にブチ込んでやるぜー")
                        await asyncio.sleep(0.5)
                        async with message.channel.typing():
                            await asyncio.sleep(1)
                            await message.channel.send("いきなり撃ってすいません！許して下さい、なんでもしますから！(なんでもするとは言ってない)")
            else:
                await message.add_reaction('❤️')
                await message.add_reaction('♻️')
                async with message.channel.typing():
                    await asyncio.sleep(1)
                    await message.channel.send("FF外から失礼するゾ～（謝罪）このリンク先面白スギィ！！！！！")
                    await asyncio.sleep(0.5)
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                        await message.channel.send("自分、拡散いいっすか？ 淫夢知ってそうだから淫夢のリストにぶち込んでやるぜー")
                        await asyncio.sleep(0.5)
                        async with message.channel.typing():
                            await asyncio.sleep(1)
                            await message.channel.send("いきなりリプしてすみません！許してください！なんでもしますから！(なんでもするとは言ってない)")
    elif message.attachments:
        if x < 2.5:
            if ff < 0.5:
                for attachment in message.attachments:
                    if attachment.url.endswith(("png", "jpg", "jpeg")):
                        await message.add_reaction('❤️')
                        await message.add_reaction('♻️')
                        async with message.channel.typing():
                            await asyncio.sleep(1)
                            await message.channel.send("FF外から失礼するゾ～（突撃）この乱戦面白スギィ！！！！！")
                            await asyncio.sleep(0.5)
                            async with message.channel.typing():
                                await asyncio.sleep(1)
                                await message.channel.send("自分、漁夫いいっすか？ 秘密知ってそうだから収容所にブチ込んでやるぜー")
                                await asyncio.sleep(0.5)
                                async with message.channel.typing():
                                    await asyncio.sleep(1)
                                    await message.channel.send("いきなり撃ってすいません！許して下さい、なんでもしますから！(なんでもするとは言ってない)")
            else:
                await message.add_reaction('❤️')
                await message.add_reaction('♻️')
                async with message.channel.typing():
                    await asyncio.sleep(1)
                    await message.channel.send("FF外から失礼するゾ～（謝罪）このリンク先面白スギィ！！！！！")
                    await asyncio.sleep(0.5)
                    async with message.channel.typing():
                        await asyncio.sleep(1)
                        await message.channel.send("自分、拡散いいっすか？ 淫夢知ってそうだから淫夢のリストにぶち込んでやるぜー")
                        await asyncio.sleep(0.5)
                        async with message.channel.typing():
                            await asyncio.sleep(1)
                            await message.channel.send("いきなりリプしてすみません！許してください！なんでもしますから！(なんでもするとは言ってない)")
    elif bot.user in message.mentions:
        await message.channel.send("ホモはせっかち、はっきりわかんだね")
    else:
        if message.author.bot:
            return
        else:
            if x < 2.5:
                await message.reply(f"{random.choice(Word_list.word)}", mention_author=False)

bot.run(token)
