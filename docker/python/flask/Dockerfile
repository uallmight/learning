FROM python:3.8

# set working directory for where docker should look for files
WORKDIR /

# add source files to target container for compilation
ADD app.py /
ADD requirements.txt /
# run any requirements and install scripts

# install development and compile dependencies
RUN apt-get update -y

# install project dependencies
RUN pip install -r requirements.txt

# ensure we can reach the container by the port we want

# tell our container to run our application
CMD ["python", "app.py"]