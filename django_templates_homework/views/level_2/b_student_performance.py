"""
Оживите шаблон.

Исходите из предположения, что в курсе не может быть больше 3-х недель.
"""

from dataclasses import dataclass

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse


@dataclass
class StudentPerformance:
    student_name: str
    # only three weeks
    weeks: list[bool]


def students_performance_view(request: HttpRequest) -> HttpResponse:
    performances: list[StudentPerformance] = [
        StudentPerformance(
            student_name="Reed Boles",
            weeks=[False, False, False],
        ),
        StudentPerformance(
            student_name="David Mitchell",
            weeks=[True, True, True],
        ),
        StudentPerformance(
            student_name="Teresa Monger",
            weeks=[False, False, True],
        ),
        StudentPerformance(
            student_name="Doris Dayton",
            weeks=[True, False, False],
        ),
    ]
    return TemplateResponse(
        request,
        "level_2/students_performance.html",
        context={"performances": performances},
    )
