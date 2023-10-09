import pandas as pd
def read_csv_and_assign_tO_variable(csv_file_path):
    try:
        #Reading csv file into dataframe
        df = pd.read_csv(csv_file_path)

        # Data frame can be used for future processing
        #e.g, printing the first 5 rows in csv file
        print(df.head())
        
    # Return Dataframe if needed
        return df
    except FileNotFoundError: 
        print(f"Error: The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occured: {str(e)}")

# calling the function with the csv file path
csv_file_path = r"C:\Users\user\OneDrive\Documents\melb_data.csv"
data_frame_variable = read_csv_and_assign_tO_variable(csv_file_path)




if __name__ == "__main__":
    read_csv_and_assign_tO_variable(csv_file_path)