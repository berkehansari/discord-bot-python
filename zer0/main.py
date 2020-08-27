import discord
from discord.ext import commands
import logging
from pathlib import Path
import json
import platform
import asyncio
import random
import googletrans
from googletrans import Translator
import os
import veriler
import time
import sunucuverileri
from itertools import cycle
from urllib.request import Request, urlopen
from discord import File
import requests
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import io
from discord import FFmpegPCMAudio
from os import system



cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"(cwd)\n-----")


url='https://i.ibb.co/mFm1Dwn/sas42.png'
url2='https://i.ibb.co/9nbwvVp/lvexp.png'
response = urlopen(url)
background_image = Image.open(response)
background_image = background_image.convert('RGBA')

response2 = urlopen(url2)
background_image2 = Image.open(response2)
background_image2 = background_image2.convert('RGBA')


songs = asyncio.Queue()
play_next_song = asyncio.Event()






bot = commands.Bot(command_prefix='/', case_insensitive=True)
bot.config_token = "tokeninizi girin."
logging.basicConfig(level=logging.INFO)


reklamlar = ['https','http','.com','.gg','.net','.org','.xyz','www']
status = ['/yardım ile komutlarımı görebilirsin', '/bilgi ile detaylarımı öğrenebilirsin', 'Ben Poe, sana yardımcı olmakla meşgulüm.']
küfürler = ['amk','ananı','4n4n1','4nanı','an4nı','anani','anan1','aamk','amkkk','amkk','ammq','amq','aq','aQ','AQ','amQ','a q','a m k','a m q','A m q', 'A M Q', 'aamkk','aammk','ANAN','orosbu','oç','oÇ','0ç','sik','Sik','sık','SIK','SİK','çük','ÇÜK','annene','anana','sokuyum','Piç','Oç','Sokayım','Sikeyim','Koyayım','Amk','Amq','penis','Penis','Vajina','vajina','Pezevenk','Orospu','Ananı','Anan','Amına','AMINA','amına','Amm','AMMına','AMMINA','AMMIINNA','anana','Sikeyim','Yarram','YARRA','yarra','yarrak','YARRAK','yarram','YARRAM','yARRAM','yaRRam','Sokuk','Sikik','sokuk','sikik','SOKUK','SİKİK','aptal','Aptal','salak','Salak','SALAK','APTAL','OROSBU','ÇOCU','Çocu','çocu','aq','amk','iBine','İbine','İBNE','ANAN','ANANI','ananı','İBİNE','İBNE','İPNE','ibne','ipne','yavşak','YAŞVAK','Yavşak','s2k','Oç','amına','Amına','Orosbu','Orusbu','Orspu','evladı','koyum','anan','am1na','4m1na','piç','pic','p1ç','Piç','PİC','PIC','orospu','0rospu','ibne','amcık','amçuk','ibine','1bne','1bn3','pezevenk','pezemek','pezemenk','pezo','pez0','p3z3v3nk','fuck','zina','cima','Pezevenk','Pezo','İbne','İbine','Piç','Amcık','Amına','Orospu','Orosbu','yarram','yaarraam','yaaarraaamm','yarraaam','Yarram','y4rr4m','oç', 'ananıskm','anaskm','amına','ananısikim','ananakoyum','anneni sik','anneni sikiyim', 'sikiyim', 'sokuyum','sokayım','SOKAYIM','SOKUYUM','SİKİYİM','valideni','valideciğini','kodumun','koyduğum','KOYDUĞUM']


@bot.event
async def on_ready():
    print(f"-----\nGiriş yapıldı {bot.user.name} olarak : {bot.user.id}\n-----\nKullanım prefix'i '/'\n-----")
    #await bot.change_presence(activity=discord.Game(name=f"Ben Poe, sana yardımcı olmakla meşgulüm."))
    

@bot.command()
@commands.is_owner()
async def istatistik(ctx):

    pythonVersion = platform.python_version()
    serverCount = len(bot.guilds)
    memberCount = len(set(bot.get_all_members()))
    await ctx.send(f"Bi'bakayım, {serverCount} tane Sunucuda toplam {memberCount} kullanıcıya ulaşıyorum. Vhagar beni Python {pythonVersion} ile yazdı.")    

@bot.event
async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)
    print(type(next(msgs)))

    while bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(5)


