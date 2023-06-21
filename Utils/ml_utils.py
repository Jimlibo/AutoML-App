"""
Created: 21 June 2023
Author: Dimitris Lymperopoulos
Description: A file containing some functions that help with the ml pipeline process
"""

import os
import streamlit as st
import pandas_profiling
from pycaret import regression, classification


def create_model(task, train_df, target, model_name_):
    best_model_ = None

    if task == 'Classification':
        classification.setup(train_df, target=target, verbose=False)
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

    return best_model_


# Further enhance overview function - TODO
def overview():
    st.title("Welcome to AutoML App!")
    st.write("This app has 6 tabs, including General, Import Dataset, EDA, Create Model,"
             " Download Model, and Deploy Model.")

    # Add descriptions for each tab
    st.header("General")
    st.write("This is the overview page you are currently viewing. It provides an overview of the entire app.")

    st.header("Import Dataset")
    st.write("In this tab, you can import your dataset to be used for analysis and model building.")

    st.header("EDA")
    st.write("This tab allows you to explore your dataset using various visualizations and statistical methods.")

    st.header("Create Model")
    st.write("In this tab, you can build and train a machine learning model on your dataset.")

    st.header("Download Model")
    st.write("This tab allows you to download your trained machine learning model for future use.")

    st.header("Deploy Model")
    st.write("In this tab, you can deploy your trained machine learning model to a cloud service or a local environment"
             " for inference.")

