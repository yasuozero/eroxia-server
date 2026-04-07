from dataclasses import dataclass

@dataclass
class MotionData:
    x: int = 0
    y: int = 0
    z: int = 0
    alpha: int = 0
    
@dataclass
class ProcessData:
    temperature: int = 0
    pressure: int = 0
    flow: int = 0