
from discord.ext.commands import bot
from discord.ext import commands
from tdaUtil import getPayouts
TOKEN = ""

class elpres(bot):

    async def on_ready(self):
        print("Logged in as {0}".format(self.user))

    @bot.command()
    @commands.command()
    async def CashMoney(self, ctx):
        """
        Portfolio update command
        :param ctx:
        :return:
        """
        await ctx.send(getPayouts())

    @bot.command()
    @commands.command()
    async def who(self, ctx):
        await ctx.send("I am God")

if __name__ == "__main__":
    elpres.run(TOKEN)