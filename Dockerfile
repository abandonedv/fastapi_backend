FROM python:3.9

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

#docker build -t fastapi_image .
#docker run -d --name fastapi_container -p 80:80 fastapi_image