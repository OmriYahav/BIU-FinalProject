FROM python:3.9-alpine3.18
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5005
CMD [ "python3" "PingPongApp.py" ]
