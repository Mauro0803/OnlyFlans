# Generated by Django 3.2.4 on 2024-07-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flan',
            name='flan_uuid',
        ),
        migrations.AddField(
            model_name='flan',
            name='receta',
            field=models.TextField(default='SOME STRING', max_length=20000),
        ),
        migrations.AlterField(
            model_name='flan',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
