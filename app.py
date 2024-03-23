import streamlit as st
import pandas as pd
import seaborn as sns 

#Tite and subheader
st.title('Exploratory Data Analysis')
st.subheader('Data Information')

#Upload File
upload = st.file_uploader('Choose a CSV file', type='csv')
if upload is not None:
    data = pd.read_csv(upload)

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
        test = data.isnull().values().any()
        if test:
            st.write('There are NULL values in the dataset')
            if st.checkbox('Show NULL values'):
                sns.heatmap(data.isnull())
                st.pyplot()

        else:
            st.write('There are no NULL values in the dataset')

        
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

    #Correlation
    if st.checkbox('Show Correlation'):
        st.write(data.corr())
        sns.heatmap(data.corr())
        st.pyplot()
    
    #Plotting
    if st.checkbox('Plotting'):
        column = st.selectbox('Select Column', data.columns)
        sns.countplot(data[column])
        st.pyplot()
if st.button("About Application"):
    st.text('This is a simple EDA application which is used to perform EDA on the dataset. ')
    st.text('It is developed by Ayush Das as a part of TTL Mini Project')
    st.text('Email: 2105113@kiit.ac.in')
    st.text('Roll Number: 2105113')
