import sys
import os
import django
import csv

# system setup
sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
django.setup()

from django.conf import settings
from companies.models import Company

# db upload
base_path = settings.DATA_ROOT
csv_path = base_path + '\wanted_temp_data.csv'


# companies.Company
def insert_company():
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        data_reader = csv.DictReader(csv_file)

        Company.objects.all().delete()
        for row in data_reader:
            if row['company_ko']:
                Company.objects.get_or_create(
                    company_kr=row['company_ko'],
                    company_en=row['company_en'],
                    company_ja=row['company_ja'],
                    tag_ko=row['tag_ko'],
                    tag_en=row['tag_en'],
                    tag_ja=row['tag_ja'])
        print("Company CSV UPLOADED SUCCESS!")


insert_company()
