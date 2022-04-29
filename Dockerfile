FROM python

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "main.py"]

