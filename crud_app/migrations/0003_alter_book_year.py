# Generated by Django 5.0 on 2024-05-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateTimeField(blank=True, null=True, verbose_name='chop etilgan sanasi'),
        ),
    ]
