FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip

COPY ./storaging/requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY . .


COPY ./storaging/docker-build/entrypoint.sh /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

COPY ./storaging/docker-build/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start
