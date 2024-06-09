"""
Оживите шаблон.

Обратите внимание, что потенциально мошеннические транзакции подсвечиваются красным цветом в таблице.
"""

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from django_templates_homework.generators.transactions import generate_fake_transactions


def transactions_list_view(request: HttpRequest) -> HttpResponse:
    transactions = generate_fake_transactions(num=100)
    return TemplateResponse(
        request,
        "level_2/transactions_list.html",
        context={"transactions": transactions},
    )
