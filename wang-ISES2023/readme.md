# ISES 2023 Purple Air Data Download

## Prerequisites
The sensor index is an identifying number unique to each sensor. It is 4-6 characters long.

* To find the sensor index, locate your sensor on the PurpleAir map and click or tap its Map Marker. Then, view the URL in your browser. You will find the sensor index after the text `“select=”`.
* The index can also be found in the registration confirmation email received after your sensor was registered. To locate it, open your registration confirmation email and scroll down until you see `“Useful links”`. In the `“Download data”` link, the sensor index is the number that follows the text `“show=”`.
* On top of sensor indexes, every PurpleAir sensor has its own unique sensor read key. This key is a special code that allows you to view its data if it is private. If the sensors you are collecting data from are public, nothing needs to be entered into this field.
* Locate the section of the URL that says, `‘key=’`, the sensor read key appears after `‘=’`.
* See the descriptions in [Link 1](https://community.purpleair.com/t/making-api-calls-with-the-purpleair-api/180) and [Link 2](https://community.purpleair.com/t/sensor-index/4000)


## Instruction
* Make API calling to download PurpleAir data from cloud with using `PurpleAir API Calling.py`
* Append files downloaded from API calling with using `PurpleAir WiFi Data Append.py`
* Append files downloaded from SD card and decoding the file struction to be the same as the WiFi data file with using `PurpleAir SD Data append.py`

## Cite
Wang, M., Stephens, B., Heidarinejad, M., Kang, I., Singh, A., Rodriguez, R., Chang, D., Solomon, G., Rubinstein, I., Elfessi, Z., Jagota, K., and Karpen, N., "Experiences with low-cost optical particle sensors for indoor exposure assessment in residential field studies, ORAL presentation at the ISES 2023 Annual Meeting, August 27-31 in Chicago, Illinois.

