"""
У нас есть темплэйт about_us.html с короткой информацией о нас.
Мы ее делали очень давно и сейчас мы называемся Learn Python, да и год указан неправильно, мы работаем с 2013.
Хочется передавать актуальную информацию прямо из вьюхи, а не хардкодить в темплэйте

Задания:
    1. Откройте страницу http://127.0.0.1:8000/about/ и убедитесь, что название комании и год основания уже неактуальны.
    2. Посмотрите какие данные передаются в темплэйт из вьюхи.
    3. Замените в темплэйте about_us.html название компании и год на переменные.
    4. Откройте страницу http://127.0.0.1:8000/about/ и убедитесь, что название комании и год основания актуальные.
"""

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET


@require_GET
def about_us_view(request: HttpRequest) -> HttpResponse:
    company_name = "Learn Python"
    work_from_year = 2013

    return TemplateResponse(
        request,
        "level_1/about_us.html",
        context={
            "title": "О нас",
            "company_name": company_name,
            "work_from_year": work_from_year,
        },
    )
