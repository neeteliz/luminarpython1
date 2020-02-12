# Generated by Django 2.0.5 on 2020-02-12 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=250)),
                ('eid', models.CharField(max_length=8)),
                ('esal', models.IntegerField()),
                ('design', models.CharField(max_length=260)),
            ],
        ),
    ]