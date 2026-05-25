This script updates four HASS sensors to show the Chickamauga Lake level.

![Screenshot of the completed product in HASS](https://github.com/scottocs11/hass/blob/main/lakelevel/images/chiclake.png)

Instructions:
1. Create four Helper Template Sensors via Settings -> Helpers -> Create Helper -> Template -> Sensor.

| Name | State | Unit of Measurement | State Class |
| :--- | :--- | :--- | :--- |
| Chickamauga Lake Full | {{0}} | ft | Measurement |
| Chickamauga Lake Level | {{0}} | ft | Measurement |
| Chickamauga Level Difference | {{0}} | ft | Measurement |
| Chickamauga Refresh Time | {{0}} |  |  |

2. Download and install [HACS](https://github.com/hacs) if not already installed. Restart HASS.
3. Using HACS, download [Pyscript](https://github.com/custom-components/pyscript). Restart HASS.
4. Download lakelevel.py and copy it to your <HASSconfig>/pyscript folder.
5. Reload Pyscript
6. The four sensors should now have the new values.
7. Add a new automation using the YAML from [notifications.yaml](https://github.com/scottocs11/hass/blob/main/lakelevel/notifications.yaml).