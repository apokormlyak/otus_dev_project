FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip

COPY ./storaging .

RUN pip install -r requirements.txt


RUN sed -i 's/\r$//g' docker-build/entrypoint.sh && chmod +x docker-build/entrypoint.sh


RUN sed -i 's/\r$//g' docker-build/start && chmod +x docker-build/start

