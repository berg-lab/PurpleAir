
# Developed by Mingyu Wang
# Updated on: 8/30/2023

# // Copyright (c) 2022-2023 Mingyu Wang
# // Distributed under the MIT software license, see the accompanying
# // file LICENSE or http://www.opensource.org/licenses/mit-license.php.

from datetime import datetime
import pandas as pd
import glob
import os

# Merging the files (Have to change the file path to your own device)
joined_files = os.path.join("C:\\Users\\OneDrive\\Desktop\\Device1EachFile", "*.csv")

# A list of all joined files is returned
joined_list = glob.glob(joined_files)

# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)

# Drop the duplicated lines (In the raw files, the last line of the 1st file is the same as the first line of the 2nd file, and so on)
df = df.drop_duplicates(subset=['UTCDateTime'], keep = 'first', inplace = False)

# Change "UTCDateTime" to the format which can be used as datetime index
df["UTCDateTime"] = list(map(lambda x: datetime.strptime(x,'%Y/%m/%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'), df['UTCDateTime']))

# Rename the column 'time_stamp' to be 'datetime'
df.rename(columns = {'UTCDateTime': 'datetime'}, inplace = True)

# Make the type of column 'datetime' to be DATETIME in a yyyy/mm/dd hh/MM/ss format
df["datetime"] = pd.to_datetime(df["datetime"], format='%Y-%m-%d %H:%M:%S')

# Set the column 'datetime' to be the index
df = df.set_index('datetime', inplace=False)
print(df)

# Delete any columns that you don't want to have
df = df.drop(['mac_address', 'firmware_ver', 'hardware', 'current_dewpoint_f', 'adc', 'mem', 'rssi', 'uptime', 'pm2.5_aqi_cf_1', 'pm2.5_aqi_atm', 'pm2.5_aqi_cf_1_b', 'pm2.5_aqi_atm_b', 'gas'], axis=1)
print(df)
df.to_csv("C:\\Users\\91763\\OneDrive\\Desktop\\Insung\\PA003.csv")

# Add the missing datetime/timestamp
df = df.resample('10T').mean()
print(df)

# Rename the Columns, double check which column should be which
df = df.rename(columns={df.columns[3]: 'pm1.0_cf_1_a'})
df = df.rename(columns={df.columns[0]: 'temperature'})
df = df.rename(columns={df.columns[1]: 'humidity'})
df = df.rename(columns={df.columns[4]: 'pm2.5_cf_1_a'})
df = df.rename(columns={df.columns[5]: 'pm10.0_cf_1_a'})
df = df.rename(columns={df.columns[6]: 'pm1.0_atm_a'})
df = df.rename(columns={df.columns[7]: 'pm2.5_atm_a'})
df = df.rename(columns={df.columns[8]: 'pm10.0_atm_a'})
df = df.rename(columns={df.columns[9]: '0.3_um_count_a'})
df = df.rename(columns={df.columns[10]: '0.5_um_count_a'})
df = df.rename(columns={df.columns[11]: '1.0_um_count_a'})
df = df.rename(columns={df.columns[12]: '2.5_um_count_a'})
df = df.rename(columns={df.columns[13]: '5.0_um_count_a'})
df = df.rename(columns={df.columns[14]: '10.0_um_count_a'})
df = df.rename(columns={df.columns[15]: 'pm1.0_cf_1_b'})
df = df.rename(columns={df.columns[16]: 'pm2.5_cf_1_b'})
df = df.rename(columns={df.columns[17]: 'pm10.0_cf_1_b'})
df = df.rename(columns={df.columns[18]: 'pm1.0_atm_b'})
df = df.rename(columns={df.columns[19]: 'pm2.5_atm_b'})
df = df.rename(columns={df.columns[20]: 'pm10.0_atm_b'})
df = df.rename(columns={df.columns[21]: '0.3_um_count_b'})
df = df.rename(columns={df.columns[22]: '0.5_um_count_b'})
df = df.rename(columns={df.columns[23]: '1.0_um_count_b'})
df = df.rename(columns={df.columns[24]: '2.5_um_count_b'})
df = df.rename(columns={df.columns[25]: '5.0_um_count_b'})
df = df.rename(columns={df.columns[26]: '10.0_um_count_b'})

# Calculate the average of channel A & B
df['pm1.0_cf_1'] = (df['pm1.0_cf_1_a'] + df['pm1.0_cf_1_b'])/2
df['pm2.5_cf_1'] = (df['pm2.5_cf_1_a'] + df['pm2.5_cf_1_b'])/2
df['pm10.0_cf_1'] = (df['pm10.0_cf_1_a'] + df['pm10.0_cf_1_b'])/2
df['pm1.0_atm'] = (df['pm1.0_atm_a'] + df['pm1.0_atm_b'])/2
df['pm2.5_atm'] = (df['pm2.5_atm_a'] + df['pm2.5_atm_b'])/2
df['pm10.0_atm'] = (df['pm10.0_atm_a'] + df['pm10.0_atm_b'])/2
df['0.3_um_count'] = (df['0.3_um_count_a'] + df['0.3_um_count_b'])/2
df['0.5_um_count'] = (df['0.5_um_count_a'] + df['0.5_um_count_b'])/2
df['1.0_um_count'] = (df['1.0_um_count_a'] + df['1.0_um_count_b'])/2
df['2.5_um_count'] = (df['2.5_um_count_a'] + df['2.5_um_count_b'])/2
df['5.0_um_count'] = (df['5.0_um_count_a'] + df['5.0_um_count_b'])/2
df['10.0_um_count'] = (df['10.0_um_count_a'] + df['5.0_um_count_b'])/2

# Calculate the ALT algorithm
df['pm2.5_alt'] = 3*(0.00030418*(df['0.3_um_count'] - df['0.5_um_count']) + 0.0018512 *(df['0.5_um_count'] - df['1.0_um_count']) + 0.02069706 * (df['1.0_um_count'] - df['2.5_um_count']))
df['pm2.5_alt_a'] = 3*(0.00030418*(df['0.3_um_count_a'] - df['0.5_um_count_a']) + 0.0018512 *(df['0.5_um_count_a'] - df['1.0_um_count_a']) + 0.02069706 * (df['1.0_um_count_a'] - df['2.5_um_count_a']))
df['pm2.5_alt_b'] = 3 *(0.00030418*(df['0.3_um_count_b'] - df['0.5_um_count_b']) + 0.0018512 *(df['0.5_um_count_b'] - df['1.0_um_count_b']) + 0.02069706 * (df['1.0_um_count_b'] - df['2.5_um_count_b']))


# Write to csv (Have to change the file path to your own device)
df.to_csv("C:\\Users\\OneDrive\\Desktop\\SDappend\\Device1.csv")


















