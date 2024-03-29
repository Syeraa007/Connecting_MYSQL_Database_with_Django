# Generated by Django 4.2.1 on 2023-07-26 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.page')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.topic'),
        ),
    ]
