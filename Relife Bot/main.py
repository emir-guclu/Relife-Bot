import discord
from discord.ext import commands
from discord import app_commands
import platform
import os
from cog import config
import asyncio
prefix = "!"
token=""

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=prefix, intents=discord.Intents.all(),pm_help=None, description="Relife Türkiye RP suncusunun özel botudur.")
        self.bot_version = "1.0.0"
        self.bot_name = "Relife Bot"
        self.author  = "Admin.eg"
        self.author_url = "https://cdn.discordapp.com/attachments/682662799457255503/687325376019824764/eg_teknolojileri2.jpg?ex=66e506e3&is=66e3b563&hm=4fc0d42a7aaf20591f066fdce8b9459d5f8a160dd300377c83f146457f493625&"
        self.icon_url = "https://cdn.discordapp.com/attachments/1283887730161483848/1284092783547908128/image_1-Photoroom.png?ex=66e56018&is=66e40e98&hm=f0e578b7f86aeda3ce8a01285c7494cf783b7842eb4ebb3437d17d019aa9e022&"
        self.getDeviceOs = platform.system()



    async def on_ready(self):
        await bot.change_presence(activity=discord.Game(name="Relife Rp Suncusunda rol yapıyor."))
        list_extension= []
        for filename in os.listdir("./cog"):
            if filename =="config.py":
                continue
            elif filename.endswith(".py"):
                list_extension.append("cog."+filename[:-3])
        
        for i in list_extension:
            print(i)
            await self.load_extension(i)
        maas_cog = bot.get_cog("MaasCog")
        if maas_cog:
            await maas_cog.send_maas_message()
        guild = discord.Object(id=1283878062248955975)  # Sunucu ID'sini buraya yaz
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
        print("Bot çalıştırma emri alındı.")
        print("Bot Başlatıldı...")
        print(f"Bot Name: {self.user.name}")
        print(f"Bot ID: {self.user.id}")
        print(str(len(set(self.get_all_members())))+" Kullancıya ulaşıyorum.")
        print(str(len(set(self.get_all_channels())))+" Kanala ulaşıyorum")
    

    ##async def on_command_error(self, context,exception):
        ##if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            ##await context.send(f"Bilinmeyen bir komut girdiniz. Komutlara bakmak için `{prefix}komutlar` yazın.")
        #elif isinstance (exception, discord.ext.commands.errors.BadArgument):
            #await context.send("Komudu yanlış kullandınız. **Örnek kullanımlar:** !para_çek 100,  !para_yatır 100,  !para_gönder @Emir 100")


bot= Bot()
@bot.tree.command(name="yenile",description="Bu botu kapatmadan sayfayı güncellemeni sağlar")
async def yenile(ctx: discord.Interaction, value: str):
    role = ctx.guild.get_role(config.kurucu)
    if role in ctx.user.roles:
        await bot.unload_extension("cog."+value)
        await bot.load_extension("cog."+value)
        await ctx.response.send_message(f"{value} Sayfası Yenilendi...")
    else:
        await ctx.response.send_message(f"Bu komudu kullanamazsın")
bot.run(token=token)