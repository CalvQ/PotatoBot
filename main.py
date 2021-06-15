import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(brief='Testing function for output from bot')
async def debug(ctx):
    await ctx.send('"' + ctx.message.content + '"' + ' was sent by ' + ctx.message.author.name)

token = open('TOKEN', 'r')
bot.run(token.readline().strip())
