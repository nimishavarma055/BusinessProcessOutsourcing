# Generated by Django 2.0 on 2018-10-17 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Name', models.CharField(max_length=200)),
                ('Organization', models.BooleanField(default=True)),
                ('HR_Info', models.FileField(upload_to='docs/')),
            ],
        ),
    ]
