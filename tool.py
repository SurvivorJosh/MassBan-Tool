import asyncio, os, requests
import aiohttp
import tasksio, time


token = input("Token: ")
guild_id = input("Guild Id: ")



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
                print(f"Banned {id}")
            elif r.status == 429:
                b = await r.json()
                await asyncio.sleep(b['retry_after'])
            
                
                
                
                
                
async def main():
    
    async with aiohttp.ClientSession() as ses:
        async with ses.get(f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers) as r:
            memberIDS = await r.json()
            print(len(memberIDS))
    async with tasksio.TaskPool(20_000) as pool:
        for member in memberIDS:
            await pool.put(worker(member["user"]["id"]))
            
            
            
            
            
if __name__ == "__main__":

    asyncio.run(main())
