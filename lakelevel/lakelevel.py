import requests
import pandas as pd
from io import StringIO
url = "https://www.lakelevels.info/USA/Tennessee/"
html = await hass.async_add_executor_job(requests.get, url)
df_list = pd.read_html(StringIO(html.text))
df = df_list[3]
levelCurrent = df.at[3,'Current Level']
levelCurrent = levelCurrent.item()
levelFull = df.at[3,'Full Pool']
levelFull = levelFull.item()
levelDifference = df.at[3,'+/- Full Pool']
levelDifference = levelDifference.item()
levelDate = df.at[3,'Reading Date - Time']

@time_trigger("startup", "once(06:00:00)")
def update_lake_info():
    val = print(levelCurrent)
    state.set("sensor.chickamauga_lake_full", value=levelFull, attr={'unit_of_measurement': 'ft'})
    state.set("sensor.chickamauga_lake_level", value=levelCurrent, attr={'unit_of_measurement': 'ft'})
    state.set("sensor.chickamauga_level_difference", value=levelDifference, attr={'unit_of_measurement': 'ft'})
    state.set("sensor.chickamauga_refresh_time", value=levelDate)
