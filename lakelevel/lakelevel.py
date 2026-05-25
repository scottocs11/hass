import requests
import pandas as pd
from io import StringIO
url = "https://www.lakelevels.info/"
# html = requests.get(url)
# lakename = "Chickamauga  (TN)"
html = await hass.async_add_executor_job(requests.get, url)
df_list = pd.read_html(StringIO(html.text))
df = df_list[4]

def update_lake_info():
    html = await hass.async_add_executor_job(requests.get, url)
    df_list = pd.read_html(StringIO(html.text))
    df = df_list[4]
    lakename = state.get("input_select.lake")
    fdf = df[df['Lake Name'].str.contains(lakename)].reset_index()
    levelCurrent = fdf.at[0,'Current Level']
    levelCurrent = levelCurrent.item()
    levelFull = fdf.at[0,'Full Pool']
    levelFull = levelFull.item()
    levelDifference = fdf.at[0,'+/- Full Pool']
    levelDifference = levelDifference.item()
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

def quick_update_lake_info():
    lakename = state.get("input_select.lake")
    fdf = df[df['Lake Name'].str.contains(lakename)].reset_index()
    levelCurrent = fdf.at[0,'Current Level']
    levelCurrent = levelCurrent.item()
    levelFull = fdf.at[0,'Full Pool']
    levelFull = levelFull.item()
    levelDifference = fdf.at[0,'+/- Full Pool']
    levelDifference = levelDifference.item()
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

@time_trigger("once(06:00:00)")
def update_sensors_time():
    update_lake_info()

@time_trigger("once(now)","startup")
def update_sensors_time():
    quick_update_lake_info()

@state_trigger("input_select.lake")
def update_sensors_lakechange():
    quick_update_lake_info()