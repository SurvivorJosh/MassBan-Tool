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
paste this before ```Python asyncio.run(main())``` if your getting the Event loop closed error
