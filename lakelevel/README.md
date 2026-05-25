This script pulls lake level info from [lakelevels.info](https://www.lakelevels.info/updates) and updates HASS sensors with the data.

<img src="https://github.com/scottocs11/hass/blob/main/lakelevel/images/lakelevelcard.png" width="400"/>

Prerequisites:
1. Download and install [HACS](https://github.com/hacs). Restart HASS.
2. Using HACS, download [Pyscript](https://github.com/custom-components/pyscript). Restart HASS.

Instructions:
1. Download lakelevel.py and copy it to your <HASSconfig>/pyscript folder.
2. Reload Pyscript. The four sensors should now have the new values.
3. Add a new card to your dash using the YAML from [card_config.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/card_config.yaml)
4. Optionally, add a new automation using the YAML from [notifications.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/notifications.yaml).

Known Bugs:
1. Hass' [Input Select](https://www.home-assistant.io/integrations/input_select/) removes one of the two required spaces between the lake name and the state, so until I figure that out, I can't perform exact name searches, only 'contains'.
2. Unique ID's are not set for sensors.

To Do:
1. Create and set the dropdown menu with all state names, or text box to type the name. Unfortunately, HASS doesn't have a way to autocomplete the lake name.