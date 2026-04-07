import asyncio
import telemetry.producer as tp
# TODO: yukarı silinecek

import json
from server.messages import handshake_message, admin_message, telemetry_message
from server.connection_manager import manager
from config import ADMIN_PASS


async def handler(websocket):
    manager.register(websocket)
    await websocket.send(handshake_message())
    
    try:
        async for message in websocket:
            await message_handler(websocket, message)
    except Exception as e:
        print(f"Bağlantı hatası: {e}")
    finally:

        manager.unregister(websocket)
        if websocket == manager.admin:
            await manager.broadcast(admin_message("available"))

async def message_handler(ws, message: str) -> None:
    try:
        data = json.loads(message)
    except json.JSONDecodeError:
        return

    msg_type = data.get('type')
    payload = data.get('payload', {})

    match msg_type:
        case "admin":
            password = payload.get('password')

            if password == ADMIN_PASS:
                if manager._admin is None:
                    manager.admin = ws
                    await manager.send(ws, admin_message("success"))
                    await manager.broadcast(admin_message("occupied")) 
                else:
                    await manager.send(ws, admin_message("occupied"))
            else:
                await manager.send(ws, admin_message("failed"))
                
        case "test": # TODO: silinecek
            while True:
                mtn = tp.motion()
                prc = tp.process()
                
                await manager.broadcast(telemetry_message(mtn, prc))
                await asyncio.sleep(1)
                
                                
        case _:
            return