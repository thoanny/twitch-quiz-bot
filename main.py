from dotenv import dotenv_values
from twitchio.ext import commands

config = dotenv_values(".env")


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=config['TMI_TOKEN'], prefix=config['BOT_PREFIX'], initial_channels=[config['CHANNEL']])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()
