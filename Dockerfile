FROM python:3.10.5-slim-buster

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# Bundle app source
COPY . .
EXPOSE 5005
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=5005" ]