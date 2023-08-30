# Prerequisites
The sensor index is an identifying number unique to each sensor. It is 4-6 characters long.

• To find the sensor index, locate your sensor on the PurpleAir map and click or tap its Map Marker. Then view the URL in your browser. You will find the sensor index after the text “select=”.

• The index can also be found in the registration confirmation email received after your sensor was registered. To locate it, open your registration confirmation email and scroll down until you see “Useful links”. In the “Download data” link, the sensor index is the number that follows the text “show=”.

On top of sensor indexes, every PurpleAir sensor has its own unique sensor read key. This key is a special code that allows you to view its data if it is private. If the sensors you are collecting data from are public, nothing needs to be entered into this field.
Locate the section of the URL that says, ‘key=’, the sensor read key appears after ‘=’.
https://community.purpleair.com/t/making-api-calls-with-the-purpleair-api/180
https://community.purpleair.com/t/sensor-index/4000

# Instruction
Make API calling to download PurpleAir data from cloud, use PurpleAir API Calling.py

Append files downloaded from API calling, use PurpleAir WiFi Data Append.py

Append files downloaded from SD card and decoding the file struction to be the same as the WiFi data file, use PurpleAir SD Data append.py

