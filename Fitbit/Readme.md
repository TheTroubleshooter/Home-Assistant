-------------------------------------------------------
My system:
Home Assistant Version: 2021.12.10
Account1: Charge 2 & Arai scale user
Account2: Arai scale user
-------------------------------------------------------

The following instructions will walk you through configuring a single Fitbit account on Home Assistant using the contents of the "Fitbit1" folder. For multiple Fitbit accounts just repeat the process using the contents of the Fitbit2, Fitbit3, Fitbit4, Fitbit5 folders. I have tested this with two Fitbit accounts and it works flawlessly.

Instructions:
1. Download the contents of the "Fitbit1" folder to a separate folder on your computer.
2. Create a folder named "fitbit1" in the config/custom_components folder of Home Assistant. Put all of the files except the sensor.yaml file that you downloaded in the previous step into the "fitbit1" folder. 
3. Restart Home Assistant
4. Depending on how you are adding sensors you will need to update your configuration.yaml or sensor.yaml file with the new sensor information. From the sensor.yaml that you downloaded in step 1 copy the contents of that file and add it to configuration.yaml or sensor.yaml. All of the current sensors available will be added unless you customize this step. If you want to just add the sensors you need then remove the unnecessary sensors before copying to your configuration.yaml or sensor.yaml.
5. Restart Home Assistant
6. You should now see a Notification to setup the Fitbit sensor in the Notifications section of the menu. Click Notification then click Configure and follow the steps to create app on dev.fitbit.com. Make sure that the callback address looks like this "https://YOURDOMAIN:8123/api/fitbit1/callback". <--This will change depending on the provided folder you are using fitbit1, fitbit2, fitbit3, fitbit4, fitbit5.
7. You should now see a second Notification to setup the Fitbit sensor in the Notifications section of the menu. Click Notification then click Configure and follow steps to authorize Home Assistant to access your fitbit information.
8. Open Entities and check to see if you see the new sensors. Do a search in Entities for "sensor.fitbit1" to see the sensors populated. 
9. For multiple Fitbit accounts repeat the process using the provided Fitbit2, Fitbit3, Fitbit4, Fitbit5 folders.

Other: 
1. For the dev.fitbit.com part of the setup use a browser that you are ok with clearing the browser data. The reason why is that you should clear the browser between adding additional accounts. I found that doing this prevented any errors I would get when adding the second account.
2. To customize the sensor names from the set names of fitbit1, fitbit2, fitbit3, fitbit4, fitbit5 use the following steps. It is best to use Notepad++ for this. In the "fitbit1" folder open the const.py file and do a find/replace for this name="Fitbit1 and replace it with the name you want the sensor to be. For example if you want the name to be john replace the name to be name="john and the sensors names will be sensor.john_weight for the weight sensor.
3. To customize the config file name saved in the /config folder from the set name of fitbit1.conf open the const.py file and find the section "FITBIT_CONFIG_FILE: Final = "fitbit1.conf" and change it to your preferd name. For example if you want john as the config file name change it to "fitbit_john.conf"
4. Customizations should be done prior to placing the files into your Home Assistant installation.
5. Notepad++ with the compare plug-in is recommended for file edits.
6. Cloud Polling issues. I have not confirmed this is a real issue but if you experiance cloud polling issues with multiple accounts where entities do not get updated info try offsetting the cloud polling time by one minute for each account added. For example the default cloud polling time is 30 minutes so for fitbit1 leave it at 30 minutes but set fitbit2 to 31 minutes. The cloud polling time can be found sensor.py file in each fitbit folder. This is the section you need to update: "SCAN_INTERVAL: Final = datetime.timedelta(minutes=31)"
