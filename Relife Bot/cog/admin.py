import discord
from discord.ext import commands
from cog import config
import asyncio
from discord import app_commands
class admin_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        ##@self.bot.tree.command()
        
    @commands.command(hidden= True)
    async def kick(self,ctx, member: discord.Member, *,reason=None):
        admin = member.guild.get_role(config.kurucu)
        if (admin in ctx.author.roles):
            await member.kick()
            await ctx.send(f"""**{member.display_name}** Sunucudan Atıldı.
                        **Reason: **{reason}""")
        else:
            await ctx.send("Bu komudu kullanmazsınız!")
    @commands.command(hidden= True)
    async def ban(self,ctx, member: discord.Member, *,reason=None):
        admin = member.guild.get_role(config.kurucu)
        if (admin in ctx.author.roles):
            await member.ban()
            await ctx.send(f"""**{member.display_name}** Sunucudan Atıldı.
                        **Reason: **{reason}""")
        else:
            await ctx.send("Bu komudu kullanmazsınız!")
        
    @commands.command(hidden= True,alliases=['Clear'])
    async def sil(self, ctx, sayi: int):
        admin = ctx.author.get_role(config.kurucu)
        if (admin in ctx.author.roles):
            if (0<sayi<100):
                ctx2 = await ctx.send(f"{sayi} mesaj siliniyor...")
                deleted = await ctx.channel.purge(limit=sayi+2, check=lambda msg: msg != ctx2)
                await ctx2.edit(content=f"Mesajlar başarılı bir şekilde silinmiştir. :white_check_mark:",delete_after=1.3)
            else:
                await ctx.send("Sadece 1 ile 99 arasında mesaj silebilirsiniz!",delete_after=1.3)
        else:
            await ctx.send("Bu komutu kullanmaya yetkiniz yok.")

async def setup(bot):
    await bot.add_cog(admin_commands(bot))