import discord
from discord.ext import commands
import random
from cog import config
import asyncio

class membrance(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def zar(self,ctx):
            zar = random.randint(1,20)
            embed=discord.Embed(title="Zar Sistemi", description="Aşağıda attığınız zar gözükecektir", color=0x4dff61)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="Zarın Sahibi", value=ctx.author.mention, inline=True)
            embed.add_field(name="Zar Türü", value="Normal Zar", inline=True)
            embed.add_field(name="Gelen Zar", value="Zar atılıyor...", inline=False)
            embed.set_footer(text=f"Vatandaş rolü ile atıldı.")
            ctx2 =await ctx.send(embed=embed)
            embed.set_field_at(index=2,name="Gelen Zar",value=f"**{zar}**",inline=False)
            await asyncio.sleep(2)
            await ctx2.edit(embed=embed)

    @commands.command()
    async def zarf(self,ctx):
        role = ctx.author.get_role(config.kurucu)
        if role in ctx.author.roles:
            zarf = random.randint(16,20)
            embed=discord.Embed(title="Zar Sistemi", description="Aşağıda attığınız zar gözükecektir", color=0x6fe79d)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="Zarın Sahibi", value=ctx.author.mention, inline=True)
            embed.add_field(name="Zar Türü", value="Fiziksel Zar", inline=True)
            embed.add_field(name="Gelen Zar", value="Zar atılıyor...", inline=False)
            embed.set_footer(text=f"Kurucu rolü ile atıldı.")
            ctx2 =await ctx.send(embed=embed)
            embed.set_field_at(index=2,name="Gelen Zar",value=f"**{zarf}**",inline=False)
            await asyncio.sleep(2)
            await ctx2.edit(embed=embed)
        else:
            zarf = random.randint(1,20)
            embed=discord.Embed(title="Zar Sistemi", description="Aşağıda attığınız zar gözükecektir", color=0x6fe79d)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="Zarın Sahibi", value=ctx.author.mention, inline=True)
            embed.add_field(name="Zar Türü", value="Fiziksel Zar", inline=True)
            embed.add_field(name="Gelen Zar", value="Zar atılıyor...", inline=False)
            embed.set_footer(text=f"Vatandaş rolü ile atıldı.")
            ctx2 =await ctx.send(embed=embed)
            embed.set_field_at(index=2,name="Gelen Zar",value=f"**{zarf}**",inline=False)
            await asyncio.sleep(2)
            await ctx2.edit(embed=embed)

    @commands.command()
    async def zard(self,ctx):
        role = ctx.author.get_role(config.kurucu)
        if role in ctx.author.roles:
            zard = random.randint(16,20)
            embed=discord.Embed(title="Zar Sistemi", description="Aşağıda attığınız zar gözükecektir", color=0xb0f7cb)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="Zarın Sahibi", value=ctx.author.mention, inline=True)
            embed.add_field(name="Zar Türü", value="Duygusal Zar", inline=True)
            embed.add_field(name="Gelen Zar", value="Zar atılıyor...", inline=False)
            embed.set_footer(text=f"Kurucu rolü ile atıldı.")
            embed.set_image(url="https://www.hareketligifler.net/data/media/710/zar-hareketli-resim-0012.gif")
            ctx2 =await ctx.send(embed=embed)
            embed.set_field_at(index=2,name="Gelen Zar",value=f"**{zard}**",inline=False)
            await asyncio.sleep(2)
            await ctx2.edit(embed=embed)
        else: 
            zard = random.randint(1,20)
            embed=discord.Embed(title="Zar Sistemi", description="Aşağıda attığınız zar gözükecektir", color=0xb0f7cb)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="Zarın Sahibi", value=ctx.author.mention, inline=True)
            embed.add_field(name="Zar Türü", value="Duygusal Zar", inline=True)
            embed.add_field(name="Gelen Zar", value="Zar atılıyor...", inline=False)
            embed.set_footer(text=f"Vatandaş rolü ile atıldı.")
            ctx2 =await ctx.send(embed=embed)
            embed.set_field_at(index=2,name="Gelen Zar",value=f"**{zard}**",inline=False)
            await asyncio.sleep(2)
            await ctx2.edit(embed=embed)
        
async def setup(bot):
    await bot.add_cog(membrance(bot))