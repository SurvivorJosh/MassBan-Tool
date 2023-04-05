# MassBan-Tool
discord mass ban tool i guess. if it's showing errors fix it yourself

# Requirements
```bash
pip install -r requirements.txt
```
# OR:
simply pip isntall these seperately.
tasksio
requests
aiohttp
asyncio


# FIX
```Python
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
paste this ***before*** ```Python asyncio.run(main())``` if your getting the Event loop closed error <br>
![image](https://user-images.githubusercontent.com/123038077/230219014-bc5e66dc-b237-496c-b5a0-d2e1e28d642e.png)
