import json
# Replace 'your_app' with the name of your Django app
from .models import Tafseer


def populate_database(json_file):
    # Load the JSON file
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # Iterate over each item in the JSON data and create model instances
    for item in data['ayahs']:
        surah = item['surah']
        ayah = item['ayah']
        text = item['text']

        # Create a new Tafseer instance and save it to the database
        tafseer = Tafseer.objects.create(surah=surah, ayah=ayah, text=text)
        tafseer.save()


# Call the function and pass the path to your merged JSON file