@bot.command()
async def çeviri(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(a.text)

@bot.command()
async def dolar(ctx):
    r = requests.get("https://www.bloomberght.com/")
    soup = BeautifulSoup(r.content,"html.parser")
    veri = soup.find_all('span', attrs={'class':'LastPrice'})
    dolar = veri[1].text 
    await ctx.send("1 Dolar = {} TL ".format(dolar))   
  


@bot.command()
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def duyuruyap(ctx, *, message=None):

    message = message or "Lütfen bir şeyler söyle."
    await ctx.message.delete()
    await ctx.send("@everyone "+ message)

@bot.command(aliases=['disconnect', 'close', 'stopbot'])
@commands.is_owner()
async def kapat(ctx):
    await ctx.send(f"{ctx.author.mention} Beni kapattı, gidiyorum :wave:")
    await bot.logout()    

@kapat.error
async def logout_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Üzgünüm, beni kapatabilecek kadar kudretli değilsin.")
    else:
        raise error    

@bot.command(pass_context=True)
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def rolver(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.name} tarafından, {user.name} adlı kişiye rol verildi. ")   


@bot.command()
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def otorol(ctx, role:discord.Role):
    guild = ctx.guild
    try:
        sunucuverileri.set_otorol(guild, role)
        await ctx.send("Otorol {} olarak belirlendi.".format(role))
    except:
        await ctx.send("Bi'şeyi yanlış yaptın.")

@bot.command()
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def otorolkaldır(ctx, role:discord.Role):
    guild = ctx.guild
    try:
        sunucuverileri.set_otorol(guild, role, 0)
        await ctx.send("Otorol {} kaldırıldı.".format(role))
    except:
        await ctx.send("Bi'şeyi yanlış yaptın.")        
    
@bot.event
async def on_member_join(member): #ctx.author
    guild = member.guild
    channelID = sunucuverileri.get_channel(guild)  
    if channelID != None or channelID != "0":
        channel = bot.get_channel(channelID)
        if channel:
            await channel.send("Ve sonra.. Gökler onu verdi {}. Selam olsun!".format(member.mention))
            #buraya botun kullanım tanıtımı eklenebilir. embed
            AVATAR_SIZE = 128
            image = background_image.copy()
            image_width, image_height = image.size

            rect_x0 = 20
            rect_y0 = 20

            rect_x1 = image_width - 20
            rect_y1 = 20 + AVATAR_SIZE - 1

            rect_width = rect_x1 - rect_x0
            rect_height = rect_y1 - rect_y0

            rectangle_image = Image.new('RGBA', (image_width, image_height))
            rectangle_draw = ImageDraw.Draw(rectangle_image)

            rectangle_draw.rectangle((rect_x0, rect_y0, rect_x1, rect_y1), fill=(255,0,0, 0))
            
            image = Image.alpha_composite(image, rectangle_image)
            draw = ImageDraw.Draw(image)

            text = f'{member.display_name}'
            #yazının fontu ve boyutu.
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 78)
            #font = ImageFont.truetype("arial.ttf", 78)

            text_width, text_height = draw.textsize(text, font=font)
            x = (rect_width - text_width - AVATAR_SIZE)//2
            y = (rect_height - text_height)//2

            #yazının x eksen
            x += rect_x0 + 60
            #yazının y eksen kısmı, aşağı için +
            y += rect_y0 + 330
            draw.text((x-2, y), text, font=font, fill=(0,0,0,0))
            draw.text((x+2, y), text, font=font, fill=(0,0,0,0))
            draw.text((x, y-2), text, font=font, fill=(0,0,0,0))
            draw.text((x, y+2), text, font=font, fill=(0,0,0,0))
            draw.text((x, y), text, fill=(255,255,0), font=font)

            avatar_asset = member.avatar_url_as(format='jpg', size=AVATAR_SIZE)
            buffer_avatar = io.BytesIO(await avatar_asset.read())
            avatar_image = Image.open(buffer_avatar)
            avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))

            circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
            circle_draw = ImageDraw.Draw(circle_image)
            #avatar boyutu
            circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)

            #avatarın konumu
            image.paste(avatar_image, (rect_x0 + 558, rect_y0 + 100), circle_image)


            buffer_output = io.BytesIO()
            image.save(buffer_output, format = 'PNG')
            buffer_output.seek(0)
            #embed mesaj şeklinde gönder genel bilgileri de yaz içine
            embed=discord.Embed(title="Ben Poe Bot, Sana yardımcı olmak için her zaman buradayım.", description="Öncelikle Prefix'im '/', komutlarımı kullanırken / ile başlamalısın.", color=0x5a44ca)
            embed.set_author(name="Hoşgeldin {}".format(member.display_name))
            embed.add_field(name=":star2: Bilgilendirme;", value="Merhaba {}, bu sunucuda diğer insanlara karşı saygılı olmalısın. Sunucu ve kanal kurallarına uymalısın. Eğer bu Sunucu'da herhangi bir kural yoksa, hmm işte o zaman sorun yok demektir. Kuralları öğrenmek için, açılmış olan Kurallar kanalına göz atabilir, halihazırda böyle bir kanal yoksa Sunucu yetkililerine sorabilirsin.               İyi eğlenceler dilerim.".format(member.mention), inline=False)
            embed.add_field(name=":sparkles: /yardım", value="Bu komutu kullanarak, basitçe benim sahip olduğum tüm özelliklere ulaşabileceksin. ", inline=False)
        
            embed.add_field(name=":sparkles: /bilgi", value="Bu komutu kullanarak, Poe Bot hakkında detaylara ulaşabilirsin, aynı zamanda Bot ile ilgili bir sorun oluşursa yine bu komutu kullanarak Destek Sunucumuza ulaşabilirsin. ", inline=False)
            embed.add_field(name=":zap: Bot Destek Sunucusu", value="[[DestekSunucusu]](https://discord.gg/wZW56ZV)")
            embed.set_footer(text="Developer: Vhagar#2837")                     
            embed.set_image(url='attachment://myimage.png')

            await channel.send(embed=embed, file=File(buffer_output, 'myimage.png'))        


    roleID = sunucuverileri.get_otorol(member.guild)
    if roleID != None or roleID != '0':
        role = member.guild.get_role(roleID)
        if role:
            await member.add_roles(role)

    with open('users.json','r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json','w') as f:
        json.dump(users, f, indent=4)          


