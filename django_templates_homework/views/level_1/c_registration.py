"""
У нас есть страница с регистрацией, но нет ни названия у вкладки, ни загаловка у страницы. Кажется, мы что-то упустили.

Задания:
    1. Откройте страницу http://127.0.0.1:8000/registration/ и убедитесь, что нет ни заголовка, ни названия у вкладки в брузере.
    2. Найдите в проекте темплэйт registration.html и найдите переменные, которые там используются.
    3. Начните передавать из вьюхи registration_view эту переменную в темплэйт в контексте функции render.
    4. Откройте страницу http://127.0.0.1:8000/registration/ и убедитесь, что и заголовок, и название у вкладки появились.
"""

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET


@require_GET
def registration_view(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Регистрация",
    }
    return TemplateResponse(
        request,
        "level_1/registration.html",
        context=context,
    )
