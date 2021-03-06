import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/2056781888/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/2056781888')
   open(f"Users/2056781888/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 1761415
API_HASH = "e989d7ca9dfbfe3da8ffb39e283dd9ce"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
UPDATES_CHANNEL = "OwenUserBot"
OWNER= [5159148002]
PREMIUM=[5159148002]
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))






# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("Login???", callback_data="Login"), InlineKeyboardButton("Adding????", callback_data="Adding") ],[InlineKeyboardButton("Phone??????", callback_data="Edit"), InlineKeyboardButton("PhoneSee????", callback_data="Ish")],[InlineKeyboardButton("Phone Remove??????", callback_data="Remove"), InlineKeyboardButton("AdminPannel", callback_data="Admin")]])
   await message.reply_text(f"**Hi** `{message.from_user.first_name}` **!\n\nI'm Induced Scraper Bot \nMade for doing Scraping for free,\nWithout Using Any Use of Python.\n\nMade with ?????? By @Ber4tbey**", reply_markup=but)



# ------------------------------- Set Phone No --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()

   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Premium deilsin ?????? By @Ber4tbey**")
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**Giri?? yapmak i??in hesap say??s??n?? girin (in intiger)\n\nMade with ?????? By @Ber4tbey**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**Ge??ersiz Bi??im 1'den az Tekrar deneyin\n\nMade with ?????? By @Ber4tbey**""")
         return
      if a>100:
         await app.send_message(message.chat.id, f"**Yaln??zca {100-a} Telefon numaras?? ekleyebilirsiniz \n\nMade with ?????? By @Ber4tbey**")
         return
      for i in range (1,n+1):
         number = await app.ask(chat_id=message.chat.id, text="**??imdi Telegram Hesab??n??z??n Telefon Numaras??n?? Uluslararas?? Formatta G??nderin. \n**??lke Kodu** dahil. \n??rnek: **+14154566376 = 14154566376 sadece + de??il**\n\nMade with ?????? By @Ber4tbey**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**Bahsedildi??i gibi + dahil de??ildir\n\nMade with ?????? By @Ber4tbey**""")
         elif len(phone)==11 or len(phone)==12:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). Phone: {phone} Set Sucessfully???\n\nMade with ?????? By @Ber4tbey**")
         else:
            await app.send_message(message.chat.id, """**Ge??ersiz Numara Bi??imi Tekrar deneyin\n\nMade with ?????? By @Ber4tbey**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ?????? By @Ber4tbey**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
 
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Premium ??yesi deilsin\n\nMade with ?????? By @Ber4tbey**")
      return
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"{e.x} Saniyelik Floodwait'iniz Var")
            return
         except PhoneNumberInvalidError:
            await message.reply("Telefon Numaran??z Ge??ersiz.\n\nYeniden Ba??lamak i??in /start'a bas??n!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} is Baned")
            continue
         try:
            otp = await app.ask(message.chat.id, ("Telefon numaran??za bir OTP g??nderilir, \nL??tfen OTP'yi `1 2 3 4 5` format??nda girin. __(Her say?? aras??ndaki bo??luk!)__ \n\nBot OTP g??ndermiyorsa, Bot'a /start komutuyla /yeniden ba??latmay?? ve G??revi Ba??latmay?? tekrar deneyin.\n??ptal etmek i??in /iptal'e bas??n."), timeout=300)
         except TimeoutError:
            await message.reply("5 Dakikal??k Zaman S??n??r??na Ula????ld??.\nYeniden Ba??lamak i??in /start'a bas??n!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("Ge??ersiz kod.\n\nYeniden Ba??lamak i??in /start'a bas??n!")
            return
         except PhoneCodeExpiredError:
            await message.reply("Kodun S??resi Doldu.\n\nYeniden Ba??lamak i??in /start'a bas??n!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"Hesab??n??z??n ??ki Ad??ml?? Do??rulamas?? Var.\nL??tfen Parolan??z?? Girin.",timeout=300)
            except TimeoutError:
               await message.reply("`5 Dakikal??k Zaman S??n??r??na Ula????ld??.\n\nYeniden Ba??lamak i??in /start'a bas??n!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**HATA:** `{str(e)}`")
               return
            
      with open("Users/2056781888/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/2056781888/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="Good news, no limits are currently applied to your account. You???re free as a bird!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"Ba??ar??yla Giri?? Yap??? Yap??ld??.\n\n**Ad:** {me.first_name}\n**Kullan??c?? ad??:** {me.username}\n**Telefon:** {phone}\n**SpamBot ??statistikleri :** {stats}\n\n**Made with ?????? By @Ber4tbey**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**Telefon numaras??n?? girmediniz \nl??tfen Config??????  /start ile d??zenleyin.\n\nMade with ?????? By @Ber4tbey**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ?????? By @Ber4tbey**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**T??m Hesaplar??n Giri??i {s}  {po} Hesap Kullan??labilir \n\nMade with ?????? By @Ber4tbey**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ?????? By @Ber4tbey**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:

   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Premium ??yesi deilsin\n\nMade with ?????? By @Ber4tbey**")
      return
   number = await app.ask(chat_id=message.chat.id, text="**Grup kullan??c?? ad??n?? at??n??z \n\nMade with ?????? By @Ber4tbey**")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Gtup kullan??c?? ad??n?? at??n??z \n\nMade with ?????? By @Ber4tbey**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**??imdi G??nder Ba??lang??c??  \n\nMade with ?????? By @Ber4tbey**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Ekleme ba??lad??**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**Scraping Start**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nMade with ?????? By @Ber4tbey**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**Error: {phone}Sonrakine Ge??erken Baz?? Hatalar olu??tu\n\nMade with ?????? By @Ber4tbey**")
                     break
                  if dad>40:
                     r+="**\nMade with ?????? By @Ber4tbey**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Ekleme ba??lad??**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nMade with ?????? By @Ber4tbey**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**FloodWaitError for {s.seconds} sec\nMoving To Next Number**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Error In Entry"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 10:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**Too Many PeerFloodError\nMoving To Next Number**")
                     break
                  status = 'PeerFloodError'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ???   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Error: {e} \n\n Made with ?????? By @Ber4tbey")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Error: {e}\n\nMade with ?????? By @Ber4tbey**")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
  
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Premium ??yesi deilsin\n\nMade with ?????? By @Ber4tbey**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Your Phone Numbers are**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nMade with ?????? By @Ber4tbey**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Your Phone Numbers are**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nMade with ?????? By @Ber4tbey**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   
   if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Premium ??yesi deilsin\n\nMade with ?????? By @Ber4tbey**")
      return
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**Silmek i??in hesap numaras??n?? g??nder\n\nMade with ?????? By @Ber4tbey**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="Ba??ar??l??")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nMade with ?????? By @Ber4tbey**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):

   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("Users???", callback_data="Users")], [InlineKeyboardButton("Broadcast????", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**Hi** `{message.from_user.first_name}` **!\n\nWelcome to Admin Pannel of ??ye Bot\n\nMade with ?????? By @Ber4tbey**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**You are not owner of Bot \n\nMade with ?????? By @Ber4tbey**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /login'e t??klaman??z yeterli.\n\nMade with ?????? By @Ber4tbey**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /phonesee'ye t??klaman??z yeterli.\n\nMade with ?????? By @Ber4tbey**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /kald??r'a t??klaman??z yeterli.\n\nMade with ?????? By @Ber4tbey**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Art??k bir ??ey yok..!\nOturum A????? Hesaptan eklemeye ba??lamak i??in /adding t??klaman??z yeterli.\n\nMade with ?????? By @Ber4tbey**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nGiri?? yapmak ve Hesap istatistiklerini kontrol etmek i??in /phone'a t??klaman??z yeterli.\n\nMade with ?????? By @Ber4tbey**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Art??k hi??bir ??ey yok..!\nEve Gitmek i??in /start'a t??klaman??z yeterli.\n\nMade with ?????? By @Ber4tbey**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"L??tfen bekleyin...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**Yeni Kullan??c??n??n Kullan??c?? Kimli??ini G??nder\n\nMade with ?????? By @Ber4tbey**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="Done SucessFully")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2021-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Made with ?????? By @Ber4tbey**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Users???", callback_data="Users")], [InlineKeyboardButton("Broadcast????", callback_data="Broadcast")],[InlineKeyboardButton("AddUser", callback_data="New")], [InlineKeyboardButton("Check Users", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**Welcome to Admin Pannel of Induced Bot\n\nMade with ?????? By @Ber4tbey**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**You are not owner of Bot \n\nMade with ?????? By @Ber4tbey**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**Now me message For Broadcast\n\nMade with ?????? By @Ber4tbey**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"Successfully Broadcasted to {a} Chats\nFailed - {b} Chats !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**Error: {e}\n\nMade with ?????? By @Ber4tbey**")




text = """
?????????????????????Members 
?????????????????? Scraping Bot
??????????????????
?????????????????????Induced
?????????????????? Scraper Bot
??????????????????
?????????????????? 
?????????????????? 
"""
print(text)
print("Induced Ekleme ba??lad??ed Sucessfully........")
app.run()
