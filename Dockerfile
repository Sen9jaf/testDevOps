FROM python:3.11-slim

WORKDIR /testDevOps

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["python", "program.py"]

