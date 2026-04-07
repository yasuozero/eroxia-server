import secrets
import config
import time

class Session:
    def __init__(self):
        self.id = secrets.token_hex(config.SESSION_ID_LENGTH)
        self._start_time = time.monotonic()
        self._activity_start = None
        
    def get_elapsed_ms(self) -> int:
        return int((time.monotonic() - self._start_time) * 1000)
    
    def start_activity(self):
        self._activity_start = time.monotonic()
    
    def stop_activity(self):
        self._activity_start = None
    
    @property
    def active_time_seconds(self) -> int:
        if self._activity_start is not None:
            return int(time.monotonic() - self._activity_start)
        return 0

session = Session()