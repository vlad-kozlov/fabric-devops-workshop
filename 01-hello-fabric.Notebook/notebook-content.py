# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
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
