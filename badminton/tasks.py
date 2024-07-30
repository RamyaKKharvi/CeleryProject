from celery import shared_task
from time import sleep


@shared_task()
def score_difference(team1_score, team2_score):
    sleep(10)
    return abs(team1_score - team2_score)


@shared_task()
def total_score(team1_score, team2_score):
    sleep(10)
    print("This will print in celery port")
    return team1_score + team2_score


@shared_task()
def my_scheduled_task(id):
    print(f'Session Cache: {id}')
    return id
