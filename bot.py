import config
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ';;;', intents = discord.Intents.all())
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
  if ctx.author.id == 458666543924903936:
    bot.load_extension(f"cogs.{extension}")
    await ctx.send('Загрузил!')

@bot.command()
async def unload(ctx, extension):
  if ctx.author.id == 458666543924903936:
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send('Отгрузил!')

@bot.command()
async def reload(ctx, extension):
  if ctx.author.id == 458666543924903936:
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send('Перезагрузил!')

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.TOKEN)