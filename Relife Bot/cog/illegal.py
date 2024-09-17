import discord
from discord.ext import commands
from discord import app_commands
import platform
import os
from cog import config
import asyncio
import random
import json

class Illegal(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def çal(self,ctx,member: discord.Member,number: int):
        if (0<number<1000):
            check=0
            async for check_people in ctx.channel.history(limit=6):
                if check_people.author==member:
                    check+=1
            if (check>0):
                embed=discord.Embed(title="Çalma Sistemi", description="Etrafınızda kimse var mı diye kontrol ettin", color=0x5cabff)
                embed.set_thumbnail(url=ctx.author.avatar.url)
                embed.add_field(name="Çalma Sahibi", value=ctx.author.display_name, inline=False)
                embed.add_field(name="Sonuç", value="Çalmaya çalışıyorsun", inline=True)
                embed.set_footer(text="Vatandaş rolü ile atıldı")
                ctx2 = await ctx.send(embed=embed)
                if (0<number<501):
                    liste_cal = ["Çal","Kaç"]
                    cal = random.choices(liste_cal)
                    if cal == ['Çal']:
                    # JSON dosyasından verileri oku
                        with open('cüzdan.json', 'r') as file:
                            cüzdan = json.load(file)
                        if (cüzdan[str(member.id)]>=number):
                            embed.set_field_at(index=1,name="Sonuç",value=f"{number} Türk lirası kadar para Çaldınız")
                            cüzdan[str(ctx.author.id)] += number
                            cüzdan[str(member.id)] -= number
                        else:
                            embed.set_field_at(index=1,name="Sonuç",value=f"{member.display_name} {number} Türk lirası kadar parası yok")
                    # JSON dosyasını günceller
                        with open('cüzdan.json', 'w') as file:
                            json.dump(cüzdan, file, indent=4)

                    else:
                        embed.set_field_at(index=1,name="Sonuç",value="Parayı alamadan fark edildin")
                    await asyncio.sleep(2)
                    await ctx2.edit(embed=embed)
                
                else:
                    liste_cal = ["Çal","Kaç","Polis"]
                    cal = random.choices(liste_cal)
                    if cal == ['Çal']:
                    # JSON dosyasından verileri oku
                        with open('cüzdan.json', 'r') as file:
                            cüzdan = json.load(file)
                        if(cüzdan[str(member.id)]>=number):
                            embed.set_field_at(index=1,name="Sonuç",value=f"{number} Türk lirası kadar para Çaldınız")
                            cüzdan[str(ctx.author.id)] += number
                            cüzdan[str(member.id)] -= number
                        else:
                           embed.set_field_at(index=1,name="Sonuç",value=f"{member.display_name} {number} Türk lirası kadar parası yok") 
                    # JSON dosyasını günceller
                        with open('cüzdan.json', 'w') as file:
                            json.dump(cüzdan, file, indent=4)
                    
                    elif cal == ['Kaç']:
                        embed.set_field_at(index=1,name="Sonuç",value="Parayı alamadan fark edildin")
                    else:
                        role = ctx.guild.get_role(config.şüpheli)
                        await ctx.author.add_roles(role)
                        embed.set_field_at(index=1,name="Sonuç",value="Oralardan geçen bir polis seni fark etti. Artık daha dikkatli olmalısın")
                    await asyncio.sleep(2)
                    await ctx2.edit(embed=embed)

            else:
                await ctx.send("Parayı çalmak istediğin kişi etrafında yok... Amacın ne?")
                await asyncio.sleep(2)
                deleted = await ctx.channel.purge(limit=2)
        
        else:
            await ctx.send("Çalabileceiğiniz minumum 1 lira maximum 999 lira'dır.")
            await asyncio.sleep(2)
            deleted = await ctx.channel.purge(limit=2) 













async def setup(bot):
    await bot.add_cog(Illegal(bot))