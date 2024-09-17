import discord
from discord.ext import commands
from cog import config
import asyncio

class Message(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        


    @commands.command()
    async def mesaj(self, ctx, member: discord.Member):
        telefon = ctx.author.get_role(config.telefon)
        if telefon in ctx.author.roles:
            if ctx.author.id != member.id:
                kategori = ctx.guild.get_channel(config.özel_mesaj_kategorisi)
                kanal_ismi = f"{ctx.author.display_name} ve {member.display_name} Telefon mesajı kanalı"
                check_kanal = discord.utils.get(ctx.guild.text_channels,name=kanal_ismi)
                if (check_kanal is False):
                    kanal = await ctx.guild.create_text_channel(kanal_ismi, category=kategori)

                    overwrites = {
                        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),  # Herkesten görünürlüğü kaldır
                        member: discord.PermissionOverwrite(view_channel=True),  # Belirtilen üyeye görünür yap
                        ctx.author :discord.PermissionOverwrite(view_channel=True) 
                    }
                    print(kanal)
                    await kanal.edit(overwrites=overwrites)
                    await kanal.send(f"{ctx.author.mention} and {member.mention}")
                else:
                    await ctx.send(f"Bu kanal zaten var.")
                    await asyncio.sleep(2)
                    deleted = await ctx.channel.purge(limit=2)

            else:
                await ctx.send(f"Kendinize mesaj gönderemezsiniz")
                await asyncio.sleep(2)
                deleted = await ctx.channel.purge(limit=2)      
        else:
            await ctx.send(f"Bu komudu kullanmanız için Telefonunuz olmalı")
            await asyncio.sleep(2)
            deleted = await ctx.channel.purge(limit=2)


async def setup(bot):
    await bot.add_cog(Message(bot))