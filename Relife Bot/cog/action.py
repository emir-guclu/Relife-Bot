import discord
from discord.ext import commands
from discord import app_commands
import platform
import os
from cog import config
import asyncio
import random


class Action(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def tekme(self,ctx):
        embed=discord.Embed(title="Tekme Sistemi", description="Tekme atmaya çalıştınız", color=0xff52f1)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Tekme Sahibi", value=ctx.author.display_name, inline=False)
        embed.add_field(name="Sonuç",value="Tekme atılıyor...",inline=True)
        embed.set_footer(text="Vatandaş rolü ile atıldı")
        ctx2= await ctx.send(embed=embed)
        liste_tekme = ["Tekme","Yer","Kelebek",""]
        tekme = random.choices(liste_tekme)
        if tekme == ['Tekme']:
            embed.set_field_at(index=1,name="Sonuç",value="Başarılı bir şekilde Tekme attın",inline=True)
        elif tekme ==['Yer']:
            embed.set_field_at(index=1,name="Sonuç",value="Tam Tekme atacağın sıra ayağın kaydı ve yere düştün",inline=True)
        elif tekme ==['Kelebek']:
            embed.set_field_at(index=1,name="Sonuç",value="Tekme atarken önüne bir kelebek geçti ve tekmeni durdurdu",inline=True)
        else:
            embed.set_field_at(index=1,name="Sonuç",value="Karşındaki tekmeni engelledi",inline=True)
        await asyncio.sleep(2)
        await ctx2.edit(embed=embed)
    
    @commands.command()
    async def yumruk(self,ctx):
        embed=discord.Embed(title="Yumruk Sistemi", description="Yumruk atmaya çalıştınız", color=0xff52f1)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Yumruk Sahibi", value=ctx.author.display_name, inline=False)
        embed.add_field(name="Sonuç",value="Yumruk atılıyor...",inline=True)
        embed.set_footer(text="Vatandaş rolü ile atıldı")
        ctx2= await ctx.send(embed=embed)
        liste_yumruk = ["Yumruk","Boşluk","Omuz",""]
        yumruk = random.choices(liste_yumruk)
        if yumruk == ['Yumruk']:
            embed.set_field_at(index=1,name="Sonuç",value="Başarılı bir şekilde Yumruk attın",inline=True)
        elif yumruk ==['Boşluk']:
            embed.set_field_at(index=1,name="Sonuç",value="Yumruğunu salladın ama karşındakine denk gelmedi",inline=True)
        elif yumruk ==['Omuz']:
            embed.set_field_at(index=1,name="Sonuç",value="Yumruk atarken omzunu incittin",inline=True)
        else:
            embed.set_field_at(index=1,name="Sonuç",value="Karşındaki yumruğunu engelledi",inline=True)
        await asyncio.sleep(2)
        await ctx2.edit(embed=embed)
    
    @commands.command()
    async def tokat(self,ctx):
        embed=discord.Embed(title="Tokat Sistemi", description="Tokat atmaya çalıştınız", color=0xff52f1)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Tokat Sahibi", value=ctx.author.display_name, inline=False)
        embed.add_field(name="Sonuç",value="Tokat atılıyor...",inline=True)
        embed.set_footer(text="Vatandaş rolü ile atıldı")
        ctx2= await ctx.send(embed=embed)
        liste_tokat = ["Tokat","Sinek","Kafa",""]
        tokat = random.choices(liste_tokat)
        if tokat == ['Tokat']:
            embed.set_field_at(index=1,name="Sonuç",value="Başarılı bir şekilde Tokat attın",inline=True)
        elif tokat ==['Sinek']:
            embed.set_field_at(index=1,name="Sonuç",value="Karşındaki Tokatı hissetmedi bile",inline=True)
        elif tokat ==['Kafa']:
            embed.set_field_at(index=1,name="Sonuç",value="Karşındakinin kafasına sadece elinle dokundun... Ne yapıyorsun?",inline=True)
        else:
            embed.set_field_at(index=1,name="Sonuç",value="Karşındaki Tokatını engelledi",inline=True)
        await asyncio.sleep(2)
        await ctx2.edit(embed=embed)
    
    @commands.command()
    async def tükür(self,ctx):
        embed=discord.Embed(title="Tükürme Sistemi", description="Tükürmeye çalıştınız", color=0xff52f1)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Tükürük Sahibi", value=ctx.author.display_name, inline=False)
        embed.add_field(name="Sonuç",value="Tükürüyorsunuz...",inline=True)
        embed.set_footer(text="Vatandaş rolü ile atıldı")
        ctx2= await ctx.send(embed=embed)
        liste_tokat = ["Tükür","Olmadı","Yer"]
        tokat = random.choices(liste_tokat)
        if tokat == ['Tükür']:
            embed.set_field_at(index=1,name="Sonuç",value="Tam alnının ortasına Tükürdün",inline=True)
        elif tokat ==['Olmadı']:
            embed.set_field_at(index=1,name="Sonuç",value="Ağzından Tükürük çıkmadı",inline=True)
        else:
            embed.set_field_at(index=1,name="Sonuç",value="Tükürüğün yeterince hızlı değildi",inline=True)
        await asyncio.sleep(2)
        await ctx2.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(Action(bot))