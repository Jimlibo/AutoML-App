#!/bin/bash


# function to check if a specific service exists in the os
service_exists() {
    local n=$1
    if [[ $(systemctl list-units --all -t service --full --no-legend "$n.service" | sed 's/^\s*//g' | cut -f1 -d' ') == $n.service ]]; then
        return 0
    else
        return 1
    fi
}


# define color codes for output formatting
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Go to Setup directory
cd Setup

# check if docker exists and if yes, use it to setup and start the app
if service_exists docker; then

    # Check if docker container exists - if not create it
    if [ ! "$(docker ps -a | grep automl)" ]; then
        # create docker image named automl
        echo -e "${GREEN}Creating automl image...${NC}";
        docker build -t automl:latest .

        # create docker container named automl
        echo -e "${GREEN}Creating and starting automl container...${NC}";
        docker run  --name automl -p 8501:8501 automl:latest;

    else
        # else, simply start the container
        echo -e "${GREEN}Starting automl container...${NC}";
        docker start automl;
    fi

else
    # if docker does not exist, use python and streamlit to run the app
    pip install -r requirements.txt   # download necessary packages directly into python
    cd ../ 
    streamlit run app.py   # run the app

fi