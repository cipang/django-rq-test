from django.utils.timezone import now
from rq.job import Job

from main.models import T


class JobBase(Job):

    def perform(self):
        t = T.objects.filter(id=self.id).first()
        try:
            retval = super().perform()
        except Exception as e:
            retval = str(e)
        if t:
            t.value = retval
            t.modified = now()
            t.save()
