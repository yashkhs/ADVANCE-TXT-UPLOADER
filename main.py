# Don't Remove Credit Tg - @Tushar0125
# Ask Doubt on telegram @Tushar0125

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Define the owner's user ID
OWNER_ID = 5840594311 # Replace with the actual owner's user ID

# List of sudo users (initially empty or pre-populated)
SUDO_USERS = [5840594311,7856557198]

# Function to check if a user is authorized
def is_authorized(user_id):
    return user_id in SUDO_USERS

# Function to check if a user is authorized
def is_authorized(user_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

# Sudo command to add/remove sudo users
@bot.on_message(filters.command("sudo"))
async def sudo_command(bot: Client, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("**🚫 You are not authorized to use this command.**")
        return

    try:
        args = message.text.split(" ", 2)
        if len(args) < 2:
            await message.reply_text("**Usage:** `/sudo add <user_id>` or `/sudo remove <user_id>`")
            return

        action = args[1].lower()
        target_user_id = int(args[2])

        if action == "add":
            if target_user_id not in SUDO_USERS:
                SUDO_USERS.append(target_user_id)
                await message.reply_text(f"**✅ User {target_user_id} added to sudo list.**")
            else:
                await message.reply_text(f"**⚠️ User {target_user_id} is already in the sudo list.**")
        elif action == "remove":
            if target_user_id == OWNER_ID:
                await message.reply_text("**🚫 The owner cannot be removed from the sudo list.**")
            elif target_user_id in SUDO_USERS:
                SUDO_USERS.remove(target_user_id)
                await message.reply_text(f"**✅ User {target_user_id} removed from sudo list.**")
            else:
                await message.reply_text(f"**⚠️ User {target_user_id} is not in the sudo list.**")
        else:
            await message.reply_text("**Usage:** `/sudo add <user_id>` or `/sudo remove <user_id>`")
    except Exception as e:
        await message.reply_text(f"**Error:** {str(e)}")

# Start command handler
@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    editable = await m.reply_text(
       f"ʜᴇʟʟᴏ🙂\n\n ☆ ɪ ᴀᴍ ᴛxᴛ ᴛᴏ ᴠɪᴅᴇᴏ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ.\n\n ☆ ғᴏʀ ᴜsᴇ ᴍᴇ sᴇɴᴅ /tushar.</a>", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🇮🇳ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ🇮🇳" ,url=f"https://t.me/Tushar0125") ],
                    [
                    InlineKeyboardButton("🔔ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ🔔" ,url="https://t.me/TxtToVideoUpdateChannel") ],
                    [
                    InlineKeyboardButton("🦋ғᴏʟʟᴏᴡ ᴜs🦋" ,url="https://t.me/AIM_AIIMS143") ]                               
            ]))
  
  
