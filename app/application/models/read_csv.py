import pandas as pd

class reader:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.data = None

        # read CSV file
        def read_csv(self):
            try:
                self.data = pd.read_csv(self.file_path)
                print("CSV file loaded successfully.")
            except FileNotFoundError:
                print("File not found. Please check the file path.")
            except Exception as e:
                print(f"An error occurred: {e}")

        #Displays the first few rows of the DataFrame.
        def preview_data(self, rows=5):
            if self.data is not None:
                print("Preview of the CSV data:")
                print(self.data.head(rows))
            else:
                print("Data not loaded. Please read the CSV file first.")

        #Filters rows based on a specific condition.
        def filter_data(self, column, value):
            if self.data is not None:
                filtered_data = self.data[self.data[column] > value]
                if not filtered_data.empty:
                    print(f"\nFiltered data (where {column} > {value}):")
                    print(filtered_data[['roomNo', 'class', 'price']])
                else:
                    print("\nNo data found matching the criteria.")
            else:
                print("Data not loaded. Please read the CSV file first.")

file_path = r"D:\Software Engineer 350 GP\group23_COMPS350F\default.csv"# Replace with your actual CSV file path
reader = reader(file_path)
reader.read_csv()
reader.preview_data()
reader.filter_data('price', 100)