FROM python:3.10
WORKDIR /app
COPY . /app
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x run.sh
