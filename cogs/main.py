from sys import prefix
import discord
from discord.ext import commands
import config
from discord import utils
import datetime 



class Main(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		await self.bot.change_presence(
			activity=discord.Streaming(name=';;;help', url='https://www.twitch.tv/jok_exe')
		)

	@commands.command()

	async def help (self, ctx):
		emb = discord.Embed(title = '', description = '```Все доступные команды для музыкального бота```\n**play(ссылка)** - запустит трек который вы выберете (видео только с ютуба)\n**stop** - остановит музыку\n**pause** - ставит на паузу\n**connect** - бот присоединится к каналу в котором вы находитесь\n**next** - переключит на следующий трек в очереди\n**previous** - запустит предыдущий трек в очереди\n**shuffle** - перемешает очередь\n**repeat** - ставит трек на повтор\n**queue** - покажет очередь треков\n**volume** - изменяет громкость бота\n**lyrics (название трека)** - выдаст текст песни которую вы закажете\n**playing** - покажет название трека, который сейчас играет\n**restart** - перезапустит трек', colour = discord.Color.from_rgb(48,52,52))

		emb.set_image(url = '')

		await ctx.send(embed = emb)

def setup(bot):
	bot.add_cog(Main(bot))