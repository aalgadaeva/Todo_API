# Generated by Django 2.2 on 2020-04-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('status_completed', models.BooleanField(default=None, null=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('tags', models.ManyToManyField(related_name='tasks', to='todos.Tag')),
            ],
        ),
    ]
