import requests
import pandas as pd
from io import StringIO
url = "https://www.lakelevels.info/"

def initial_lake_info():
    html = await hass.async_add_executor_job(requests.get, url) #Pyscript Only
    #When testing in python: html = requests.get(url)
    df_list = pd.read_html(StringIO(html.text))
    df = df_list[4]
    df['Lake Name'] = df['Lake Name'].str.lower().str.replace('  ', ' ').str.replace('(', '').str.replace(')', '')
    return df

#df = initial_lake_info() #Initial Request

@service
def update_lake_info():
    """Update Lake Info using Pyscript"""
    log.info(f"Reloaded Lake Info")
    df = initial_lake_info()
    quick_load_lake_info(df)

def quick_load_lake_info(df):
    lakename = state.get("input_select.lake") #Pyscript only
    #When testing in python: lakename = "Cherokee (TX)"
    lakename = lakename.lower().replace('(', '').replace(')', '')
    exists = df['Lake Name'].str.contains(lakename).any().item()
    if exists  == True:
        fdf = df[df['Lake Name'].str.contains(lakename)].reset_index()
        levelCurrent = fdf.at[0,'Current Level'].item()
        levelFull = fdf.at[0,'Full Pool'].item()
        levelDifference = fdf.at[0,'+/- Full Pool'].item()
        levelDate = fdf.at[0,'Reading Date - Time']

        state.set('sensor.lake_current_level', levelCurrent, {
        'friendly_name': 'Current Level',
        'unit_of_measurement': 'ft',
        'state class': 'measurement',
        'icon': 'mdi:waves'
        })

        state.set('sensor.lake_full_pool', levelFull, {
        'friendly_name': 'Full Pool',
        'unit_of_measurement': 'ft',
        'state class': 'measurement',
        'icon': 'mdi:moon-full'
        })

        state.set('sensor.lake_level_difference', levelDifference, {
        'friendly_name': 'Difference',
        'unit_of_measurement': 'ft',
        'state class': 'measurement',
        'icon': 'mdi:waves-arrow-up'
        })

        state.set('sensor.lake_last_update', levelDate, {
        'friendly_name': 'Last Update',
        'icon': 'mdi:update'
        })
    else:
        state.set('sensor.lake_current_level', 'Lake Not Found', {
        'friendly_name': 'Current Level',
        'unit_of_measurement': 'ft',
        'state class': 'measurement',
        'icon': 'mdi:waves'
        })

        state.set('sensor.lake_full_pool', 'Lake Not Found', {
        'friendly_name': 'Full Pool',
        'unit_of_measurement': 'ft',
        'state class': 'measurement',
        'icon': 'mdi:moon-full'
        })

        state.set('sensor.lake_level_difference', 'Lake Not Found', {
        'friendly_name': 'Difference',
        'unit_of_measurement': 'ft',
        'state class': 'measurement',
        'icon': 'mdi:waves-arrow-up'
        })

        state.set('sensor.lake_last_update', 'Lake Not Found', {
        'friendly_name': 'Last Update',
        'icon': 'mdi:update'
        })

@time_trigger("once(06:00:00)")
def update_sensors_time():
    update_lake_info()

@time_trigger("startup")
def quick_load_sensors_time():
    quick_load_lake_info(df)

@state_trigger("input_select.lake")
def quick_load_lakechange():
    quick_load_lake_info(df)