from typing import TypedDict

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET

"""
Задания:
    1. Откройте страницу http://127.0.0.1:8000/contacts/ и наведите на вкладку в браузере, чтобы посмотреть ее название.
       Хотелось бы чего-то более осмысленного.
    2. Найдите в проекте темплэйт contacts_info.html, найдите там сообщение из первого пункта и исправьте на "Контактная информация".
    3. Откройте страницу http://127.0.0.1:8000/contacts/ и убедитесь, что теперь название вкладки соответствует содержанию.
"""


class ContactsInfoView(TypedDict):
    page_title: str
    phone_number: str
    email: str


def get_contacts_context(
    page_title: str = "Контактная информация",
    phone_number: str = "+78455323454",
    email: str = "cooldevs@gmail.com",
) -> ContactsInfoView:
    return ContactsInfoView(
        page_title=page_title,
        phone_number=phone_number,
        email=email,
    )


@require_GET
def contacts_info_view(request: HttpRequest) -> HttpResponse:

    return TemplateResponse(
        request,
        "level_1/contacts_info.html",
        context={**get_contacts_context()},
    )
