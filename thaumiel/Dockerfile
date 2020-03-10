FROM python:3.6
WORKDIR /app
COPY requirements.txt .
EXPOSE 5000
RUN pip3 install requests
RUN pip install -r requirements.txt
RUN run.sh
ENTRYPOINT ["/usr/local/bin/python","app.py"]
COPY . .