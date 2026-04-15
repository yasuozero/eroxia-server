import json
from domain.state import state 
from domain.session import session
from telemetry.models import MotionData, ProcessData
from server.connection_manager import manager
from typing import Literal

def handshake_message() -> str:
    return json.dumps(
        {
            "type": "handshake",
            "payload": {
                "admin": manager.admin is not None,
                "session_id": session.id,
                "system": {
                    "active": state.active,  
                    "dust": state.dust,
                    "air": state.air
                } 
            },
        }
    )
    
def admin_result_message(status: Literal["failed", "success", "occupied", "available"]) -> str:
    return json.dumps({
        "type": "admin_result",
        "payload": {
            "status": status,
            "session_id": session.id
        }
    }) 

def telemetry_message(motion: MotionData, process: ProcessData) -> str:
    return json.dumps({
        "type": "telemetry",
        "payload": {
            "t": session.active_time_seconds,
            "motion": {
                "x": motion.x,
                "y": motion.y,
                "z": motion.z,
                "alpha": motion.alpha,
            },
            "process": {
                "temperature": process.temperature,
                "pressure": process.pressure,
                "flow": process.flow,
            }
        }
    })

def action_result_message(action: str, success: bool) -> str:
    return json.dumps({
        "type": "action_result",
        "payload": {
            "action": action,
            "success": success
        }
    })