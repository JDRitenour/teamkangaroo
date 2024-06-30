# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# Originating Pieces files - merge these two
OriginatingPieces1 = pd.read_csv("C:/Users/andie/OneDrive/Documents/Capstone/Mail_v2/Piece Output v2/Originating Pieces pt.1 v2.csv")
OriginatingPieces2 = pd.read_csv("C:/Users/andie/OneDrive/Documents/Capstone/Mail_v2/Piece Output v2/Originating Pieces pt.2 v2.csv")


#------- Filter out data by ACTUAL_DLVRY_DATE that isn't between 01/08/24 to 01/21/24
op_january = OriginatingPieces1[(OriginatingPieces1['ACTUAL_DLVRY_DATE'] > "2024-01-08") & (OriginatingPieces1['ACTUAL_DLVRY_DATE'] < "2024-01-21")]
op2_january = OriginatingPieces2[(OriginatingPieces2['ACTUAL_DLVRY_DATE'] > "2024-01-08") & (OriginatingPieces2['ACTUAL_DLVRY_DATE'] < "2024-01-21")]

# Clean the two data sets
noNull_op1 = op_january.dropna(how='any',axis=0) 
clean_op1 = noNull_op1.drop_duplicates()

noNull_op2 = op2_january.dropna(how='any',axis=0)
clean_op2 = noNull_op2.drop_duplicates()

# Add columns that determine if the mail was On Time Exactly, Early, or Late
clean_op1['OnTimeExactly'] = np.where(clean_op1['ACTUAL_DLVRY_DATE'] == clean_op1['EXPECTED_DELIVERY_DATE'], True, False)
clean_op1['Early'] = np.where(clean_op1['ACTUAL_DLVRY_DATE'] < clean_op1['EXPECTED_DELIVERY_DATE'], True, False)
clean_op1['Late'] = np.where(clean_op1['ACTUAL_DLVRY_DATE'] > clean_op1['EXPECTED_DELIVERY_DATE'], True, False)

clean_op2['OnTimeExactly'] = np.where(clean_op2['ACTUAL_DLVRY_DATE'] == clean_op2['EXPECTED_DELIVERY_DATE'], True, False)
clean_op2['Early'] = np.where(clean_op2['ACTUAL_DLVRY_DATE'] < clean_op2['EXPECTED_DELIVERY_DATE'], True, False)
clean_op2['Late'] = np.where(clean_op2['ACTUAL_DLVRY_DATE'] > clean_op2['EXPECTED_DELIVERY_DATE'], True, False)


# Combine the datasets with only data between Jan 8th and Jan 21st of 2024
originatingPieces_stormPeriod = pd.concat([clean_op1, clean_op2])

# Compare the delivery status of the mail (Late vs. Ontime / Early)
originating_late = originatingPieces_stormPeriod['Late'].values.sum()
originating_early = originatingPieces_stormPeriod['Early'].values.sum()
originating_ontime = originatingPieces_stormPeriod['OnTimeExactly'].values.sum()
print("Late mail: "+ str(originating_late) + ", Early Mail: "+ str(originating_early)+", On Time Mail: "+ str(originating_ontime))
# ratio of late vs rest
originating_late_ratio = originating_late / (originating_early + originating_ontime)
print("Ratio of Late Mail vs. Early or On Time mail: " + str("%f" % originating_late_ratio))

# distribution of mail shape by lateness
originatingPieces_stormPeriod['MAIL_SHAPE'].value_counts()

op_shape = originatingPieces_stormPeriod.groupby(by=["MAIL_SHAPE", "Late"]).size() # True = Late, False = either Early or On Time Exactly
print(op_shape)

# Mail Class
originatingPieces_stormPeriod['MAIL_CLASS'].value_counts()
op_class = originatingPieces_stormPeriod.groupby(by=["MAIL_CLASS", "Late"]).size() # True = Late, False = either Early or On Time Exactly
print(op_class)

#ORIGIN_FACILITY
originatingPieces_stormPeriod['ORIGIN_FACILITY'].value_counts()
op_originFacility = originatingPieces_stormPeriod.groupby(by=["ORIGIN_FACILITY", "Late"]).size() # True = Late, False = either Early or On Time Exactly
print(op_originFacility)


# Convert delivery date columns to the 'date' data type
originatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'] = pd.to_datetime(originatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'])
print(originatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'].head())
originatingPieces_stormPeriod['EXPECTED_DELIVERY_DATE'] = pd.to_datetime(originatingPieces_stormPeriod['EXPECTED_DELIVERY_DATE'])

# Difference between EXPECTED and ACTUAL delivery dates - Positive values indicate LATE deliveries
originatingPieces_stormPeriod['Difference'] = (originatingPieces_stormPeriod['ACTUAL_DLVRY_DATE'] - originatingPieces_stormPeriod['EXPECTED_DELIVERY_DATE']).dt.days
#print(originatingPieces_stormPeriod.head(10))

# Average days late a piece of mail arrives
late_deliveries = originatingPieces_stormPeriod.loc[originatingPieces_stormPeriod.Late]
latemean = late_deliveries['Difference'].mean()
print("The mean for mail delivered late is: " + str("%f" % latemean) + " days after expected delivery date")

# Differences and their Count by Mail Class
late_by_class = late_deliveries.groupby(by=["MAIL_CLASS", "Difference"]).size() # True = Late, False = either Early or On Time Exactly
print(late_by_class)
# late_class_mean = late_deliveries.groupby(by=["MAIL_CLASS", "Difference"])
# print(late_class_mean.mean())

# Differences and their Count by Mail Shape
late_by_shape = late_deliveries.groupby(by=["MAIL_SHAPE", "Difference"]).size() # True = Late, False = either Early or On Time Exactly
print(late_by_shape)
