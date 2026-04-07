import random
from telemetry.models import MotionData, ProcessData

def motion() -> MotionData:
    return MotionData(
        x     = round(random.uniform(-110, 110), 2),
        y     = round(random.uniform(-110, 110), 2),
        z     = round(random.uniform(-110, 110), 2),
        alpha = round(random.uniform(-90, 90), 2),
    )
    
def process() -> ProcessData:
    return ProcessData(
        temperature = round(random.uniform(-20, 80), 1),
        pressure    = round(random.uniform(0, 40), 2),
        flow        = round(random.uniform(0, 100), 1),
    )