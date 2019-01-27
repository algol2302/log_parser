# Generated by Django 2.1.5 on 2019-01-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParsedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.GenericIPAddressField(verbose_name='IP')),
                ('log_date', models.DateTimeField(verbose_name='Дата')),
                ('http_method', models.CharField(max_length=10, verbose_name='Нttp метод')),
                ('uri', models.TextField(verbose_name='URI')),
                ('error_code', models.PositiveIntegerField(default=0, verbose_name='Код ошибки')),
                ('response_size', models.PositiveIntegerField(verbose_name='Размер ответа')),
                ('other', models.TextField(verbose_name='Текст строки')),
            ],
            options={
                'verbose_name': 'Распарсенные данные',
                'verbose_name_plural': 'Распарсенные данные',
            },
        ),
    ]
