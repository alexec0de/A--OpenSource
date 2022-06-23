"""
A# - discord libs

"""

import discord
from discord.ext import commands


def check_func_discord(func, args):
	if func == 'bot':
		global client
		client = commands.Bot(command_prefix=args)
	
	elif func == 'on_ready':
		@client.event
		async def on_ready():
			print(args)
			
			
	elif func == 'add_command':
		print('test')
		@client.command(name = 'test')
		async def command(ctx):
			print('test')
			await ctx.send('test')
	elif func == 'run':
		client.run(args)