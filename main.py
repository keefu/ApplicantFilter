import streamlit as st
import module

def main():
    # Streamlit Title
    st.title("Data Filtering")

    # Load data using Streamlit's file uploader
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "json"])  # Change type as needed

    if uploaded_file is not None:
        # Load data from the uploaded file
        data = module.load_data(uploaded_file)
        st.write("Data Loaded Successfully!")
        
        # Display the data on the app
        st.dataframe(data)  

        # Create a DataFilter instance
        filter = module.DataFilter(data) 

        # Get the result of whether there are accounts older than 90 days
        accounts_older_than_90_days = filter.account_older_than_90_days()

        # Display the result in the Streamlit app
        st.write(f"Are there accounts older than 90 days? {accounts_older_than_90_days}")

        # Display the result in the Streamlit app
        st.write(filter.balance_equal_to_credit_debit())

if __name__ == "__main__":
    main()