@bot.command(name='rank')
async def rank(ctx, member:discord.Member):
            #member ismi girilmeden gösterebilir.
            AVATAR_SIZE = 128
            image = background_image2.copy()
            image_width, image_height = image.size

            rect_x0 = 20
            rect_y0 = 20

            rect_x1 = image_width - 20
            rect_y1 = 20 + AVATAR_SIZE - 1

            rect_width = rect_x1 - rect_x0
            rect_height = rect_y1 - rect_y0

            rectangle_image = Image.new('RGBA', (image_width, image_height))
            rectangle_draw = ImageDraw.Draw(rectangle_image)

            rectangle_draw.rectangle((rect_x0, rect_y0, rect_x1, rect_y1), fill=(255,0,0, 0))
            
            image = Image.alpha_composite(image, rectangle_image)
            draw = ImageDraw.Draw(image)

            text = f'{veriler.lv_come(member)}'
            text2 = f'{veriler.exp_come(member)}'
            text3 = f'{member.display_name}'
            #yazının fontu ve boyutu.
            
            #font = ImageFont.load_default()
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 78)
            print(font)

            text_width, text_height = draw.textsize(text, font=font)
            x = (rect_width - text_width - AVATAR_SIZE)//2
            y = (rect_height - text_height)//2

            #yazının x eksen
            x += rect_x0 - 265
            #yazının y eksen kısmı, aşağı için +
            y += rect_y0 + 450


            x1 = (rect_width - text_width - AVATAR_SIZE)//2
            y1 = (rect_height - text_height)//2
            x1 += rect_x0 - 250
            y1 += rect_y0 + 160
            draw.text((x-2, y), text, font=font, fill=(0,0,0,0))
            draw.text((x+2, y), text, font=font, fill=(0,0,0,0))
            draw.text((x, y-2), text, font=font, fill=(0,0,0,0))
            draw.text((x, y+2), text, font=font, fill=(0,0,0,0))
            draw.text((x, y), text, fill=(255,255,0), font=font)
            draw.text((x-605, y), text2, font=font, fill=(0,0,0,0))
            draw.text((x+609, y), text2, font=font, fill=(0,0,0,0))
            draw.text((x+607, y-2), text2, font=font, fill=(0,0,0,0))
            draw.text((x+607, y+2), text2, font=font, fill=(0,0,0,0))
            draw.text((x+607,y), text2, fill=(255,255,0), font=font)
            draw.text((x1,y1), text3, font=font, fill=(255,255,0))
            

            avatar_asset = member.avatar_url_as(format='jpg', size=AVATAR_SIZE)
            buffer_avatar = io.BytesIO(await avatar_asset.read())
            avatar_image = Image.open(buffer_avatar)
            avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))

            circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
            circle_draw = ImageDraw.Draw(circle_image)
            #avatar boyutu
            circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)

            #avatarın konumu
            image.paste(avatar_image, (rect_x0 + 560, rect_y0 + 8), circle_image)


            buffer_output = io.BytesIO()
            image.save(buffer_output, format = 'PNG')
            buffer_output.seek(0)

            await ctx.send(file=File(buffer_output, 'myimage2.png')) 
       

@bot.command()
async def yardım(ctx):
    embed=discord.Embed(title="|Merhaba ben Poe", description="Öncelikle, komutlara tam erişim sağlayabilmek için, lütfen kanalda bir mesajın olduğundan emin ol. ", color=0x61dfff)
    embed.set_author(name="/yardım 'a hoşgeldin!")
    embed.add_field(name="=> :wrench: Admin Komutları", value=":sparkles: `/adminyardım` | Bot'u sunucuna ayarlayabilmen için gerekli talimatlar özel mesaj olarak gelecek.", inline=False)
    embed.add_field(name="=> :tada: Eğlence Komutları", value=":sparkles: `/eğlence` | Eğlence komutlarına göz atmak için.", inline=False)
    embed.add_field(name="=> :mag_right: Genel Komutlar", value=":sparkles: `/genel` | Burada senin için pek çok komutum var. ", inline=False)
    embed.add_field(name="=> :robot: Bot Özel", value=":sparkles: `/bilgi` | Bot'a dair bilgiler, Destek Sunucusu gibi şeylere ulaşabilirsin.", inline=False)
    embed.set_footer(text="Sana yardımcı olmak için hep buradayım.")
    embed.set_image(url='https://i.pinimg.com/originals/95/01/cd/9501cd7cee2c36047ae4aa94a95d555e.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/app-icons/733681967631171625/34d299a39e099f919547380b70721ae5.png?size=64')
    await ctx.send(embed=embed)

