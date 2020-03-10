FROM python:3.6
WORKDIR /app
COPY requirements.txt,run.sh .
EXPOSE 5000
RUN export 'DB_URI'="mysql+pymysql://root:123456@35.246.33.184/linux"
RUN export 'SECRET_KEY'="7218a9143c27c16610765205a1b21cb7"
RUN pip3 install requests
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python","app.py"]
COPY . .