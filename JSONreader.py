import pandas as pd

json_file = "product_data.json"  # Path to the JSON file

# Read the JSON file into a pandas DataFrame
df = pd.read_json(json_file)

# Select the desired columns
selected_columns = ["RelativePrice"]
df_selected = df[selected_columns]

# Set display options
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 100)  # Set the display width to a large value

# Display the selected columns
print(df_selected)
