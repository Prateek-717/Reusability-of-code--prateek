#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import json


# In[64]:


with open("globalmart_data.json","r") as json_data:
    data=json.load(json_data)


# In[65]:


data


# In[66]:


type(data)


# In[67]:


df=pd.DataFrame(data)
df


# In[69]:


# Assuming you have a DataFrame named df
product_names = []
product_sizes = []

for index, row in df.iterrows():
    # Access the "product" dictionary within the row
    product_data = row["product"]
    
    # Fetch the "product_name" and "sizes" from the "product" dictionary
    product_name = product_data["product_name"]
    sizes = product_data.get("sizes", "N/A")  # Use .get() to handle missing sizes
    
    # Append the values to the respective lists
    product_names.append(product_name)
    product_sizes.append(sizes)

# Add the product_names and product_sizes lists as new columns in the DataFrame
df["product_names"] = product_names
df["product_sizes"] = product_sizes


# In[70]:


df


# In[71]:


data = {'product_name': [
    'Redi-Strip #10 Envelopes, 4 1/8 x 9 1/2',
    'Cisco SPA 501G IP Phone',
    'Bretford CR4500 Series Slim Rectangular Table',
    "Eldon Fold 'N Roll Cart System"],
    'product_sizes': [
        '4 1/8 x 9 1/2',
        '5 x 3 x 8',
        '8 x 10, 7 x 9, 6 x 8',
        '12 x 16']
}

df = pd.DataFrame(data)

def get_max_range_product(df, product_names):
    max_range_product = None
    max_range = 0

    for product_name in product_names:
        sizes = df[df['product_name'] == product_name]['product_sizes'].values[0].split(', ')
        size_range = len(sizes)
        if size_range > max_range:
            max_range = size_range
            max_range_product = product_name

    return max_range_product

# List of product names
product_names = [
    'Redi-Strip #10 Envelopes, 4 1/8 x 9 1/2',
    'Cisco SPA 501G IP Phone',
    'Bretford CR4500 Series Slim Rectangular Table',
    "Eldon Fold 'N Roll Cart System"
]

# Get the product with the maximum size range
max_range_product = get_max_range_product(df, product_names)

print(f"The product with the maximum size range is: {max_range_product}")


# In[79]:


# Specify the product name you're looking for
product_name = "Mitel 5320 IP Phone VoIP phone"

# Filter the DataFrame to include only the rows with the specified product name
filtered_df = df[df['product_name'] == product_name]

if not filtered_df.empty:
    # Extract the "product_sizes" information for the product
    sizes = filtered_df['product_sizes'].values[0]

    # Count the number of sizes available (assuming sizes are separated by commas)
    num_sizes = len(sizes.split(','))

    # Print the result
    print(f"The product '{product_name}' has {num_sizes} available sizes.")
else:
    print(f"No product found with the name '{product_name}'.")


# In[ ]:




