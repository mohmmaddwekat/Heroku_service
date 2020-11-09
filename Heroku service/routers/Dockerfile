FROM python:3.8.0-buster

# set a directory for the app
WORKDIR /app

COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
# define the port number the container should expose
COPY /app .
COPY model.sav .
EXPOSE 5000/tcp
EXPOSE 5000/udp
# run the command
ENTRYPOINT [ "python" ]

CMD [ "app.py","-path","./model.sav"]
