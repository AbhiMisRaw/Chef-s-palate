# Generated by Django 4.2.4 on 2023-10-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzu9W2lPY8qu3gj5clTMrxES8fFWkjgWPpIQ&usqp=CAU', max_length=500),
        ),
    ]
