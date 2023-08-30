
# Developed by Mingyu Wang
# Updated on: 8/30/2023

# // Copyright (c) 2022-2023 Mingyu Wang
# // Distributed under the MIT software license, see the accompanying
# // file LICENSE or http://www.opensource.org/licenses/mit-license.php.

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
df = df.drop_duplicates(subset=['time_stamp'], keep = 'first', inplace = False)

# Rename the column 'time_stamp' to be 'datetime'
df.rename(columns = {'time_stamp': 'datetime'}, inplace = True)

# Make the type of column 'datetime' to be DATETIME in a yyyy/mm/dd hh/MM/ss format
df["datetime"] = pd.to_datetime(df["datetime"], format='%Y-%m-%d %H:%M:%S')

# Set the column 'datetime' to be the index
df = df.set_index('datetime', inplace=False)
print(df)

# Add the missing datetime/timestamp
df = df.resample('10T').mean()

# Write to csv (Have to change the file path to your own device)
df.to_csv("C:\\Users\\OneDrive\\Desktop\\WIFIappend\\Device1.csv")


















