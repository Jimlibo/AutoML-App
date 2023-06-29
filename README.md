# AutoML-App

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.23-orange.svg)
![Pycaret](https://img.shields.io/badge/pycaret-v2.3.3-green.svg)

## General
An app that utilizes streamlit and pycaret to automate a machine learning pipeline. The web app
contains several tabs, for data upload, data preprocessing, model training, model evaluation, and
model deployment.

## Setup
In order to get the app running, first you need to clone this repository.
This can be done with the command:
```bash
git clone https://github.com/Jimlibo/AutoML-App.git
```

### Setup with Docker <img src="https://github.com/walkxcode/dashboard-icons/blob/main/png/docker-moby.png?raw=true" width="30" height="30" />
If you have docker installed, you can run the app with the following commands:
```sh
cd AutoML-App
./start-automl.sh
```
The above script will build the docker image, initialize the container and run the app.

### Setup with Python <img src="https://github.com/walkxcode/dashboard-icons/blob/main/png/python.png?raw=true" width="30" height="30" />
If you don't have docker installed,then you can install the required python
packages with the following command:
```sh
cd AutoML-App
pip install -r Setup/requirements.txt
```
Then you can run the app with the following command:
```sh
streamlit run app.py
```

## Usage
Once the app is running, you can go to http://localhost:8501/ to access it.
You will be presented with the <b>General</b> tab, which contains a brief overview of the different
functionalities and actions that are available. From the <b>Import Dataset</b> tab, you can upload a
dataset in csv format. The datasets you upload will be saved inside the [Datasets] folder. In the 
<b>Exploratory Data Analysis</b> tab, you can get a summary of the dataset you uploaded, as well as some 
useful statistics. In the <b>Create Model</b> tab, you have the option to train a model on the specified dataset,
and you can also download it from the <b>Download Model</b> tab. All the models you create will be saved inside
the [Models] folder. In case you want to remove older datasets and models, you can click the 'Clear Datasets and Models'
button.\
<b>Note:</b> The 'Clear Datasets and Models' button will remove all the datasets and models that are saved in the folders
mentioned above!

[Datasets]: https://github.com/Jimlibo/AutoML-App/tree/main/Datasets
[Models]: https://github.com/Jimlibo/AutoML-App/tree/main/Models

## License
Distributed under the MIT License. See 
[LICENSE](https://github.com/Jimlibo/AutoML-App/tree/main/License_Aggreement/LICENSE) for more information.



