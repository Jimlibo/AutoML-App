"""
Created: 21 June 2023
Author: Dimitris Lymperopoulos
Description: A file containing some functions that help with the ml pipeline process
"""

import os
import streamlit as st
import pandas_profiling
from pycaret import regression, classification, clustering, anomaly, time_series


# add implementation for clustering, anomaly detection and time series - TODO
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
        regression.setup(train_df, target=target, verbose=False)
        st.dataframe(regression.pull())
        best_model_ = regression.compare_models()
        st.dataframe(regression.pull())
        regression.save_model(best_model_, os.path.join("Models", model_name_))

    if task == 'Clustering':
        pass

    if task == "Anomaly Detection":
        pass

    if task == "Time Series":
        pass

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
    'label'. Then, define the ML task (classification or regression) that the model needs to solve. Classification 
    means that the model should be able to categorize given data into distinct classes, while a Regression model
    tries to predict a real value from a continuous range of values. Finally, you also have the option to change the
    default name of the model ('autoML_model'). By pressing 'Run Modeling' the app will try to find the best model that
    corresponds to the specified task. After the training phase is over, you will be presented with a table containing
    the candidate models, as well as their related metrics.
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
