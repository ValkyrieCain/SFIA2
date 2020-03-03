FROM python:3.6
WORKDIR /app
COPY requirements.txt .
EXPOSE 5000
RUN python3 -m venv venv
RUN source ./venv/bin/activate
RUN pip3 install requests
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python","app.py"]
COPY . .