import os,sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()
from author.models import Author
import csv

try:
    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row[0] == 'name' and not row[0] == '' :
                newAuthor = Author( name = row[0])
                print('Author:'+row[0])
                newAuthor.save()
                print('Sucess!')
except:
    print('Fail!')








