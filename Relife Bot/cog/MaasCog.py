import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
from discord.ui import View, Button
from cog import config
import asyncio
import json

tiklama_zamanlari_vip = {}
tiklama_zamanlari_normal = {}

class MaasButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # Butonun süresi sınırsız yapılıyor
        
    @discord.ui.button(label="Özel Üye Maaşı", style=discord.ButtonStyle.primary)
    async def vip_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if any(role.id == config.özel_üye for role in interaction.user.roles):
            # Zaman kontrolü (haftada bir kez tıklama izni)
            now = datetime.now()
            last_click = tiklama_zamanlari_vip.get(interaction.user.id)

            if last_click and now - last_click < timedelta(weeks=1):
                await interaction.response.send_message("Özel üyeler için maaş butonuna haftada bir kez tıklayabilirsin.", ephemeral=True)
            else:
                tiklama_zamanlari_vip[interaction.user.id] = now
                await interaction.response.send_message("Özel üyeler için maaş alındı! 1000 Türk Lirası Banka Hesabınıza Eklendi!", ephemeral=True)
                # JSON dosyasından verileri oku
                with open('banka.json', 'r') as file:
                    banka = json.load(file)
                banka[str(interaction.user.id)] +=1000
                # JSON dosyasını günceller
                with open('banka.json', 'w') as file:
                    json.dump(banka, file, indent=4)

    @discord.ui.button(label="Normal Üye Maaşı", style=discord.ButtonStyle.secondary)
    async def normal_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Zaman kontrolü (haftada bir kez tıklama izni)
        now = datetime.now()
        last_click = tiklama_zamanlari_normal.get(interaction.user.id)
        
        if last_click and now - last_click < timedelta(weeks=1):
            await interaction.response.send_message("Normal üyeler için maaş butonuna haftada bir kez tıklayabilirsin.", ephemeral=True)
        else:
            tiklama_zamanlari_normal[interaction.user.id] = now
            await interaction.response.send_message("Normal üyeler için maaş alındı! 600 Türk Lirası Banka Hesabınıza Eklendi!", ephemeral=True)
                            # JSON dosyasından verileri oku
            with open('banka.json', 'r') as file:
                banka = json.load(file)
            banka[str(interaction.user.id)] +=600
            # JSON dosyasını günceller
            with open('banka.json', 'w') as file:
                json.dump(banka, file, indent=4)

class MaasCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send_maas_message(self):
        # Maaş embedini belirli bir kanala gönder
        kanal_id = 1285376226504085504  # Maaş kanalı ID'sini buraya girin
        kanal = self.bot.get_channel(kanal_id)

        if kanal:
            embed = discord.Embed(title="Maaş Sistemi", description="Her hafta maaşınızı almak için butonlara tıklayabilirsiniz.")
            view = MaasButton()
            await kanal.send(embed=embed, view=view)
        else:
            print("Kanal bulunamadı.")

async def setup(bot):
    await bot.add_cog(MaasCog(bot))