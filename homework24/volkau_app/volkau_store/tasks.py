from datetime import datetime, timedelta
from .models import Log, Games
from celery import shared_task
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from typing import List

import logging

logger = logging.getLogger('store')



@shared_task()
def log_store(path, username, time):
    time = datetime.now()
    message_log = f'{time} | {username} | {path}'
    logger.info(message_log)
    log = Log(path=message_log, time=time)
    log.save()


@shared_task()
def send_news_email_task(games_of_last_week, three_top_games, user:dict):
    message_text = f'Hello, {user["username"]}! See all our offers from last week!\n'
    for game in games_of_last_week:
        msg_chunk = f"""New games:\n {game['name']}, Release date: {game['release_date']}, Price: {game['price']}
        More details: {reverse('store:game_slug', args=[game['slug']])}
        """
        message_text += msg_chunk
    for game in three_top_games:
        msg_chunk = f"""Top rating:\n {game['name']}, Release date: {game['release_date']}, Price: {game['price']}
        More details:  {reverse('store:game_slug', args=[game['slug']])}
        """
        message_text += msg_chunk    
        send_mail("Weekly news", message_text, "support@example.com",[user['email']], fail_silently=False,)


@shared_task()
def weekly_newsletter():
    all_users = list(User.objects.filter(is_staff=False).values())
    all_games_of_last_week = list(Games.objects.filter(public_date__gte=datetime.today() - timedelta(days=7)).values())
    all_three_top_games = list(Games.objects.order_by('comments__average_rating')[:3].values())
    for user in all_users:
        send_news_email_task.delay(all_games_of_last_week, all_three_top_games, user)

