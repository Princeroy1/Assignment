# scheduled_task.py
import os
import sys
import schedule
import time
from datetime import date

# Add the path to your Django project directory
sys.path.append('C:\\Users\\princ\\OneDrive\\Desktop\\Assignment')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Advertisement_system.settings'  # Replace 'myapp' with your Django app name

import django
django.setup()

from add.models import Ad, DailyVisitor  # Adjust the import path as needed
from django.db.models import Q

def reset_blocked_status_and_visitor_count():
    today = date.today()
    filtered_visitors = DailyVisitor.objects.filter(Q(is_blocked=True) | Q(is_blocked=False), ad__end_date=today)
    filtered_visitors.update(is_blocked=True)
    filtered2 = DailyVisitor.objects.filter(
    Q(is_blocked=True) | Q(is_blocked=False),
    ad__end_date__gt=today,
    date__lt=today
)
    filtered2.update(is_blocked=False)

schedule.every().day.at("00:00").do(reset_blocked_status_and_visitor_count)
while True:
    schedule.run_pending()
    time.sleep(1)
