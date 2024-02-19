import requests
from celery import Celery
from celery.schedules import crontab
from ..settings.celery import app


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

@app.task
def get_the_quote_of_the_day():
    url = 'https://favqs.com/api/qotd'
    session = requests.Session()
    quote_of_the_day = session.get(url=url).json()['quote']
    return quote_of_the_day['author'], quote_of_the_day['body']


if __name__=='__main__':
    print(get_the_quote_of_the_day())