FROM python:3.10.1-slim

COPY requirements.txt .
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt
RUN rm -rf requirements.txt

COPY src /code/src
COPY *.csv /code

WORKDIR /code
CMD ["python3", "/code/src/main.py"]