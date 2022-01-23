These instructions the steps to configure a single Fitbit account using the provided files in the fitbit1 folder. For multiple accounts repeat the steps using the fitbit2 name instead. For three or more accounts you will need to alter the files provided.

Instructions:
1. Download the three folders and their contents to separate folders on your computer.
2. The contents of the "Fitbit - Core Files (Untouched)" should be used to compare against the contents of the Fitbit1 & Fitbit2 folders. Use Notepad++ with the compare plug-in to compare what has been changed. For example for Fitbit1 if you would like to have the sensors display your name instead of sensor.fitbit1.weight you can edit the "name="Fitbit1" entries for all of settings under "FITBIT_RESOURCES_LIST:" in the const.py to change the name presented in Home Assistant.
3. Create a folder named "fitbit1" in the config/custom_components folder of HA and place the files from the fitbit1 folder into it.
4. Restart Home Assistant
5. Depending on how you are applying your sensors (configuration.yaml or sensor.yaml) add the sensor information provided in the sensor.yaml from the fitbit1 folder.
6. Restart Home Assistant
7. You should now see a new Notification to setup the fitbit1 sensor. Click Configure and follow the steps to create app on dev.fitbit.com. Make sure that the callback address looks like this "https://YOURDOMAIN:8123/api/fitbit1/callback"
8. After you have completed the first configuration step you should see a second notification. Click configure and follow steps to authorize HA to access fitbit information.
9. You should now see sensors names with "sensor.fitbit1.xxxxx"
10. For second account repeat steps using the contents of fitbit2 folder.

Suggestion:
1. for the dev.fitbit.com part of the setup use a browser that you are ok with clearing the browser data. The reason why is that you should clear the browser between the steps needed on the dev.fitbit.com website. 
