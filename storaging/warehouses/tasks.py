import requests
from ..settings.celery import app
import logging

logger = logging.getLogger(__name__)


@app.task(bind=True, max_retries=3, soft_time_limit=86400, time_limit=90000)
def get_the_quote_of_the_day(self):
    logger.info('HELLO!!!!!!!!')
    url = 'https://favqs.com/api/qotd'
    session = requests.Session()
    quote_of_the_day = session.get(url=url).json()['quote']
    return quote_of_the_day['author'], quote_of_the_day['body']
