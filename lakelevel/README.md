This script updates four HASS sensors to show the Chickamauga Lake level.

![Screenshot of the completed product in HASS](https://github.com/scottocs11/hass/blob/main/lakelevel/images/lakelevelcard.png)

Prerequisites:
1. Download and install [HACS](https://github.com/hacs). Restart HASS.
2. Using HACS, download [Pyscript](https://github.com/custom-components/pyscript). Restart HASS.

Instructions:
1. Download lakelevel.py and copy it to your <HASSconfig>/pyscript folder.
2. Reload Pyscript. The four sensors should now have the new values.
3. Add a new card to your dash using the YAML from [card_config.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/card_config.yaml)
4. Add a new automation using the YAML from [notifications.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/notifications.yaml).
8.

Known Bugs:
1. Hass' INPUT SELECT removes one of the two required spaces between the lake name and the state.
2. Unique ID's are not set for sensors.

To Do:
1. Create and set the dropdown menu with all state names, or text box to type the name. Unfortunately, HASS doesn't have a way to autocomplete the lake name.