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


# code for optional bash parameter --remove-container
REMOVE_CONTAINERS=false
while [ "$1" ]; do
        case $1 in
            --remove-containers) REMOVE_CONTAINERS=true ;;
            *) echo 'Error in command line parsing' >&2
               exit 1
        esac
        shift
    done

# color codes for better output formatting
GREEN='\033[0;32m'  # green color
NC='\033[0m' # No Color

# check if docker exists, and if yes, use it to stop the app
if service_exists docker; then
    # stop app by shutting down the container
    echo -e "${GREEN}Shutting down AutoML...${NC}"
    docker stop automl

    if "$REMOVE_CONTAINERS"; then
        echo -e "${GREEN}Removing docker container and images...${NC}"

        docker rm automl      # remove kafka container
        docker image rm automl:latest # remove automl image
        docker volume prune -f   # remove unused volumes
    fi

else
    # if docker does not exist, kill the streamlit process
    echo -e "${GREEN}Shutting down AutoML...${NC}"
    kill `pgrep streamlit`
    
fi

echo -e "${GREEN}AutoML app was successfully shutted down!${NC}"