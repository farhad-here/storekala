# fix_migrations.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # اسم پروژه‌ات رو چک کن
django.setup()

from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM django_migrations WHERE app='stores'")
    print("stores migration record deleted!")