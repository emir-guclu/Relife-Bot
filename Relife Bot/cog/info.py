import discord
from discord.ext import commands

class info_command(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot_version = bot.bot_version
        self.bot_name = bot.bot_name
        self.author = bot.author
        self.icon_url = bot.icon_url
        self.getDeviceOs = bot.getDeviceOs
    
    @commands.command()
    async def bilgi(self,ctx):
        embed=discord.Embed(title="Relife Türkiye RP", description="Bu bir bilgi mesajıdır.", color=0xf52424)
        embed.set_author(name="Relife Botu Bilgilendirme Metni", icon_url="https://cdn.discordapp.com/attachments/682662799457255503/687325376019824764/eg_teknolojileri2.jpg?ex=66e506e3&is=66e3b563&hm=4fc0d42a7aaf20591f066fdce8b9459d5f8a160dd300377c83f146457f493625&")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1283887730161483848/1284092783547908128/image_1-Photoroom.png?ex=66e56018&is=66e40e98&hm=f0e578b7f86aeda3ce8a01285c7494cf783b7842eb4ebb3437d17d019aa9e022&")
        embed.add_field(name="Bot ismi", value="Relife Bot", inline=False)
        embed.add_field(name="Version", value="1.0.0", inline=True)
        embed.add_field(name="Yapımcı", value="Admin.eg", inline=True)
        embed.add_field(name="İnstagram", value="@instagram.ig", inline=True)
        embed.add_field(name="Resmi Sitemiz", value="resmi site", inline=True)
        embed.add_field(name="İyi Roller dileriz", value="<3", inline=True)
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(info_command(bot))