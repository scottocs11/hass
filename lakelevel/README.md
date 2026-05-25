This script pulls US lake level info from [lakelevels.info](https://www.lakelevels.info) and updates HASS sensors with the data.

<img src="https://github.com/scottocs11/hass/blob/main/lakelevel/images/lakelevelcard.png" width="400"/>

Features:
1. Uses Python libraries [requests](https://pypi.org/project/requests/) and [pandas](https://pypi.org/project/pandas/) to load lakes from [lakelevels.info](https://www.lakelevels.info).
2. Only makes one request per day (set to 6am).
3. When the lake name is changed, loads the chosen lake's data from the cached table.
4. Creates required template sensors automatically.
5. Includes YAML for Dashboard card and daily notifications.

Prerequisites:
1. Download and install [HACS](https://github.com/hacs). Restart HASS.
2. Using HACS, download [Pyscript](https://github.com/custom-components/pyscript). Restart HASS.

Instructions:
1. Create a new dropdown: Settings > Devices & Services > Create Helper > Dropdown  
   **Name**: Lake  
   **Icon**: mdi:format-list-bulleted  
   **Options**: Names of lakes you want, taken from [here](https://www.lakelevels.info). State is not required unless a lake's name is not unique.  
   **Example**: Chickamauga  
   **Example**: Cherokee (TX)  
1. Download lakelevel.py and copy it to your HASSconfig/pyscript folder.
2. Reload Pyscript. The four sensors should now have the new values.
3. Add a new card to your dash using the YAML from [card_config.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/card_config.yaml)
4. Optionally, add a new automation using the YAML from [notifications.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/notifications.yaml).

Known Bugs:
1. Unique ID's are not set for sensors, so the sensors can't be customized in the UI. Make changes within the script.

To Do:
1. Fix bugs.
2. Add ability to import via HACS custom repo.