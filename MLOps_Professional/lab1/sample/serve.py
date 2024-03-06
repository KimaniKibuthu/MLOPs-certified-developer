import uvicorn
import logging
import warnings

from fastapi import FastAPI
from data_model import MaintenancePayload, HelpCall
from maintenance import test_maintenance, test_hydraulic_pressure


app = FastAPI()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore")


@app.get("/ping")
async def ping():
    """Ping server to determine status

    Returns
    -------
    API response
        response from server on health status
    """
    return {"message":"Server is Running"}

@app.post("/maintenance")
async def predict(payload:MaintenancePayload):
    """
    Predicts the maintenance status of the harvester based on the temperature and pressure sensor readings

    Args:
        payload (MaintenancePayload): The payload containing the temperature and pressure sensor readings

    Returns:
        dict: The maintenance status of the harvester
    """
    temp_result = test_maintenance(payload.temperature)
    pressure_result = test_hydraulic_pressure(payload.pressure)
    if temp_result == 'No Maintenance Required' and pressure_result == 'No Maintenance Required':
        maintenance_result = 'No Maintenance Required'
    elif temp_result == 'Needs Maintenance' and pressure_result == 'Needs Maintenance':
        maintenance_result = 'Needs Maintenance, Temperature and Pressure Sensor'
    else:
        if temp_result == 'Needs Maintenance':
            maintenance_result = 'Needs Maintenance, Temperature Sensor'
        
        elif pressure_result == 'Needs Maintenance':
            maintenance_result = 'Needs Maintenance, Pressure Sensor'
        
    return {"msg": "Completed Analysis", "Maintenance Status": maintenance_result}

@app.post("/supportbot")
async def help(helpcall:HelpCall):
    if helpcall.message.lower() == 'help':
        return {"msg": "bring the harvester in for maintenance"}

if __name__ == "__main__":
    uvicorn.run("serve:app", host="localhost", port=5000, log_level="info", reload=True)