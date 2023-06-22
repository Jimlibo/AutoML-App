"""
Created: 20 June 2023
Author: Dimitris Lymperopoulos
Description: A streamlit app that creates a model trained on a given dataset and deploys it online
"""

import os
import pandas as pd
import streamlit as st
import pandas_profiling
from Utils.ml_utils import create_model, overview, import_dataset, eda, download_model


def main():
    # add main page properties
    st.set_page_config(page_title="AutoML App", page_icon=":computer:", layout="wide")

    # Initialization
    df = None
    if os.path.exists("Log_Dir/current_dataset.txt"):
        with open("Log_Dir/current_dataset.txt", 'r') as f:
            cur_dataset = f.readline()
        df = pd.read_csv(os.path.join("Datasets", cur_dataset), index_col=None)

    # Create menu sidebar with different options
    with st.sidebar:
        st.image("./Images/ai.png")
        st.title("AutoML App")
        choice = st.radio("Navigation", ["General", "Import Dataset", "Exploratory Data Analysis", "Create Model",
                                         "Download Model", "Deploy Model"
                                         ])
        if st.button("Clear Cache"):
            # delete old datasets and models - TODO
            pass

    # Overview of the app
    if choice == "General":
        overview()

    # Upload file
    if choice == "Import Dataset":
        import_dataset()

    # Get a summary of the dataframe along with statistics about it
    if choice == "Exploratory Data Analysis":
        eda(df)

    # Generate the best model using pycaret
    if choice == "Create Model":
        st.title("Create Model")

        if df is not None:
            chosen_target = st.selectbox('Choose the Target Column', df.columns)
            chosen_task = st.selectbox('Choose ML Task', ['Classification', 'Regression', 'Time Series'])
            model_name = st.text_input("Choose Model Name", "autoML_model")

            if st.button('Run Modelling'):
                _ = create_model(task=chosen_task, train_df=df, target=chosen_target, model_name_=model_name)
        else:
            st.info("No dataset has been chosen! Please go to the 'Import Dataset' tab and choose your dataset.")

    # Download the best model that was previously created
    if choice == "Download Model":
        download_model()

    # Deploy the model - TODO
    if choice == "Deploy Model":
        st.title('Deploy Model')
        st.info("Not yet implemented!")


if __name__ == '__main__':
    main()
