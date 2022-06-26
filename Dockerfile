FROM python:3.7.7-slim

COPY * /opt/
COPY requirements.txt /opt/
RUN pip install --upgrade pip \
  && apt-get clean \
  && apt-get update \
  && apt install -y build-essential \
  && apt install -y elasticsearch \
  && pip install --upgrade -r /opt/requirements.txt

USER 1001

EXPOSE 8080
WORKDIR /opt/

CMD ["python", "app.py", "8080"]
