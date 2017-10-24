FROM python:3.4-alpine
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD . /code
CMD ["python", "app.py"]
