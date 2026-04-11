from dataclasses import dataclass

@dataclass
class MotionData:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    alpha: float = 0.0

@dataclass
class ProcessData:
    temperature: float = 0.0
    pressure: float = 0.0
    flow: float = 0.0