# Generated by Django 4.2.6 on 2023-12-06 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255, verbose_name='Название организации')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('description', models.TextField(verbose_name='Описание стажировки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/internships')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Стажировка',
                'verbose_name_plural': 'Стажировки',
            },
        ),
    ]
