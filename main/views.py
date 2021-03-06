from random import randint

from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django_rq import job, enqueue

from main.models import T


class DefaultView(TemplateView):
    template_name = "main_default.html"

    def get_context_data(self, **kwargs):
        qs = T.objects.order_by("-created")
        return {"qs": qs}


@require_POST
def generate_view(request):
    t = T(created=now())
    t.save()
    enqueue(update_record, int(request.POST.get("d") or 0), job_id=str(t.id))
    return redirect("home")


@job
def update_record(d):
    x = randint(10000, 99999) / d
    for i in range(10000000):
        x += (randint(100, 999) - randint(100, 999))
    return f"Added {x}"