@bot.command()
async def adminyardım(message):
    embed=discord.Embed(title="|Ben Poe", description="Sunucundaki eksikleri güvenli bir şekilde giderebilmen ve kullanıcılarına daha iyi destek verebilmen amacıyla geliştirildim. Aşağıdaki komutlar ile Sunucunu ayarlayacağız. Ban-sustur-at komutları dışındaki komutlar genel olarak `yönetici ve rolleri yönetme` yetkilerine ihtiyaç duyar.", color=0xf00060)
    embed.set_author(name="Merhaba Admin")
    embed.add_field(name=":star2: /kanalbelirle #kanaladı", value="Kullanıcılar Sunucuna girdiğinde hoş karşılanmaları için, bir hoşgeldin kanalı belirlemeliyiz.", inline=False)
    embed.add_field(name=":sparkles: /otorol Roladı", value="Sunucuya yeni katılan üyelere verilen rolü belirler. Rol isminin tek kelime olmasına dikkat etmelisin. `(Rolün ismini birebir yazmalısın!)`", inline=False)
    embed.add_field(name=":star2: /otorolkaldır", value="Yanlış bir otorol ayarladıysan diye böyle bir komutum var.", inline=True)
    embed.add_field(name=":sparkles: /sustur @isim", value="İstediğin kişiyi susturursun, hiçbir yazı yazamaz.", inline=False)
    embed.add_field(name=":star2: /susturma @isim", value="Kişi artık tekrar konuşabilir.", inline=True)
    embed.add_field(name=":sparkles: /ban @isim", value="`Bu işlem geri alınamaz.` Kişi sunucudan temelli şutlanır.", inline=False)
    embed.add_field(name=":star2: /at @isim", value="Kişi sunucudan atılır, fakat geri gelebilir.", inline=False)
    embed.add_field(name=":sparkles: /rolver @isim Roladı", value="Kişiye seçtiğin rolü verirsin. `(Rolün ismini birebir yazmalısın!)`", inline=False)
    embed.add_field(name=":star2: /anket anket-adı anket-içeriği #kanaladı", value="Bir anket başlatırsın. `(anket-adı ve içerik kısmında boşluk bırakmamalısın, bunun yerine '-' kullan!)`", inline=False)
    embed.add_field(name=":sparkles: /küfürengelle", value="Artık Sunucunda küfür edilmesi gerçekten çok zor bir hale gelir. Küfürler anında silinir. `(Adminler hariç)`", inline=False)
    embed.add_field(name=":star2: /küfürengellekapat", value="Artık küfür edilebilir.", inline=True)
    embed.add_field(name=":sparkles: /reklamengelle", value="Sunucunda Link paylaşılması yasaklanır. Link içeren mesajlar silinir. `(Adminler hariç)`", inline=False)
    embed.add_field(name=":star2: /reklamengellekapat", value="Artık Link paylaşılabilir.", inline=True)
    embed.add_field(name=":sparkles: /duyuruyap", value="Basitçe bir duyuru yaparsın.", inline=True)
    embed.add_field(name=":shield: Destek Sunucusu", value="[Tıkla](https://discord.gg/fTqjyDk)", inline=False)
    embed.add_field(name=":sparkling_heart: Oy Ver", value="[Tıkla](https://top.gg/bot/733681967631171625)",inline=False)
    embed.set_footer(text="Sana yardımcı olmak için hep buradayım.")
    await message.author.send(embed=embed)

@bot.command()
async def genel(ctx):
    embed=discord.Embed(title="--------------------", description="`( ) parantezleri koymayınız.`", color=0x2f56ca)
    embed.set_author(name="Genel Komutlar")
    embed.add_field(name=":sleeping: `/afk` `(sebep)`", value="Birisi sizi etiketlediğinde AFK olduğunuzu ve nedenini yazar.", inline=True)
    embed.add_field(name=":slight_smile: `/afkboz`", value="AFK durumundan çıkarsınız.", inline=True)
    embed.add_field(name=":crown: `/kullanıcı` `@isim`", value="Belirlediğiniz kullanıcının bilgilerini gösterir.", inline=True)
    embed.add_field(name=":chart_with_upwards_trend: `/rank` `@isim`", value="Belirlediğiniz kullanıcının Level ve Experience bilgilerini gösterir.", inline=True)
    embed.add_field(name=":dollar: `/dolar`", value="Dolar'ı Türk Lirasına çevirir.", inline=True)
    embed.add_field(name=":printer: `/çeviri` `(tr)` `(cümle)`", value="Cümleyi Türkçe'ye çevirir. (tr yerine en yazıp Türkçe cümleyi İngilizce'ye de çevirebilirsiniz.)", inline=True)
    embed.add_field(name=":grey_question: `/yardım`", value="Yardım Menüsünü açar.", inline=True)
    embed.set_footer(text="Sana yardımcı olmak için hep buradayım.")
    await ctx.send(embed=embed)

