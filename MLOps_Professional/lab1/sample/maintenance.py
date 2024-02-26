# maitnenace test business logic

def test_maintenance(temperature:int):
    """_summary_

    Parameters
    ----------
    temperature : int
        test parameter for temperature sensor readings

    Returns
    -------
    str
        'Approved' or 'Denied' based on temperature readings
    """
    maintenance_status = 'Needs Maintenance' if temperature > 50 else 'No Maintenance Required'
    
    return maintenance_status

def test_hydraulic_pressure(pressure:int):
    """_summary_

    Parameters
    ----------
    pressure : int
        test parameter for hydraulic pressure sensor readings

    Returns
    -------
    str
        'Approved' or 'Denied' based on hydraulic pressure readings
    """
    maintenance_status = 'Needs Maintenance' if pressure > 2000 else 'No Maintenance Required'
    
    return maintenance_status