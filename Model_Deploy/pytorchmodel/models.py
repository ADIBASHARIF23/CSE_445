from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class RecordCollection(models.Model):
        complaint = models.CharField(max_length=500, primary_key=True)
        issue = models.CharField(max_length=30)
        aspect = models.CharField(max_length=30)
        class Meta:
            verbose_name = _("Issue")
            verbose_name_plural = _("Issues")

        def __str__(self):
            return self.issue
        
        
        
class FeedBack(models.Model):
    name =  models.CharField(max_length=100, primary_key=True)
    review =  models.CharField(max_length=500)

    class Meta:
        verbose_name = _("FeedBack")
        verbose_name_plural = _("FeedBacks")

    def __str__(self):
        return self.name

