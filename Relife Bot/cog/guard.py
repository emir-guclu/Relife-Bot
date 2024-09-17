import discord
from discord.ext import commands
from cog import config
import random
import asyncio

class Guard(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    
    @commands.command() 
    async def tutukla(self, ctx,member: discord.Member):
        role = ctx.author.get_role(config.polis)
        liste_tutukla= ["Tutuklandı","Kaçtı","Tutuklanabilir"]
        if role in ctx.author.roles:
            if role in member.roles:
                await ctx.send("Başka Bir Polisi Tutuklayamazsın")
                await asyncio.sleep(2)
                deleted = await ctx.channel.purge(limit=2)
            else:
                embed=discord.Embed(title="Tutukla Sistemi", description="Aşağıda Tutuklanma işlemine ait bilgiler bulunuyor", color=0xc800ff)
                embed.set_thumbnail(url=ctx.author.avatar.url)
                embed.add_field(name="Tutuklanın Sahibi", value=ctx.author.mention, inline=True)
                embed.add_field(name="Tutuklanmak istenen", value=member.mention, inline=True)
                embed.add_field(name="Sonuç", value="Sonuç bekleniyor...", inline=False)
                embed.set_footer(text=f"Polis rolü ile atıldı. Eğer Polis hemen arkandaysa zarf atmadan !kaç komutunu kullan")
                ctx2 =await ctx.send(embed=embed)
                tutukla= random.choices(liste_tutukla)
                if tutukla == ['Tutuklandı']:
                    embed.set_field_at(index=2,name="Sonuç",value=f"**Tutuklama başarılı**",inline=False)
                    if config.suçlu not in member.roles:
                        role2= ctx.guild.get_role(config.suçlu)
                        await member.add_roles(role2)

                elif tutukla == ['Kaçtı']:
                    kacti= random.choices(liste_tutukla)
                    if kacti == ['Kaçtı']:
                        embed.set_field_at(index=2,name="Sonuç",value=f"{ctx.author.display_name} ayakkabısını bağlamayı unuttuğundan yere düştü",inline=False)
                    elif kacti == ['Tutuklandı']:
                        embed.set_field_at(index=2,name="Sonuç",value=f"{ctx.author.display_name} az farkla mahkumu elinden kaçırdın",inline=False)
                    else:
                        embed.set_field_at(index=2,name="Sonuç",value=f"{ctx.author.display_name} {member.display_name} senden çok daha hızlı koştu",inline=False)
                else:
                    embed.set_field_at(index=2,name="Sonuç",value=f"{member.display_name} Polis hemen arkanda çabuk bir şeyler yap",inline=False)
                await asyncio.sleep(2)
                await ctx2.edit(embed=embed)
        else:
            await ctx.send("Bu komudu sadece Polisler Kullanabilir")
            await asyncio.sleep(2)
            deleted = await ctx.channel.purge(limit=2)

    @commands.command()
    async def kaç(self,ctx):
        liste_kac = ["Kaçtı","Kaçamadı"]
        embed=discord.Embed(title="Kaçma Sistemi", description="Aşağıda Kaçma işlemine ait bilgiler bulunuyor", color=0xc800ff)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Kaçmaya çalışan kişi", value=ctx.author.mention, inline=False)
        embed.add_field(name="Sonuç", value="Sonuç bekleniyor...", inline=False)
        embed.set_footer(text=f"Vatandaş rolü ile atıldı.")
        ctx2 = await ctx.send(embed=embed)
        kac = random.choices(liste_kac)
        kac2 = random.choices(liste_kac)
        if kac == ['Kaçtı']:
            embed.set_field_at(index=1,name="Sonuç",value="Başarılı bir şekilde kaçtınız")
        else:
            if kac2 == ['Kaçtı']:
                embed.set_field_at(index=1,name="Sonuç",value="Bir kelebek dikkatini dağıttı için kaçamadın")
            else:
                embed.set_field_at(index=1,name="Sonuç",value="Atletik yetenklerini geliştir... Başarısız oldun")
        await asyncio.sleep(2)
        await ctx2.edit(embed=embed)

    #@commands.command()
    #async def yakala(self,ctx):
        #embed=discord.Embed(title="Tutukla Sistemi", description="Aşağıda Tutuklanma işlemine ait bilgiler bulunuyor", color=0xc800ff)
        #embed.set_thumbnail(url=ctx.author.avatar.url)
        #embed.add_field(name="Kaçmaya çalışan kişi", value=ctx.author.mention, inline=True)
        #embed.add_field(name="Sonuç", value="Sonuç bekleniyor...", inline=False)
        #embed.set_footer(text=f"Vatandaş rolü ile atıldı.")
        #ctx2 =await ctx.send(embed=embed)
        #liste_yakala = ["Yakaladı","Yakalayamadı",""]

async def setup(bot):
    await bot.add_cog(Guard(bot))