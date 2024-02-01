from django.shortcuts import render
from django.http import HttpResponse
import logging

# создаем логгер
logger = logging.getLogger(__name__)

# определяем представление для главной страницы
def index(request):
    # создаем переменную html с вёрсткой и данными
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Вы можете узнать больше обо мне на странице <a href="/about/">О себе</a>.</p>
    """
    # сохраняем в логи данные о посещении страницы
    logger.info(f"Пользователь {request.user} посетил главную страницу")
    # возвращаем ответ с html
    return HttpResponse(html)

# определяем представление для страницы о себе
def about(request):
    # создаем переменную html с вёрсткой и данными
    html = """
    <h1>О себе</h1>
    <p>Меня зовут Влад, и я увлекаюсь программированием.</p>
    <p>Я учусь в GeekBrains по специальности Python-разработчик.</p>
    <p>Мои хобби - играть в шахматы, читать научную фантастику и слушать рок-музыку.</p>
    """
    # сохраняем в логи данные о посещении страницы
    logger.info(f"Пользователь {request.user} посетил страницу о себе")
    # возвращаем ответ с html
    return HttpResponse(html)