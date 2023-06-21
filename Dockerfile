FROM python:3.9-slim

# define starting directory
WORKDIR /AutoML-App 

# download git, to clone the repository
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# clone the repo
RUN git clone https://github.com/Jimlibo/AutoML-App.git .

# download necessary python packages
RUN pip3 install -r requirements.txt

# inform docker that container listens on port 8501 (default streamlit port)
EXPOSE 8501

# perform healthchecks to make sure the container is still running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# execute the streamlit app
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]