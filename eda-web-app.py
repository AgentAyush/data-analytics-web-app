import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import io

def set_header_as_first_row(data):

    if not data.columns.size:
        data.columns = data.iloc[0]
        data = data[1:]
    return data

#Tite and subheader
st.title('Exploratory Data Analysis')
st.subheader('Data Information')

#Upload File
upload = st.file_uploader('Choose a CSV file', type='csv')
if upload is not None:
    data = pd.read_csv(upload)
    data = set_header_as_first_row(data)

#Show Dataset
    if st.checkbox('Show Dataset'):

        #Total number of rows in the datasetis stored in n
        n = data.shape[0]
        #showing the number of rows
        st.write('Number of Rows:', n)

        #Giving users option to get required number of rows
        number = st.number_input('Number of Rows to View', 1, n)
        st.dataframe(data.head(number))

    #Show datatype of each column
    if st.checkbox('Show Datatype'):
        st.text('Data Type')
        st.write(data.dtypes)
    #Show the number of rows and columns using radio button
    if st.checkbox('Show Shape'):
        data_shape = st.radio('Shape of Dataset', ('Rows', 'Columns'))
        if data_shape == 'Rows':
            st.write('Number of Rows:', data.shape[0])
        if data_shape == 'Columns':
            st.write('Number of Columns:', data.shape[1])
    #Show NULL values
    if st.checkbox('Show NULL Values'):
        st.write(data.isnull().sum())
        test = data.isnull().values.any()
        if test:
            st.warning('There are NULL values in the dataset')
            #Plotting the NULL values
            if st.checkbox('Plot NULL values'):
                fig, ax = plt.subplots()
                sns.heatmap(data.isnull(), cbar=False, ax=ax)
                st.pyplot(fig)


            # Dropping NULL values
            if st.checkbox('Drop NULL values'):
                if st.checkbox('Drop inplace'):
                    data.dropna(inplace=True)
                    st.success('NULL values dropped inplace.')
                if st.checkbox("Create a new dataframe"):
                    new_data = data.dropna()
                    st.write('A new DataFrame without NULL values has been created.')
                    st.write(new_data)
        else:
            st.write('There are no NULL values in the dataset.')

        
    #Show Value Counts
    if st.checkbox('Show Value Counts'):
        column = st.selectbox('Select Column', data.columns)
        st.write(data[column].value_counts())
    #Show Summary
    if st.checkbox('Show Summary'):
        st.write(data.describe().T)
        
    #Finding duplicate values 
    if st.checkbox('Show Duplicate Values'):
        test1 = data.duplicated().any()
        if test1 == True:
            st.warning('There are duplicate values in the dataset')
            #Showing the duplicate values
            st.write(data[data.duplicated()])
            dup = st.selectbox("Do you want to drop duplicate values", ('Yes', 'No'))
            if dup == 'Yes':
                data.drop_duplicates()
                st.write('Duplicate values are dropped')
            else:
                st.write('Duplicate values are not dropped')
        else:
            st.success('There are no duplicate values in the dataset')
    #Plotting bar chart between two coloums
    if st.checkbox('Bar Chart'):
        column = st.selectbox('Select Column', data.columns)
        st.write('Bar Chart')
        st.bar_chart(data[column].value_counts())
    #Correlation
    if st.checkbox('Show Correlation'):
        numeric_columns = data.select_dtypes(include=[np.number]).columns
        corr_matrix = data[numeric_columns].corr()
        st.write(corr_matrix)

        if st.checkbox('Plot Correlation'):
            fig, ax = plt.subplots()
            sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, ax=ax)
            st.pyplot(fig)
    

    #Downloading the processed dataset
# Check if the user clicked the "Download Processed Data" button
    if st.button('Download Processed Data'):
        # Convert the DataFrame to a CSV file
        csv = data.to_csv(index=False)
        # Create a link for the user to click and download the file
        st.download_button(
            label='Download CSV',
            data=csv,
            file_name='processed_data.csv',
            mime='text/csv'
        )

if st.button("About Application"):
    st.text('This is a simple EDA application which is used to perform EDA on a dataset. ')
    st.text('It is developed by Ayush Das, Sayan Banerjee, Sreejata Banerjee,')
    st.text('Lucky Das and Mrinalini Bhattacharjee')
    st.text('This projected in intended to make the data preprocessing easy for users.')
