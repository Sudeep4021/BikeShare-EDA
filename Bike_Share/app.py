import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import os



def main():
    st.title("Bike Share Data Explorer")
    filename = file_selector()
    st.info("You Selected {}".format(filename))

    #Read Data
    df = pd.read_csv(filename)

    #Show Dataset
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of rows to View", 5, 100)
        st.dataframe(df.head(number))

    #Show Columns
    if st.button("Columns Names"):
        st.write(df.columns)

    #Show Shape
    if st.checkbox("Shape of Dataset"):
        data_dim = st.radio("Show Dimension By ", ("Rows", "Columns"))
        if data_dim == "Columns":
            st.text("Number of Columns")
            st.write(df.shape[1])
        elif data_dim == "Rows":
            st.text("Number of Rows")
            st.write(df.shape[0])
        else:
            st.write(df.shape)

    #Select Columns
    if st.checkbox("Select Columns To show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    #Show dtype
    if st.button("Data Types"):
        st.write(df.dtypes)

    #Show Summary
    if st.checkbox("Summary"):
        st.write(df.describe().T)

    #Plot Visualization
    # seaborn plot
    #Corr
    if st.checkbox("Correlation with Seaborn"):
        st.write(sns.heatmap(df.corr(), annot=True))
        st.pyplot()

    # Pie Chart
    if st.checkbox("PieChart"):
        all_columns = df.columns.tolist()
        columns_plot = st.selectbox("Select 1 Column ", all_columns)
        pie_plot = df[columns_plot].value_counts().plot.pie(autopct = "%1.1f%%")
        st.write(pie_plot)
        st.pyplot()

    #Customizable
    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select Type of plot", ["area", "bar", "line", "hist", "box", "kde"])
    selected_columns_names = st.multiselect("Select Columns To Plot ", all_columns_names)

    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        if type_of_plot == "area":
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        if type_of_plot == "bar":
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        if type_of_plot == "line":
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind = type_of_plot)
            st.write(cust_plot)
            st.pyplot()



def file_selector(folder_path = './dataset'):
    filenames = os.listdir(folder_path)
    selected_filenames = st.selectbox("Select a file", filenames)
    return os.path.join(folder_path, selected_filenames)


if __name__ == '__main__':
    main()