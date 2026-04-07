import asyncio
import websockets

from config import WS_HOST, WS_PORT
from server.handler import handler


async def main():
    await websockets.serve(handler, WS_HOST, WS_PORT)
    print(f"WebSocket sunucu çalışıyor: ws://{WS_HOST}:{WS_PORT}")
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())


# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/yasuozero/eroxia-server.git
# git push -u origin main