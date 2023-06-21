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
