import websockets

class ConnectionManager:
    def __init__(self):
        self._clients = set()
        self._admin = None
        
    def register(self, ws) -> None:
        print(f"Yeni bir bağlantı algılandı: {ws}")
        self._clients.add(ws)
        
    def unregister(self, ws) -> None:
        self._clients.discard(ws)
        if ws == self._admin:
            self._admin = None
            
    async def send(self, ws, message: str) -> None:
        try:
            await ws.send(message)
        except websockets.exceptions.ConnectionClosed:
            pass
            
    async def broadcast(self, message: str, ignore_admin: bool = True) -> None:
        dead = set()
        for client in list(self._clients): 
            if ignore_admin and client == self._admin:
                continue
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                dead.add(client)
        self._clients -= dead
    
    @property
    def admin(self):
        return self._admin
    
    @admin.setter
    def admin(self, ws) -> None:
        self._admin = ws

manager = ConnectionManager()
