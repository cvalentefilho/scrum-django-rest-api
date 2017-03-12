from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Sprint(models.Model):
    """Período de iteração do desenvolvimento"""

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def _str__(self):
        return self.name or _('Sprint ending %s') % self.end
