import os
import sys
import discord

from classes import CustomBot

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except OSError:
    pass


# __cogs__ = ['help', 'remind', 'schedule']
__cogs__ = ['help', 'remind']

bot = CustomBot(case_insensitive=True,
                command_prefix='-',
                activity=discord.Game(name='-help for information!'),
                strip_after_prefix=True,
                max_messages=None)


if __name__ == '__main__':
    for cog in __cogs__:
        bot.load_extension(f'cogs.{cog}')
    token = open('TOKEN', 'r')
    bot.run(token.readline().strip())