@bot.command()
async def eğlence(ctx):
        embed=discord.Embed(title="--------------------", description="`( ) parantezleri koymayınız.`", color=0xf2e126)
        embed.set_author(name="Eğlence Komutları")
        embed.add_field(name=":gun: `/vur` `@isim`", value="Kişiyi süzgeçe çevirirsin.", inline=False)
        embed.add_field(name=":hugging: `/sarıl` `@isim`", value="Kişiye sarılırsın.", inline=False)
        embed.add_field(name=":innocent: `/yalvar` `@isim`", value="Yalvarırsın, sana kimse dayanamaz.", inline=False)
        embed.add_field(name=":wave: `/görüşürüz`", value="Elvedalar zordur.", inline=False)
        embed.add_field(name=":game_die: `/yazıtura`", value="Acaba yazı mı gelecek, yoksa tura mı?", inline=False)
        embed.add_field(name=":dash: `/kaç`", value="Bir hışımla kaçarsın.", inline=False)
        embed.add_field(name=":sparkles: `/şirin`", value="Şirin gözük.", inline=False)
        embed.add_field(name=":boot: `/tekme` `@isim`", value="Tekmeyi vur.", inline=False)
        embed.add_field(name=":eyes: `/neyebakıyon` `@isim`", value="Kurabiye var simit var.", inline=False)
        embed.add_field(name=":weary: `/senpai` `@isim`", value="Senpai'ni belirle.", inline=False)
        embed.add_field(name=":wave: `/merhaba`", value="Selam ver.", inline=False)
        embed.set_footer(text="Sana yardımcı olmak için hep buradayım.")
        await ctx.send(embed=embed)



@bot.command()
@commands.has_guild_permissions(manage_channels=True, administrator=True)
async def kanalbelirle(ctx, kanal:discord.TextChannel):
    try:
        sunucuverileri.set_channel(kanal)
        await ctx.send("Kanal belirlendi.")
    except:
        await ctx.send("Bi'sıkıntı var.")    

async def update_data(users, user):
    userID = str(user.id)
    if not userID in users:
        users[userID] = {}
        users[userID]['experience'] = 0
        users[userID]['level'] = 1

async def add_experience(users, user, exp):
    userID = str(user.id)
    users[userID]['experience'] += exp

async def level_up(users, user, channel):
    userID = str(user.id)
    experience = users[userID]['experience']
    lvl_start = users[userID]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await channel.send('{}, seviye atladı! Yeni seviyen: `{}`'.format(user.mention, lvl_end))
        users[userID]['level'] = lvl_end




@bot.event
async def on_message(message):
    with open('users.json','r') as f:
        users = json.load(f)

    
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)

    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)    


    if message.author.bot:
        return
    if not message.guild:
        return           
   #BU KISIMA KOMUTLAR GÖNDERİLECEK. ÖZEL PM ATIYOR. 

    if sunucuverileri.get_reklam(message.guild) == 1:
       if not message.author.guild_permissions.administrator:
        for reklam in reklamlar:
          if reklam in message.content:
            await message.delete()
            await message.channel.send("Reklam yasaktır.",delete_after=3)


    if sunucuverileri.get_kufur(message.guild) == 1:
       if not message.author.guild_permissions.administrator:
        for kufur in küfürler:
          if kufur in message.content:
            await message.delete()
            await message.channel.send("Küfür etmek yasaktır.",delete_after=3)
     

    if message.content == "okul":
        await message.channel.send("hmm. Turşu gibi kokuyor.")
    if message.content == "selam":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "Selam":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "Sa":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "sa":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "slm":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "Slm":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "nabersiniz":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "merhaba":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "Merhaba":
        await message.channel.send("Selam, nasılsın?")
    if message.content == "iyiyim":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyiyim sen?":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyiyim, sen?":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyiyim sen":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyilik senden":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyilik senden?":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyi":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "İyiyim":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "İyilik sen nasılsın":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "İyiyim sen nasılsın?":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "iyiyim sen nasılsın?":
        await message.channel.send("Ben bir şey hissetmiyorum, Vhagar yüzünden..")
    if message.content == "yardım lazım":
        await message.channel.send("İşte buradayım, yardım için bir komutum var! :sunglasses: ==> `/yardım`")
    if message.content == "Yardım lazım":
        await message.channel.send("İşte buradayım, yardım için bir komutum var! :sunglasses: ==> `/yardım`")
    if message.content == "yardim lazim":
        await message.channel.send("İşte buradayım, yardım için bir komutum var! :sunglasses: ==> `/yardım`")
    if message.content == "Yardim Lazim":
        await message.channel.send("İşte buradayım, yardım için bir komutum var! :sunglasses: ==> `/yardım`")
    if message.content == "yardim lazim":
        await message.channel.send("İşte buradayım, yardım için bir komutum var! :sunglasses: ==> `/yardım`")
    if message.content == "yardim lazım":
        await message.channel.send("İşte buradayım, yardım için bir komutum var! :sunglasses: ==> `/yardım`")
    if message.content == "Vhagar":
        await message.channel.send("O isimde birisini tanıyorum..")
    if message.content == "berke":
        await message.channel.send("O isimde birisini tanıyorum..")
    if message.content == "Berke":
        await message.channel.send("O isimde birisini tanıyorum..")
    if message.content == "vhagar":
        await message.channel.send("O isimde birisini tanıyorum..")

        

    if "@" in message.content:
         userList = message.mentions
         for afkkullanici in userList:
             afkdurumu = veriler.get_afk(afkkullanici)
             if afkdurumu == None or afkdurumu== "0" or afkdurumu == "None":
                 pass
             else:
                 #await message.channel.send("{} kullanıcısının mesajı: {}".format(afkkullanici, afkdurumu)) 
                 embed=discord.Embed(title=":exclamation: Kullanıcı şu an AFK",color=0xff0000)
                 embed.add_field(name=":star: Sebep;", value="`{}` sebebiyle meşgul.".format(afkdurumu), inline=False)
                 embed.set_footer(text="dert etme birazdan gelir.")
                 embed.set_thumbnail(url=afkkullanici.avatar_url)
                 await message.channel.send(embed=embed)  
    elif "/kullanıcı" in message.content:
        return None
    await bot.process_commands(message)

    veriler.xp_ekle(message.author, 2)
    print(cwd+'\config\\veriler.json')


