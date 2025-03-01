
import pandas as pd
import json
from datetime import timedelta

def load_data(uploaded_file):
    # Step 1: Read the contents of the uploaded file
    json_data = uploaded_file.read().decode('utf-8')  # Decode bytes to string

    # Step 2: Convert the JSON string to a dictionary
    data = json.loads(json_data)

    # Step 3: Normalize the data into a DataFrame
    df = pd.json_normalize(data)

    # Assuming 'accounts' is a key in your JSON data
    df_account = pd.DataFrame(df['accounts'][0])

    # Assuming 'transactions' is a nested key within 'accounts'
    df_records = pd.DataFrame(df_account['transactions'][0])

    # Step 4: Convert `date` to datetime type
    df_records['date'] = pd.to_datetime(df_records['date'])  # Convert date to datetime

    # Step 5: Handle empty strings and convert to integer
    df_records['credit'] = pd.to_numeric(df_records['credit'].replace('', '0'), errors='coerce').fillna(0).astype(int)
    df_records['debit'] = pd.to_numeric(df_records['debit'].replace('', '0'), errors='coerce').fillna(0).astype(int)
    df_records['balance'] = pd.to_numeric(df_records['balance'].replace('', '0'), errors='coerce').fillna(0).astype(int)


    return df_records

class DataFilter:
    def __init__(self, data):
        self.data = data
    
    def account_older_than_90_days(self):
        account_oldest_date = self.data['date'].min()
        account_newest_date = self.data['date'].max()
        account_age_days = (account_newest_date - account_oldest_date).days
        account_older_than_90_days = account_age_days > 90
        return account_older_than_90_days
    
    def balance_equal_to_credit_debit(self): 
        oldest_date = self.data['date'].min()
        oldest_date_record = self.data[self.data['date'] == oldest_date]
        for index, record in oldest_date_record.iterrows():
            if (record['credit'] > 1 and record['credit'] == record['balance'] or record['debit'] > 1 and record['debit'] == record['balance']):
                return(f"Record on {oldest_date} meets the condition: {record.to_dict()}")

if __name__ == "__main__":
    data = load_data()

    filter = DataFilter()

    account_90_days = filter.account_older_than_90_days()
    print(account_90_days)

    balance_credit_debit = filter.balance_equal_to_credit_debit()
    print(balance_credit_debit)