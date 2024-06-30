# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


# Destinating Pieces files - merge these two datasets
DestinatingPieces1 = pd.read_csv("C:/Users/andie/OneDrive/Documents/Capstone/Mail_v2/Piece Output v2/Destinating Pieces pt.1 v2.csv")
DestinatingPieces2 = pd.read_csv("C:/Users/andie/OneDrive/Documents/Capstone/Mail_v2/Piece Output v2/Destinating Pieces pt.2 v2.csv")

#------- Filter out data by ACTUAL_DLVRY_DATE that isn't between 01/08/24 to 01/21/24
dp_january = DestinatingPieces1[(DestinatingPieces1['ACTUAL_DLVRY_DATE'] > "2024-01-08") & (DestinatingPieces1['ACTUAL_DLVRY_DATE'] < "2024-01-21")]
dp2_january = DestinatingPieces2[(DestinatingPieces2['ACTUAL_DLVRY_DATE'] > "2024-01-08") & (DestinatingPieces2['ACTUAL_DLVRY_DATE'] < "2024-01-21")]

# Clean the two data sets
noNull_dp1 = dp_january.dropna(how='any',axis=0) 
clean_dp1 = noNull_dp1.drop_duplicates()

noNull_dp2 = dp2_january.dropna(how='any',axis=0)
clean_dp2 = noNull_dp2.drop_duplicates()

# Add columns that determine if the mail was On Time Exactly, Early, or Late
clean_dp1['OnTimeExactly'] = np.where(clean_dp1['ACTUAL_DLVRY_DATE'] == clean_dp1['EXPECTED_DELIVERY_DATE'], True, False)
clean_dp1['Early'] = np.where(clean_dp1['ACTUAL_DLVRY_DATE'] < clean_dp1['EXPECTED_DELIVERY_DATE'], True, False)
clean_dp1['Late'] = np.where(clean_dp1['ACTUAL_DLVRY_DATE'] > clean_dp1['EXPECTED_DELIVERY_DATE'], True, False)

clean_dp2['OnTimeExactly'] = np.where(clean_dp2['ACTUAL_DLVRY_DATE'] == clean_dp2['EXPECTED_DELIVERY_DATE'], True, False)
clean_dp2['Early'] = np.where(clean_dp2['ACTUAL_DLVRY_DATE'] < clean_dp2['EXPECTED_DELIVERY_DATE'], True, False)
clean_dp2['Late'] = np.where(clean_dp2['ACTUAL_DLVRY_DATE'] > clean_dp2['EXPECTED_DELIVERY_DATE'], True, False)


# Combine the datasets with only data between Jan 8th and Jan 21st of 2024
destinatingPieces_stormPeriod = pd.concat([clean_dp1, clean_dp2])

# Compare the delivery status of the mail (Late vs. Ontime / Early)
destinating_late = destinatingPieces_stormPeriod['Late'].values.sum()
destinating_early = destinatingPieces_stormPeriod['Early'].values.sum()
destinating_ontime = destinatingPieces_stormPeriod['OnTimeExactly'].values.sum()
print("Late mail: "+ str(destinating_late) + ", Early Mail: "+ str(destinating_early)+", On Time Mail: "+ str(destinating_ontime))
# ratio of late vs rest
destinating_late_ratio = destinating_late / (destinating_early + destinating_ontime)
print("Ratio of Late Mail vs. Early or On Time mail: " + str("%f" % destinating_late_ratio))

# distribution of mail shape by lateness
destinatingPieces_stormPeriod['MAIL_SHAPE'].value_counts()

dp_grouped = destinatingPieces_stormPeriod.groupby(by=["MAIL_SHAPE", "Late"]).size() # True = Late, False = either Early or On Time Exactly
print(dp_grouped)

# Mail Class
destinatingPieces_stormPeriod['MAIL_CLASS'].value_counts()
dp_class = destinatingPieces_stormPeriod.groupby(by=["MAIL_CLASS", "Late"]).size() # True = Late, False = either Early or On Time Exactly
print(dp_class)

#EXPECTED_DESTINATION_FACILITY
destinatingPieces_stormPeriod['EXPECTED_DESTINATION_FACILITY'].value_counts()
dp_destFacility = destinatingPieces_stormPeriod.groupby(by=["EXPECTED_DESTINATION_FACILITY", "Late"]).size() # True = Late, False = either Early or On Time Exactly
print(dp_destFacility)

# Convert delivery date columns to the 'date' data type
destinatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'] = pd.to_datetime(destinatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'])
print(destinatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'].head())
destinatingPieces_stormPeriod['EXPECTED_DELIVERY_DATE'] = pd.to_datetime(destinatingPieces_stormPeriod['EXPECTED_DELIVERY_DATE'])

# Difference between EXPECTED and ACTUAL delivery dates - Positive values indicate LATE deliveries
destinatingPieces_stormPeriod['Difference'] = (destinatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'] - destinatingPieces_stormPeriod['EXPECTED_DELIVERY_DATE']).dt.days
#print(destinatingPieces_stormPeriod.head(10))

# Average days late a piece of mail arrives
late_deliveries = destinatingPieces_stormPeriod.loc[destinatingPieces_stormPeriod.Late]
latemean = late_deliveries['Difference'].mean()
print("The mean for mail delivered late is: " + str("%f" % latemean) + " days after expected delivery date")

# Differences and their Count by Mail Class
late_by_class = late_deliveries.groupby(by=["MAIL_CLASS", "Difference"]).size() # True = Late, False = either Early or On Time Exactly
pd.set_option('display.max_rows', 250)
print(late_by_class)
# late_class_mean = late_deliveries.groupby(by=["MAIL_CLASS", "Difference"])
# print(late_class_mean.mean())

# Differences and their Count by Mail Shape
late_by_shape = late_deliveries.groupby(by=["MAIL_SHAPE", "Difference"]).size() # True = Late, False = either Early or On Time Exactly
print(late_by_shape)
