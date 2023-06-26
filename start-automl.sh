#!/bin/bash

# define color codes for output formatting
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Go to Setup directory
cd Setup

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
