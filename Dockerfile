# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /UI

# copy the dependencies file to the working directory
COPY . /UI

# install dependencies
RUN pip install -r Requirements.txt

# copy the content of the local src directory to the working directory


# command to run on container start
CMD [ "python", "/UI/app.py" ]
