"""
В этом задании вам нужно оживить шаблон.

У вас уже есть готовая вьюха, которая пробрасывает нужный контекст и свёрстанная страница.
Проблема в том, что в шаблоне статичные данные, а нужно сделать так, чтобы шаблон использовал
данные из контекста и не содержал в себе "тестовых" данных. Этот процесс и называется оживлением.
"""

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from django_templates_homework.custom_types import Message


def get_message(
    text: str = "почувствуй себя ёжиком",
    author_nickname: str = "bg yellow plum",
    likes_num: int = 3,
    reposts_num: int = 12,
) -> Message:
    return Message(
        text=text,
        author_nickname=author_nickname,
        likes_num=likes_num,
        reposts_num=reposts_num,
    )


def message_details_view(request: HttpRequest) -> HttpResponse:
    title = "Сообщение"
    message = get_message()
    return TemplateResponse(
        request,
        "level_2/message_detail.html",
        context={
            title: title,
            "message": message,
        },
    )
