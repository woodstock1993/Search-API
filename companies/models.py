from django.db import models


# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_kr = models.CharField(max_length=128, null=True, blank=True)
    company_en = models.CharField(max_length=128, null=True, blank=True)
    company_ja = models.CharField(max_length=128, null=True, blank=True)
    tag_ko = models.CharField(max_length=256, null=False, blank=False)
    tag_en = models.CharField(max_length=256, null=False, blank=False)
    tag_ja = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        app_label = 'companies'

    def __str__(self):
        return self.name