# Stop command handler
@bot.on_message(filters.command("stop"))
async def restart_handler(_, m: Message):
    if not is_authorized(m.from_user.id):
        await m.reply_text("**🚫 You are not authorized to use this bot.**")
        return

    await m.reply_text("**𝗦𝘁𝗼𝗽𝗽𝗲𝗱**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("🔮Restarted🔮", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
    
# Upload command handler
@bot.on_message(filters.command(["tushar"]))
async def upload(bot: Client, m: Message):
    if not is_authorized(m.from_user.id):
        await m.reply_text("**🚫 You are not authorized to use this bot.**")
        return
 
    editable = await m.reply_text('⚡𝗦𝗘𝗡𝗗 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘⚡')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    
    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**🙂𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗳𝗶𝗹𝗲 𝗶𝗻𝗽𝘂𝘁🙂.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝗧𝗼𝘁𝗮𝗹 𝗟𝗶𝗻𝗸𝘀 𝗙𝗼𝘂𝗻𝗱 𝗔𝗿𝗲🔗🔗** **{len(links)}**\n\n**𝗦𝗲𝗻𝗱 𝗙𝗿𝗼𝗺 𝗪𝗵𝗲𝗿𝗲 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗜𝗻𝗶𝘁𝗶𝗮𝗹 𝗜𝘀** **𝟭**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝗡𝗼𝘄 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗬𝗼𝘂𝗿 𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**📸 𝗘𝗻𝘁𝗲𝗿 𝗥𝗲𝘀𝗼𝗹𝘂𝘁𝗶𝗼𝗻 📸**\n➤ 𝟭𝟰𝟰\n➤ 𝟮𝟰𝟬\n➤ 𝟯𝟲𝟬\n➤ 𝟰𝟴𝟬\n➤ 𝟳𝟮𝟬\n➤ 𝟭𝟬𝟴𝟬")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("𝗡𝗼𝘄 𝗘𝗻𝘁𝗲𝗿 𝗔 𝗖𝗮𝗽𝘁𝗶𝗼𝗻 𝗧𝗼 𝗔𝗱𝗱 𝗖𝗮𝗽𝘁𝗶𝗼𝗻 𝗢𝗻 𝗬𝗼𝘂𝗿 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗙𝗶𝗹𝗲\n\n𝗘𝗴 » 𝗧𝘂𝘀𝗵𝗮𝗿")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3

    await editable.edit("**𝗘𝗻𝘁𝗲𝗿 𝗣𝘄 𝗧𝗼𝗸𝗲𝗻 𝗙𝗼𝗿 𝗣𝘄 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗼𝗿 𝗦𝗲𝗻𝗱 `'noo'` 𝗙𝗼𝗿 𝗨𝘀𝗲 𝗗𝗲𝗳𝗮𝘂𝗹𝘁**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)
    if raw_text4 == 'noo':
        MR = token
    else:
        MR = raw_text4
   
    await editable.edit("𝗡𝗼𝘄 𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 𝗧𝗵𝘂𝗺𝗯 𝗨𝗿𝗹 𝗘𝗴 » https://graph.org/file/13a89d77002442255efad-989ac290c1b3f13b44.jpg\n𝗢𝗿 𝗜𝗳 𝗗𝗼𝗻'𝘁 𝗪𝗮𝗻𝘁 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗦𝗲𝗻𝗱 = 𝗻𝗼")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']

            elif "tencdn.classplusapp" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "media-cdn.classplusapp" in url:
             headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
             params = (('url', f'{url}'),)
             response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
             url = response.json()['url']
            
           
            if 'testbook' in url:
                id =  url.split("/")[-2]
                url =  "https://api-piyush-10c6745e41fc.herokuapp.com/fetch_url?url=https://cpvod.testbook.com/" + id + "/playlist.m3u8"

            elif 'cpvod.testbook' in url:
                id =  url.split("/")[-2]
                url =  "https://api-piyush-10c6745e41fc.herokuapp.com/fetch_url?url=https://cpvod.testbook.com/" + id + "/playlist.m3u8"
                            
            
            elif '/utkarshapp.mpd' in url:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
             id =  url.split("/")[-2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
             url =  "https://apps-s3-prod.utkarshapp.com/" + id + "/utkarshapp.com"
 
            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                  headers = {  
                          "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",  
                          "Accept-Language": "en-US,en;q=0.9",  
                  }
                  response = requests.get(url, headers=headers)  
                  print(response.text) 
                
            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
                    
           
           
            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url = f"https://madxapi-d0cbf6ac738c.herokuapp.com/{id}/master.m3u8?token={raw_text4}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if raw_text0 in "vikramjeet" :
                y= url.replace("/", "%2F")
#                rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2Flivehttporigin%2F{y[56:-14]}%2Fmaster.m3u8"
                rout =f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2F{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            elif raw_text0 in "sure60":
                y1= url.replace("/", "%2F")
#                rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2Flivehttporigin%2F{y[49:-14]}%2Fmaster.m3u8"
                rout =f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2F{y1[32:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"            
            elif raw_text0 in "theoptimistclasses":
                y= url.replace("/", "%2F")
                rout=f"https://live.theoptimistclasses.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.theoptimistclasses.com%2F{y[44:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')              
                cook = "cookie.txt"
            
            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MzUxMzUzNjIsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiYmt3cmVIWmxZMFUwVXpkSmJYUkxVemw2ZW5Oclp6MDkiLCJmaXJzdF9uYW1lIjoiY25GdVpVdG5kRzR4U25sWVNGTjRiVW94VFhaUVVUMDkiLCJlbWFpbCI6ImFFWllPRXhKYVc1NWQyTlFTazk0YmtWWWJISTNRM3BKZW1OUVdIWXJWWE0wWldFNVIzZFNLelE0ZHowPSIsInBob25lIjoiZFhSNlFrSm9XVlpCYkN0clRUWTFOR3REU3pKTVVUMDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJhVVZGZGpBMk9XSnhlbXRZWm14amF6TTBVazQxUVQwOSIsImRldmljZV90eXBlIjoid2ViIiwiZGV2aWNlX3ZlcnNpb24iOiJDaHJvbWUrMTE5IiwiZGV2aWNlX21vZGVsIjoiY2hyb21lIiwicmVtb3RlX2FkZHIiOiIyNDA5OjQwYzI6MjA1NTo5MGQ0OjYzYmM6YTNjOTozMzBiOmIxOTkifX0.Kifitj1wCe_ohkdclvUt7WGuVBsQFiz7eezXoF1RduDJi4X7egejZlLZ0GCZmEKBwQpMJLvrdbAFIRniZoeAxL4FZ-pqIoYhH3PgZU6gWzKz5pdOCWfifnIzT5b3rzhDuG7sstfNiuNk9f-HMBievswEIPUC_ElazXdZPPt1gQqP7TmVg2Hjj6-JBcG7YPSqa6CUoXNDHpjWxK_KREnjWLM7vQ6J3vF1b7z_S3_CFti167C6UK5qb_turLnOUQzWzcwEaPGB3WXO0DAri6651WF33vzuzeclrcaQcMjum8n7VQ0Cl3fqypjaWD30btHQsu5j8j3pySWUlbyPVDOk-g'
                url = url.split("bcov_auth")[0]+bcov
                
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
           
            if "apps-s3-jw-prod.utkarshapp" in url:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'      
       
            elif "webvideos.classplusapp." in url:
               cmd = f'yt-dlp --add-header "referer:https://web.classplusapp.com/" --add-header "x-cdn-tag:empty" -f "{ytf}" "{url}" -o "{name}.mp4"'
            
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[📽️] 𝗩𝗶𝗱_𝗜𝗱 :** {str(count).zfill(3)}.**\n\n\n**☘️𝗧𝗶𝘁𝗹𝗲 𝗡𝗮𝗺𝗲** ➤ {name1}.({res}).𝔗𝔲𝔰𝔥𝔞𝔯.mkv**\n\n\n**<pre><code>📚𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲** ➤ **{raw_text0}</code></pre>**\n\n\n**📥 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗲𝗱 𝗕𝘆** ➤ **{raw_text3}**' 
                cc1 = f'**[📁] 𝗣𝗱𝗳_𝗜𝗱 :** {str(count).zfill(3)}.**\n\n\n**☘️𝗧𝗶𝘁𝗹𝗲 𝗡𝗮𝗺𝗲** ➤ {name1}.𝔗𝔲𝔰𝔥𝔞𝔯.pdf**\n\n\n**<pre><code>📚𝗕𝗮𝘁𝗰𝗵 𝗡𝗮𝗺𝗲** ➤ **{raw_text0}</code></pre>**\n\n\n**📥 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗲𝗱 𝗕𝘆** ➤ **{raw_text3}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x) 
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**🔔𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗𝗜𝗡𝗚🔔**\n\n**📝ɴᴀᴍᴇ » **`{name}\n\n❄ǫᴜᴀʟɪᴛʏ » {raw_text2}`\n\n**🔗ᴜʀʟ »** `Not Defined\n\n🤖𝗕𝗢𝗧 𝗠𝗔𝗗𝗘 𝗕𝗬 ➤ 𝗧𝗨𝗦𝗛𝗔𝗥`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**🥺ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ғᴀɪʟᴇᴅ🥺 **\n\n{str(e)}\n\n**ɴᴀᴍᴇ** » {name}\n\n**ʟɪɴᴋ** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**🥳✅𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗗𝗼𝗻𝗲✅🥳**")


bot.run()