@bot.command()
async def vur(ctx, member:discord.Member):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Vuruldun! :boom:", value="{} adlı kovboy, seni vurdu {}".format(ctx.message.author.name, member.mention), inline=False)
    embed.set_footer(text="Süzgeçe döndün.")
    embed.set_image(url='https://media1.tenor.com/images/a83d41c02c2971629ac5a98a08db1fcd/tenor.gif?itemid=13384546')
    await ctx.send(embed=embed)

@bot.command()
async def kaç(ctx):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Kaçtı! :dash:", value="{} öyle bi'kaçtı ki..".format(ctx.message.author.name), inline=False)
    embed.set_footer(text="Çok hızlıydı..")
    embed.set_image(url='https://media1.tenor.com/images/adfd03676c48b837684f44c6cc321486/tenor.gif?itemid=16605920')
    await ctx.send(embed=embed)

@bot.command()
async def şirin(ctx):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="uWu :dizzy:", value="{} sen bi poğaçasın.".format(ctx.message.author.name), inline=False)
    embed.set_footer(text="Yumuşacık oldun.")
    embed.set_image(url='https://media1.tenor.com/images/1fe93596a8a0f84078b936305b319c55/tenor.gif?itemid=6194051')
    await ctx.send(embed=embed)  

@bot.command()
async def tekme(ctx, member:discord.Member):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Tekmeyi Yedin :boom:", value="{}, sana tekmeyi bastı. {}".format(ctx.message.author.name, member.mention), inline=False)
    embed.set_footer(text="Biraz acımıştır.")
    embed.set_image(url='https://media1.tenor.com/images/d790164f024de2917ff085d9eddd74e6/tenor.gif?itemid=15612559')
    await ctx.send(embed=embed)

@bot.command()
async def merhaba(ctx):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Merhaba :boom:", value="{}, Herkese merhaba.".format(ctx.message.author.name), inline=False)
    embed.set_footer(text="İyi eğlenceler.")
    embed.set_image(url='https://media1.tenor.com/images/72d407300428e6f2ef3e469511d5f8ec/tenor.gif?itemid=5463317')
    await ctx.send(embed=embed)    

@bot.command()
async def neyebakıyon(ctx, member:discord.Member):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Neye Bakıyon? :boom:", value="kurabiye var simit var? {}".format(member.mention), inline=False)
    embed.set_footer(text="Lan başlatma..")
    embed.set_image(url='https://media1.tenor.com/images/aa48d281845f11921a0395d48f3ab4c7/tenor.gif?itemid=13531718')
    await ctx.send(embed=embed)

@bot.command()
async def sarıl(ctx, member:discord.Member):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Sımsıkı sarıldı!", value="{}, sana sımsıkı sarılıyor {}.".format(ctx.message.author.name, member.mention), inline=False)
    embed.set_footer(text="Ne kadar da tatlı.")
    embed.set_image(url='https://media1.tenor.com/images/fd47e55dfb49ae1d39675d6eff34a729/tenor.gif?itemid=12687187')
    await ctx.send(embed=embed)

