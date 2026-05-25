This script pulls lake level info from [lakelevels.info](https://www.lakelevels.info) and updates HASS sensors with the data.

<img src="https://github.com/scottocs11/hass/blob/main/lakelevel/images/lakelevelcard.png" width="400"/>

Features:
1. Uses Python libraries [requests](https://pypi.org/project/requests/) and [pandas](https://pypi.org/project/pandas/) to load lakes from a table from [lakelevels.info](https://www.lakelevels.info).
2. Only makes one request per day (set to 6am).
3. When the lake name is changed, loads the chosen lake's data from the cached table.
4. Creates required template sensors automatically.
5. Includes YAML for Dashboard card and daily notifications.

Prerequisites:
1. Download and install [HACS](https://github.com/hacs). Restart HASS.
2. Using HACS, download [Pyscript](https://github.com/custom-components/pyscript). Restart HASS.

Instructions:
1. In HASS -> Integrations, Create a new **Input select (helper)**.  
   **Name**: Lake  
   **Icon**: mdi:format-list-bulleted  
   **Options**: Your lake names, taken from [here](https://www.lakelevels.info). If a lake's name is not unique, you must format it like below, with **TWO** spaces between the name and state. (See Known bug #1)  
   **Example**: Cherokee  (tn)
1. Download lakelevel.py and copy it to your HASSconfig/pyscript folder.
2. Reload Pyscript. The four sensors should now have the new values.
3. Add a new card to your dash using the YAML from [card_config.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/card_config.yaml)
4. Optionally, add a new automation using the YAML from [notifications.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/notifications.yaml).

Known Bugs:
1. HASS' [Input Select](https://www.home-assistant.io/integrations/input_select/) removes one of the two required spaces between the lake name and the state, so until I figure that out, it can't perform exact name searches, only 'contains'. This means only the first of any unique lake name can be used.
2. Unique ID's are not set for sensors, so the sensors can't be customized in the UI unless you add the sensors to configuration yaml. You may as well customize them within the script.

To Do:
1. Fix bugs.