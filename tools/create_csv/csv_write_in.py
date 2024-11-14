import pandas as pd
#import os

# create a dictionary
data = {
    'user_id': ["123", "Penn"],
    'username': ['Donald Trump', 'Penn Li'],
    'password': ["123", "0000"]
}

df = pd.DataFrame(data)
#directory = 'D:\Software Engineer 350 GP\group23_COMPS350F\tools\csv_data'
#file_path = os.path.join(directory, 'default.csv')
df.to_csv('default.csv', index=False)