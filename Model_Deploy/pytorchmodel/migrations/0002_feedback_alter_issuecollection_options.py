# Generated by Django 4.1 on 2022-12-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytorchmodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'FeedBack',
                'verbose_name_plural': 'FeedBacks',
            },
        ),
        migrations.AlterModelOptions(
            name='issuecollection',
            options={'verbose_name': 'Issue', 'verbose_name_plural': 'Issues'},
        ),
    ]