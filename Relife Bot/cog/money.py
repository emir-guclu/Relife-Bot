import discord
from discord.ext import commands
import random
from cog import config
##from cog import banka
##from cog import cüzdan
import asyncio
import json

class bank_account(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(hidden= True)
    async def banka1(self,ctx,member: discord.Member):
        if (ctx.channel.id in config.admin_room):
            admin = ctx.author.get_role(config.kurucu)
            if (admin in ctx.author.roles):
                # JSON dosyasından verileri oku
                with open('banka.json', 'r') as file:
                    banka = json.load(file)

                embed=discord.Embed(title="Banka Hesabınıza Hoş Geldiniz", description="Aşağıda Bilgileriniz Bulunuyor")
                embed.set_thumbnail(url=member.avatar)
                embed.add_field(name="Kullanıcı Adı", value=member.display_name, inline=False)
                embed.add_field(name="Şifre", value=member.id, inline=True)
                embed.add_field(name="Para Miktarı", value=banka[str(member.id)], inline=True)
                embed.add_field(name="Tekrar bekleriz", value="<3", inline=True)
                await ctx.send(embed=embed)

                with open('banka.json', 'w') as file:
                    json.dump(banka, file, indent=4)
            else:
                await ctx.send("Sen kimsin ne arıyorsun burada?")
                print("Kaçak tespit edildi... Gerekli işlemleri yap.")
        else:
            await ctx.send(f"Bu komutu burada kullanamazsınız. Lütfen en yakın admin_room'a gidiniz.")
    @commands.command()
    async def banka(self,ctx,):
        if (ctx.channel.id in config.banka_kanal_id):
            # JSON dosyasından verileri oku
            with open('banka.json', 'r') as file:
                banka = json.load(file)
            if str(ctx.author.id) not in banka:
                banka[str(ctx.author.id)] = 0
            
            #Ekrana Bankayı bastırır
            embed=discord.Embed(title="Banka Hesabınıza Hoş Geldiniz", description="Aşağıda Bilgileriniz Bulunuyor",color=0x05ffac)
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="Kullanıcı Adı", value=ctx.author.display_name, inline=False)
            embed.add_field(name="Şifre", value=ctx.author.id, inline=True)
            embed.add_field(name="Para Miktarı", value=str(banka[str(ctx.author.id)])+" TL", inline=True)
            embed.add_field(name="Tekrar bekleriz", value="<3", inline=True)
            embed.set_image(url="https://cdn.discordapp.com/attachments/1284146595306410056/1284558264218030204/Screenshot_20240914-194746.png?ex=66e7119c&is=66e5c01c&hm=0b9eb0872b43260f867544abb21a7e7f6f2151fa78f9ce2dd4f0fff451b25ef4&")
            await ctx.send(embed=embed)

            #JSON dosyasının verilerini günceller
            with open('banka.json', 'w') as file:
                json.dump(banka, file, indent=4)
    
        else:
            await ctx.send(f"Bu komutu burada kullanamazsınız. Lütfen en yakın ATM'ye gidiniz.")
    @commands.command()
    async def cüzdan(self,ctx):
        # JSON dosyasından verileri oku
        with open('cüzdan.json', 'r') as file:
            cüzdan = json.load(file)
            if str(ctx.author.id) not in cüzdan:
                cüzdan[str(ctx.author.id)] = 0

        #Ekrana Cüzdanı bastırır
        embed=discord.Embed(title="Cüzdanını açtın", description="Cüzdanın üzerinde bilgilerin var",color=0x2b00ff)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Cüzdanın üzerinde yazan isim", value=ctx.author.display_name, inline=False)
        embed.add_field(name="Para Miktarı", value=str(cüzdan[str(ctx.author.id)])+" TL", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1284146595306410056/1284558263773429801/Screenshot_20240914-194904.png?ex=66e7119c&is=66e5c01c&hm=c07eb00ab1ac91f3f76ca2df6de233e4551262b47894a91e156f6387e550ccea&")
        await ctx.send(embed=embed)

        #JSON dosyasının verilerini günceller
        with open('cüzdan.json', 'w') as file:
            json.dump(cüzdan, file, indent=4)

    @commands.command()
    async def para_çek(self, ctx, number: int):
        if (ctx.channel.id in config.banka_kanal_id):
        # JSON dosyasından verileri oku
            with open('banka.json', 'r') as file:
                banka = json.load(file)
    
            with open('cüzdan.json', 'r') as file:
                cüzdan = json.load(file)

    # Kullanıcının bankasında yeterli miktarda para olup olmadığını kontrol et
            if banka.get(str(ctx.author.id), 0) >= number:
            # Para çekme işlemi
                ctx2 = await ctx.send(f"{number} Türk lirası çekiliyor...")
                await asyncio.sleep(1)  # Asenkron uyku

            # Banka ve cüzdan verilerini güncelle
                banka[str(ctx.author.id)] -= number
                cüzdan[str(ctx.author.id)] += number

            # Güncellenmiş verileri JSON dosyasına yaz
                with open('banka.json', 'w') as file:
                    json.dump(banka, file, indent=4)
        
                with open('cüzdan.json', 'w') as file:
                    json.dump(cüzdan, file, indent=4)

                await ctx2.edit(content=f"Cüzdanına {number} Türk lirası eklendi.")
            else:
                await ctx.send(f"Bankanda {number} Türk lirası kadar paran bulunmuyor.")
        else:
            await ctx.send(f"Bu komutu burada kullanamazsınız. Lütfen en yakın ATM'ye gidiniz.")

    @commands.command()
    async def para_yatır(self, ctx, number: int):
        if (ctx.channel.id in config.banka_kanal_id):
        # JSON dosyasından verileri oku
            with open('banka.json', 'r') as file:
                banka = json.load(file)
    
            with open('cüzdan.json', 'r') as file:
                cüzdan = json.load(file)
    
        # Kullanıcının bankasında yeterli miktarda para olup olmadığını kontrol et
            if cüzdan.get(str(ctx.author.id), 0) >= number:
            # Para çekme işlemi
                ctx2 = await ctx.send(f"{number} Türk lirası yatırılıyor...")
                await asyncio.sleep(1)  # Asenkron uyku

            # Banka ve cüzdan verilerini güncelle
                cüzdan[str(ctx.author.id)] -= number
                banka[str(ctx.author.id)] += number

            # Güncellenmiş verileri JSON dosyasına yaz
                with open('banka.json', 'w') as file:
                    json.dump(banka, file, indent=4)
        
                with open('cüzdan.json', 'w') as file:
                    json.dump(cüzdan, file, indent=4)

                await ctx2.edit(content=f"Banka hesabına {number} Türk lirası eklendi.")
            else:
                await ctx.send(f"Cüzdanında {number} Türk lirası kadar paran bulunmuyor.")
        else:
            await ctx.send(f"Bu komutu burada kullanamazsınız. Lütfen en yakın ATM'ye gidiniz.")

    @commands.command()
    async def para_gönder(self,ctx,member : discord.Member, number: int):
        if ctx.channel.id in config.banka_kanal_id:
        # JSON dosyasından verileri oku
            with open('banka.json', 'r') as file:
                banka = json.load(file)
            
            #Para gönderme bilgilerini ekrana yazdırır
            if banka.get(str(ctx.author.id), 0) >= number:
                if ctx.author.id == member.id:
                    await ctx.send("Kendinize Para Gönderemezsiniz.")
                else:
                    embed=discord.Embed(title="Banka Hesabınıza Hoş Geldiniz", description="Aşağıda Bilgileriniz Bulunuyor",color=0xeeff00)
                    embed.set_thumbnail(url=ctx.author.avatar.url)
                    embed.add_field(name="Kullanıcı Adı", value=ctx.author.display_name, inline=False)
                    embed.add_field(name="Parayı  Gönderdiğiniz kişi", value=member.display_name, inline=True)
                    embed.add_field(name="Para Miktarı", value=str(number)+" TL", inline=True)
                    embed.add_field(name="Tekrar bekleriz", value="<3", inline=True)
                    await ctx.send(embed=embed)
                    banka[str(ctx.author.id)] -= number
                    banka[str(member.id)] += number
            else:
                await ctx.send(f"Bankanızda {number} Türk lirası kadar paranız bulunmuyor.")

        # JSON dosyasını günceller
            with open('banka.json', 'w') as file:
                    json.dump(banka, file, indent=4)
        else:
            await ctx.send(f"Bu komutu burada kullanamazsınız. Lütfen en yakın ATM'ye gidiniz.")

    #@commands.Cog.listener()
    #async def on_command_error(self, context,exception):
        #if isinstance (exception, discord.ext.commands.errors.BadArgument):
            #await context.send("Komudu yanlış kullandınız. **Örnek kullanımlar:** !para_çek 100,  !para_yatır 100,  !para_gönder @Emir 100")

async def setup(bot):
    await bot.add_cog(bank_account(bot))