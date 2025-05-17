import os
from aiohttp import web

async def handle(request):
    return web.Response(text="🤖 Yuserbot is alive on Render!")

app = web.Application()
app.router.add_get("/", handle)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    web.run_app(app, port=port)
