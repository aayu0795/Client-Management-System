from django.core.management.base import BaseCommand
from agent_portal.models import CsvFile, CustomUser, Customer
import io
import csv


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        csv_datas = CsvFile.objects.filter(completed=False)

        for csv_data in csv_datas:
            agent_instance = CustomUser.objects.get(id=csv_data.agent_id)

            f = io.TextIOWrapper(csv_data.csv_file.file)
            reader = csv.DictReader(f)
            for customer in reader:
                Customer.objects.get_or_create(agent=agent_instance,
                                               name=customer['name'],
                                               age=customer['age'],
                                               gender=customer['gender'],
                                               contact=customer['contact']
                                               )
            csv_data.completed = True
            csv_data.save()
