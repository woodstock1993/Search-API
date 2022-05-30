from django.db import models


# Create your models here.
class Companies(models.Model):
    id = models.AutoField(primary_key=True)
    company_kr = models.CharField(max_length=128, null=True, blank=True)
    company_en = models.CharField(max_length=128, null=True, blank=True)
    company_ja = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.company_kr


class TagLang(models.Model):
    tag_nation = models.CharField(max_length=32)

    class Meta:
        db_table = 'tag_lang'
