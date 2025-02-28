
import pandas as pd
from datetime import timedelta

# Load the excel file
def load_data(file_path):
    # data = pd.read_excel(file_path)
    data = pd.read_json(file_path)
    data['Date'] = pd.to_datetime(data['Date']).dt.date
    return data

class DataFilter:
    def __init__(self, data):
        self.data = data
    
    def account_older_than_90_days(self):
        account_oldest_date = self.data['Date'].min()
        account_newest_date = self.data['Date'].max()
        account_age_days = (account_newest_date - account_oldest_date).days
        account_older_than_90_days = account_age_days > 90
        return account_older_than_90_days
    
    def balance_equal_to_credit_debit(self): 
        oldest_date = self.data['Date'].min()
        oldest_date_record = self.data[self.data['Date'] == oldest_date]
        for index, record in oldest_date_record.iterrows():
            if record['credit'] == record['balance'] or record['debit'] == record['balance']:
                return(f"Record on {oldest_date} meets the condition: {record.to_dict()}")

if __name__ == "__main__":
    data = load_data()

    filter = DataFilter()

    account_90_days = filter.account_older_than_90_days()
    print(account_90_days)

    balance_credit_debit = filter.balance_equal_to_credit_debit()
    print(balance_credit_debit)