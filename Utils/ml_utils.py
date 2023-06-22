"""
Created: 21 June 2023
Author: Dimitris Lymperopoulos
Description: A file containing some functions that help with the ml pipeline process
"""

import os
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pycaret import regression, classification, time_series


# add implementation for clustering and anomaly detection ? - TODO
def create_model(task, train_df, target, model_name_):
    best_model_ = None

    if task == 'Classification':
        classification.setup(train_df, target=target, verbose=False, normalize=True, fix_imbalance=True)
        setup_df = classification.pull()
        st.dataframe(setup_df)
        best_model_ = classification.compare_models()
        compare_df = classification.pull()
        st.dataframe(compare_df)
        classification.save_model(best_model_, os.path.join("Models", model_name_))

    if task == 'Regression':
        regression.setup(train_df, target=target, verbose=False, normalize=True)
        st.dataframe(regression.pull())
        best_model_ = regression.compare_models()
        st.dataframe(regression.pull())
        regression.save_model(best_model_, os.path.join("Models", model_name_))

    if task == "Time Series":
        time_series.setup(train_df, target=target, verbose=False)
        st.dataframe(time_series.pull())
        best_model_ = time_series.compare_models()
        st.dataframe(time_series.pull())
        time_series.save_model(best_model_, os.path.join("Models", model_name_))

    return best_model_


def overview():
    st.title("Welcome to AutoML App!")
    st.write("""
    The purpose of this app is to speed up the development of machine learning models, while also remaining 
    easy-to-comprehend for the average user. The app consists  of 6 tabs, each one of which is
    designed to implement a specific step of the machine learning pipeline.
    """)

    # Add descriptions for each tab
    st.header("General Tab")
    st.write("""
    This is the home page that you are currently viewing. It provides an overview of the entire app,
    along with information about the other tabs.
    """)

    st.header("Import Dataset Tab")
    st.write("""
    In this tab, you can import your dataset to be used for analysis and model building. You can choose to either 
    upload your own, or use one of the existing datasets. As soon as you define the dataset to be used, you will 
    also be able to see a summary of the dataset, to make sure that everything is as it should be.
    """)
    st.image("./Images/import_dataset_preview.png")

    st.header("Exploratory Data Analysis Tab")
    st.write("""
    This tab allows you to explore your dataset using various visualizations and statistical methods. Here you can 
    gain valuable insights about your data such as missing values, variance and other statistics about every column
    in the dataset.
    """)
    st.image("./Images/eda_preview.png")

    st.header("Create Model Tab")
    st.write("""
    Here, you can build and train a machine learning model on your dataset. First, by utilizing the given filters,
    you can specify the column of the dataset that will be be used as the target for predictions, also known as 
    'label'. Then, define the ML task (classification, regression or time series) that the model needs to solve. 
    Classification means that the model should be able to categorize given data into distinct classes, while a 
    Regression model tries to predict a real value from a continuous range of values.The final option, Time series, 
    refers to the prediction of a specific value in a certain point in time and is commonly used for stock prices and
    financial data in general. Finally, you also have the option to change the default name of the model 
    ('autoML_model'). By pressing 'Run Modeling' the app will try to find the best model that corresponds to the 
    specified task. After the training phase is over, you will be presented with a table containing the candidate 
    models, as well as their related metrics.
    """)
    st.image("./Images/create_model_preview.png")

    st.header("Download Model Tab")
    st.write("""
    By navigating to this tab,you are able to download a trained machine learning model for future use. Apart from 
    the model you trained in the 'Create Model' tab, you can also opt to download one of the models that were previously
    trained and stored.
    """)
    st.image("./Images/download_model_preview.png")

    # add deployment tab info - TODO
    st.header("Deploy Model Tab")
    st.write("""
    In this tab, you can deploy your trained machine learning model to a cloud service or a local environment
    for inference. This functionality is not yet implemented!
    """)


def import_dataset():
    st.title("Import Dataset")
    dataset_source = st.radio("Dataset Source:", ["Upload your dataset", "Choose from existing datasets"])
    temp_df = None

    if dataset_source == "Upload your dataset":
        file = st.file_uploader("Upload Your Dataset")
        dataset_name = st.text_input("Dataset Name", file.name if file else "")

        if file:
            temp_df = pd.read_csv(file, index_col=None)
            temp_df.to_csv(os.path.join("../Datasets", dataset_name), index=None)
            st.dataframe(temp_df)

    else:
        dataset_name = st.selectbox("Dataset", os.listdir("../Datasets"))
        temp_df = pd.read_csv(os.path.join("../Datasets", dataset_name), index_col=None)
        st.dataframe(temp_df)

    if st.button("Confirm Dataset") and temp_df is not None:
        # write the name of the current dataset to a file, so that other tabs can get it from there
        with open("../Log_Dir/current_dataset.txt", 'w') as f:
            f.write(dataset_name)
        st.info("Dataset confirmed!")


def eda(df):
    st.title("Exploratory Data Analysis")

    if df is not None:
        profile_df = df.profile_report()
        st_profile_report(profile_df)
    else:
        st.info("No dataset has been chosen! Please go to the 'Import Dataset' tab and  your choose a dataset.")
