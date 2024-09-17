import discord
from discord.ext import commands
from cog import config

class button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.pages[
            discord.Embed(title="Selamlar1"),
            discord.Embed(title="Selamlar2")
        ]

    @discord.ui.button(label="Selam")
    async def button(self,ctx: discord.Interaction,button: discord.ui.Button):
        ctx.response.send_message("Sa")
    
    @discord.ui.button(label="Selam2")
    async def button(self,ctx: discord.Interaction,button: discord.ui.Button):
        ctx.response.send_message("Sa2")


class commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    

    @commands.command()
    async def komutlar(self,ctx):
        embed = discord.Embed(
            title= "Merhabalar",
            description="Bur bir denemedir.",
            color=discord.Color.green()
        )

        view = button()
        embed = view.pages[0]
        await ctx.send(embed=embed,view=view)
        
async def setup(bot):
    await bot.add_cog(commands(bot))