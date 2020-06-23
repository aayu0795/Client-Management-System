from .models import CsvFile, CustomUser, Customer
import io
import csv


def load_csv_file_to_db():
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