@bot.command()
async def görüşürüz(ctx):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Gidiyor! :wave:", value="{}, şimdilik aramızdan ayrılıyor.".format(ctx.message.author.name), inline=False)
    embed.set_footer(text="Çabuk gel.")
    embed.set_image(url='https://media1.tenor.com/images/f3c17c5ab1efca8e1cce4b8b6dd88228/tenor.gif?itemid=12999722')
    await ctx.send(embed=embed)

@bot.command()
async def yalvar(ctx, member:discord.Member):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Sana yalvarıyor!", value="{}, sana çok içten yalvardı {}.".format(ctx.message.author.name, member.mention), inline=False)
    embed.set_footer(text="Hadi ama! Buna kim dayanabilir?")
    embed.set_image(url='https://media1.tenor.com/images/21f9611aa1459d7634a88b257b10f871/tenor.gif?itemid=7252595')
    await ctx.send(embed=embed)

@bot.command()
async def senpai(ctx, member:discord.Member):
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Senpaii!! :sparkles:", value="{} diyor ki, notice me {} senpai.".format(ctx.message.author.name, member.mention), inline=False)
    embed.set_footer(text="Çok şirin.")
    embed.set_image(url='https://media1.tenor.com/images/9895b12b3971dc94c92a8368cf719553/tenor.gif?itemid=17870754')
    await ctx.send(embed=embed)    

@bot.command()
async def yazıtura(ctx):
    para = ["yazı", "tura"]
    paraat = random.choice(para)
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Para fırlattı!", value="{}, yazıtura için bir para attı.".format(ctx.message.author.name), inline=False)
    embed.set_footer(text="Bakalım ne gelecek?")
    embed.set_image(url='https://media1.tenor.com/images/756de4040539d4d0e0b2f24aa0afc6a1/tenor.gif?itemid=5526944')
    await ctx.send(embed=embed)
    time.sleep(3)
    embed=discord.Embed(color=0x8a36f2)
    embed.add_field(name="Sonuç:", value="`{}`, geldi {}".format(paraat, ctx.message.author.name), inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def anket(ctx, anketkonusu:str, anketaciklamasi:str, kanal:discord.TextChannel):
    embed = discord.Embed(title="Hadi Anket Yapalım!", color=0x8a36f2)
    embed.add_field(name=anketkonusu, value=anketaciklamasi)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
    mesaj = await ctx.send(embed=embed)
    await mesaj.add_reaction('✅')
    await mesaj.add_reaction('❌')

@bot.command()
async def kullanıcı(ctx, member:discord.Member):
    myembed = discord.Embed(title=member.name, color=0xff0021)
    myembed.add_field(name="Durum", value=member.status)
    myembed.add_field(name="Rol", value= member.top_role)
    #bu kısım
    myembed.add_field(name="Rütbe / Tecrübe", value=str(veriler.lv_come(member)) + " Level / " + str(veriler.exp_come(member)) + " EXP")
    myembed.add_field(name="Oluşturulma Tarihi", value=member.created_at)
    myembed.add_field(name="Sunucuya Katılma Tarihi", value=member.joined_at)
    myembed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=myembed)

@bot.event
async def on_command_error(ctx,error):
    channel = ctx.channel
    if isinstance(error, commands.MissingPermissions):
        await channel.send("Görünüşe bakılırsa yetkin yok, bunu yapmayacağım.")
    if isinstance(error, commands.MissingRequiredArgument):
        await channel.send("Bir şeyleri eksik yazmışsın, ==> `/yardım` buradan bakabilirsin.")
    if isinstance(error, commands.CommandNotFound):
        await channel.send("Böyle bir komutum olduğunu sanmıyorum, yoksa yapardım.. Gerçekten yapardım.. ==> `/yardım`")        


@bot.command()
@commands.has_guild_permissions(kick_members=True)
async def at(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} Kullanıcısı sunucudan atıldı!")

@bot.command(aliases=['n'])
@commands.has_guild_permissions(ban_members=True)
async def sustur(ctx, member:discord.Member = None,*,reason=None):
    role = discord.utils.get(ctx.guild.roles, name = "Susturulan")

    if role == None:
        role = await ctx.guild.create_role(name = 'Susturulan')

    await member.add_roles(role)
    await ctx.send(f"{member} Kullanıcısı susturuldu. Emri veren ==>`{ctx.author}`.")

    for channel in ctx.guild.channels:
        await channel.set_permissions(role, send_messages = False)  


@bot.command(aliases = ['un'])
@commands.has_guild_permissions(ban_members=True)
async def susturma(ctx, member:discord.Member = None):
     
     role = discord.utils.get(ctx.guild.roles, name = 'Susturulan')

     await member.remove_roles(role)
     await ctx.send(f"{member} artık konuşabilir.")
        
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, anything:discord.Member, *, reason=None):
    await anything.ban(reason=reason)
    await ctx.send(f"{anything} Kullanıcısı sunucudan Banlandı!")    

