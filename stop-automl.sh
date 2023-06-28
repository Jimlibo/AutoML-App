!/bin/bash

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

# stop app by shutting down the container
echo -e "${GREEN}Shutting down AutoML...${NC}"
docker stop automl

if "$REMOVE_CONTAINERS"; then
    echo -e "${GREEN}Removing docker container and images...${NC}"

    docker rm automl      # remove kafka container
    docker rm automl:latest # remove automl image
    docker volume prune -f   # remove unused volumes
fi