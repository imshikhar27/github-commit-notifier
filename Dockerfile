FROM python:3.14

WORKDIR /app

COPY calculator.py .

CMD ["python", "calculator.py"]