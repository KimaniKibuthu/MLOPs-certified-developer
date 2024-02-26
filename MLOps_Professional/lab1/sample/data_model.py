from pydantic import BaseModel

class MaintenancePayload(BaseModel):
    temperature: int
    pressure: int
    
class HelpCall(BaseModel):
    message: str