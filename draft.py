# import pandas as pd
# import json

file_path = '/Users/yu/Documents/Applicant_2025/InveriteInfos-20250227_1033.txt'

# # Step 1: Read the JSON formatted text file
# with open(file_path, 'r') as file:
#     json_data = file.read()

# # Step 2: Convert the JSON data to a DataFrame
# # df = pd.read_json(json_data)

# # If your JSON data is nested, you might want to use json_normalize
# df = pd.json_normalize(json.loads(json_data))

# print(df)



import pandas as pd
import json

# Path to your text file
# file_path = 'path_to_your_file.txt'

# Step 1: Read the JSON data from the text file
with open(file_path, 'r') as file:
    json_data = file.read()

# Step 2: Convert the JSON string to a Python dictionary
data = json.loads(json_data)

# Step 3: Get the key names
keys = data.keys()  # This will work since 'data' is a dictionary

# Step 4: Print the key names
for key in keys:
    print(key)

# Step 5: Normalize the JSON data into a DataFrame
df = pd.json_normalize(data)

# Step 6: Display the DataFrame (optional)
print(df)
print(pd.DataFrame(df['accounts']))