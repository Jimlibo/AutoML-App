"""
Created: 20 June 2023
Author: Dimitris Lymperopoulos
Description: A streamlit app that creates a model trained on a given dataset and deploys it online
"""

import os
import pandas as pd
import streamlit as st
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from Utils.ml_utils import create_model


# Initialization
df = None
model_name = 'AutoML_model'

# Create menu sidebar with different options
with st.sidebar:
    st.image("./Images/ai.png")
    st.title("AutoML App")
    choice = st.radio("Navigation", ["General", "Import Dataset", "Exploratory Data Analysis", "Create Model",
                                     "Download Model", "Test Model", "Deploy Model"
                                     ])
    st.info("This application helps you explore your data, build a machine learning model and deploy it online")

# Overview of the app - TODO
if choice == "General":
    st.title('Welcome to AutoML App')
    st.info("Not yet implemented!")

# Upload file
if choice == "Import Dataset":
    st.title("Import Dataset")
    dataset_source = st.radio("Dataset Source:", ["Upload your dataset", "Choose from existing datasets"])

    if dataset_source == "Upload your dataset":
        file = st.file_uploader("Upload Your Dataset")
        dataset_name = st.text_input("Dataset Name", file.name if file else "")

        if file:
            df = pd.read_csv(file, index_col=None)
            df.to_csv(os.path.join("Datasets", dataset_name), index=None)
            st.dataframe(df)

    else:
        dataset = st.selectbox("Dataset", os.listdir("Datasets"))
        df = pd.read_csv(dataset, index_col=None)
        st.dataframe(df)


# Get a summary of the dataframe along with statistics about it
if choice == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")

    if df is not None:
        profile_df = df.profile_report()
        st_profile_report(profile_df)
    else:
        st.info("No dataset has been chosen! Please go to the 'Import Dataset' tab and  your choose a dataset.")


# Generate the best model using pycaret
if choice == "Create Model":
    st.title("Create Model")

    if df is not None:
        chosen_target = st.selectbox('Choose the Target Column', df.columns)
        chosen_task = st.selectbox('Choose ML Task', ['Classification', 'Regression'])
        model_name = st.text_input("Choose Model Name", "autoML_model")

        if st.button('Run Modelling'):
            best_model = create_model(task=chosen_task, train_df=df, target=chosen_target, model_name_=model_name)
    else:
        st.info("No dataset has been chosen! Please go to the 'Import Dataset' tab and choose your dataset.")


# Download the best model that was previously created
if choice == "Download Model":
    st.title("Download Model")
    # get list of existing models
    models = os.listdir("Models")

    # check that the above list is not empty (at least one model exists)
    if len(models) > 0:
        download_name = st.selectbox("Model to download:", models)
        with open("Models/" + download_name, "rb") as f:
            st.download_button("Download Model", f, file_name=download_name)

    else:
        st.info("No model has been yet created! Please go to the 'Create Model' tab and generate a model first.")


# Deploy the model - TODO
if choice == "Deploy Model":
    st.title('Deploy Model')
    st.info("Not yet implemented!")
