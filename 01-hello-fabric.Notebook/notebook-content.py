# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a68737fe-737b-4575-ac5c-58e2ebe37d1f",
# META       "default_lakehouse_name": "workshop_lakehouse",
# META       "default_lakehouse_workspace_id": "f43b0628-2f01-433b-bca7-1e89655c79b2",
# META       "known_lakehouses": [
# META         {
# META           "id": "a68737fe-737b-4575-ac5c-58e2ebe37d1f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # My First Fabric Notebook
# 
# This notebook is part of the Fabric DevOps Workshop.
# 
# ## Purpose
# Learning how to use source control with Microsoft Fabric.

# CELL ********************

# Simple PySpark example
print("Hello from Fabric!")

# Display current date
from datetime import datetime
print(f"Notebook run at: {datetime.now()}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# New feature: Calculate something
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"The sum of {numbers} is {total}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# New feature in development - not yet deployed
print("This is a new feature!")
print("It's only in dev - production doesn't have this yet.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Create a simple DataFrame
data = [
    ("Alice", 28),
    ("Bob", 35),
    ("Charlie", 42)
]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)

# Write to the default lakehouse
df.write.mode("overwrite").format("delta").saveAsTable("people")

print("✅ Data written to 'people' table in the default lakehouse!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read from the default lakehouse
df = spark.read.table("people")

# Display the data
display(df)

print(f"✅ Read {df.count()} rows from the default lakehouse!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