@bot.command()
async def bilgi(ileti):
    embed = discord.Embed(title="︵‿︵(´ ͡༎ຶ ͜ʖ ͡༎ຶ `)︵‿︵          ", description="_____________________", color=0x80ffff)
    embed.set_thumbnail(url="https://media1.tenor.com/images/41d44560f07064e56b8048b1d33512d5/tenor.gif?itemid=12235827")
    embed.set_author(name="Poe BOT")
    embed.add_field(name="Dil", value="Python", inline=True)
    embed.add_field(name="Developer", value="Vhagar#2837", inline=True)
    embed.add_field(name="Emeği Geçenler", value="Ragnarowski#7619",inline=True)
    embed.add_field(name="Sürüm", value="1.0.1A", inline=True)
    embed.add_field(name="Prefix / Yardım Komutu", value="`/` | `/yardım`", inline=True)
    embed.add_field(name="Destek Sunucusu", value="[Tıkla](https://discord.gg/fTqjyDk)", inline=True)
    embed.add_field(name="Oy Ver", value="[Tıkla](https://top.gg/bot/733681967631171625)",inline=True)
    embed.set_footer(icon_url= "https://cdn.discordapp.com/app-icons/733681967631171625/34d299a39e099f919547380b70721ae5.png?size=64", text="Bütün sorunlarınız için tek bir çözüm.")
    embed.add_field(name="Botu Kanalına Ekle", value="[Tıkla](https://discord.com/oauth2/authorize?client_id=733681967631171625&permissions=8&scope=bot)", inline=True)
    await ileti.send(embed=embed)  

@bot.command()
async def afk(ctx, *, durum:str):
    user=ctx.message.author
    veriler.set_afk(user, durum)
    await ctx.send("{} artık `{}`, sebebiyle AFK.".format(ctx.message.author.name,durum))

@bot.command()
async def afkboz(ctx):
    user=ctx.message.author
    veriler.set_afk(user, "0")
    await ctx.send("{} kullanıcısı artık AFK değil.".format(ctx.message.author.name))


@bot.command(aliases=["clear"])
@commands.has_permissions(manage_roles=True)
async def chattemizle(mesaj, sayi:int):
    if(mesaj.author.guild_permissions.administrator):
           if(sayi != None and sayi > 0):
               kanal = mesaj.channel
               message = await kanal.history(limit = sayi).flatten()

               mesaj2 = await mesaj.send("{} tane mesaj var, hepsi aklımda.. :pleading_face:".format(sayi))
               time.sleep(1)
               await mesaj2.edit(content = "{} mesajı aklımdan sildim. Bir daha kimse göremeyecek. :shushing_face:".format(sayi))
               time.sleep(1)
               await kanal.delete_messages(message)
               mesaj2.edit(content=":heavy_check_mark:")
               time.sleep(2)
               message = await kanal.history(limit=1).flatten()
               await kanal.delete_messages(message)
           elif(sayi < 0):

               await mesaj.send("Saçma bir değer verdin, negatif değerde mesajı nasıl sileyim ki. :triumph:")

           else:
               kanal = mesaj.channel
               message = await kanal.history(limit = 1000).flatten()

               mesaj2 = await mesaj.send("{} tane mesaj var, hepsi aklımda.. :pleading_face:".format(sayi))
               time.sleep(1)
               await mesaj2.edit(content="{} mesajı aklımdan sildim. Bir daha kimse göremeyecek. :shushing_face:")
               time.sleep(1)
               await kanal.delete_messages(message)
               mesaj2.edit(content=":heavy_check_mark:")
               time.sleep(2)
               message = await kanal.history(limit = 1).flatten()
               await kanal.delete_messages(message)

    else:
           await mesaj.send("Görünüşe göre yetkin yok, bunu yapmayacağım. :expressionless: ")   


@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def reklamengelle(ctx):
    guild = ctx.guild
    try:
        sunucuverileri.set_reklam(guild)
        await ctx.send("Artık senin için reklamları engelleyeceğim.")
    except:
        await ctx.send("Muhtemelen bir hata oluştu.")

@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def reklamengellekapat(ctx):
    guild = ctx.guild
    try:
        sunucuverileri.set_reklam(guild,0)
        await ctx.send("Artık reklamları engellemeyeceğim.")
    except:
        await ctx.send("Muhtemelen bir hata oluştu.")

@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def küfürengelle(ctx):
    guild = ctx.guild
    try:
        sunucuverileri.set_kufur(guild)
        await ctx.send("Artık kimse küfür edemez.")
    except:
        await ctx.send("Muhtemelen bir hata oluştu.")

@bot.command()
@commands.has_guild_permissions(manage_roles=True)
async def küfürengellekapat(ctx):
    guild = ctx.guild
    try:
        sunucuverileri.set_kufur(guild,0)
        await ctx.send("Artık küfür edilebilir.")
    except:
        await ctx.send("Muhtemelen bir hata oluştu.")        


bot.loop.create_task(change_status())
bot.run(bot.config_token)        
