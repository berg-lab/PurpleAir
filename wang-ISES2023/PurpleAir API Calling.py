
# Developed by Mingyu Wang
# Updated on: 8/30/2023

# // Copyright (c) 2022-2023 Mingyu Wang
# // Distributed under the MIT software license, see the accompanying
# // file LICENSE or http://www.opensource.org/licenses/mit-license.php.

from purpleair import PurpleAir
from datetime import datetime
import pandas as pd
import itertools

# Replace API KEY by PA API in ''
p = PurpleAir('API KEY')

# Change the sensor index, and change the read_key of this sensor if the sensor was set to private. If the sensor was set to public, just delete ', read_key='XXXXXXXXXXXXXXXX''
SensorData = p.get_sensor_data('XXXXXX', read_key='XXXXXXXXXXXXXXXX')

# Check if sensors are still working (You can see the 'last edit' timestamp after print. Use that timestamp in the 'for' loop below)
print(SensorData)

# Input the start timestamp(1st) and the end timestamp(2nd), the step is 258600 (3days). If you don't put the 'step' here, you will only get one 3-day-data file
for i in range(1682467200, 1691179260, 258600):

    # Change the sensor index and read key if the sensor was set to private. If the sensor was set to public, just delete ', read_key='XXXXXXXXXXXXXXXX''. Delete anything the field if you don't want that data
    df1 = p.get_sensor_history(sensor_index='XXXXXX', read_key='XXXXXXXXXXXXXXXX', fields=("humidity","temperature","pressure","pm2.5_alt","pm2.5_alt_a","pm2.5_alt_b","0.3_um_count","0.3_um_count_a","0.3_um_count_b","0.5_um_count","0.5_um_count_a","0.5_um_count_b","1.0_um_count","1.0_um_count_a","1.0_um_count_b","2.5_um_count","2.5_um_count_a","2.5_um_count_b","5.0_um_count","5.0_um_count_a","5.0_um_count_b","10.0_um_count","10.0_um_count_a","10.0_um_count_b","pm1.0_cf_1","pm1.0_cf_1_a","pm1.0_cf_1_b","pm1.0_atm","pm1.0_atm_a","pm1.0_atm_b","pm2.5_atm","pm2.5_atm_a","pm2.5_atm_b","pm2.5_cf_1","pm2.5_cf_1_a","pm2.5_cf_1_b","pm10.0_atm","pm10.0_atm_a","pm10.0_atm_b","pm10.0_cf_1","pm10.0_cf_1_a","pm10.0_cf_1_b"), start_timestamp=i)

    del df1['api_version'], df1['time_stamp'], df1['sensor_index'], df1['start_timestamp'], df1['end_timestamp'], df1[
        'average'], df1['fields']

    # Change the data format from dict to list then to dataframe
    df = list(df1.values())
    out = list(itertools.chain.from_iterable(df))
    out1 = list(itertools.chain.from_iterable(out))

    # If you change the 'fileds' before, also you have to change here
    df1 = pd.DataFrame(out, columns=['time_stamp', "humidity","temperature","pressure","pm2.5_alt","pm2.5_alt_a","pm2.5_alt_b","0.3_um_count","0.3_um_count_a","0.3_um_count_b","0.5_um_count","0.5_um_count_a","0.5_um_count_b","1.0_um_count","1.0_um_count_a","1.0_um_count_b","2.5_um_count","2.5_um_count_a","2.5_um_count_b","5.0_um_count","5.0_um_count_a","5.0_um_count_b","10.0_um_count","10.0_um_count_a","10.0_um_count_b","pm1.0_cf_1","pm1.0_cf_1_a","pm1.0_cf_1_b","pm1.0_atm","pm1.0_atm_a","pm1.0_atm_b","pm2.5_atm","pm2.5_atm_a","pm2.5_atm_b","pm2.5_cf_1","pm2.5_cf_1_a","pm2.5_cf_1_b","pm10.0_atm","pm10.0_atm_a","pm10.0_atm_b","pm10.0_cf_1","pm10.0_cf_1_a","pm10.0_cf_1_b"])

    df1.sort_values(by=['time_stamp'], inplace=True)

    df1 = df1.set_index(pd.to_datetime(df1['time_stamp'], unit='s'))

    print(df1)
    # Change it to the path on your end
    df1.to_csv('C:\\Users\\OneDrive\\PurpleAir\\Device1\\Device1_' + str(datetime.fromtimestamp(i).strftime('%y%m%d')) + '.csv')

