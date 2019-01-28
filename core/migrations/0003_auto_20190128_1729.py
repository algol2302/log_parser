# Generated by Django 2.1.5 on 2019-01-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190128_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parseddata',
            name='error_code',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Код ответа'),
        ),
        migrations.AlterField(
            model_name='parseddata',
            name='log_date',
            field=models.DateTimeField(db_index=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='parseddata',
            name='uri',
            field=models.TextField(db_index=True, verbose_name='URI'),
        ),
    ]