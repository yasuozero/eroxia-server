from dataclasses import dataclass

@dataclass
class SystemState:
    active: bool = False
    dust: bool = False
    air: bool = False


state = SystemState()
