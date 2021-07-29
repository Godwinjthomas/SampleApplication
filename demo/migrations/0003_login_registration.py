# Generated by Django 3.2.4 on 2021-06-08 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('demo', '0002_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('mobile', models.BigIntegerField()),
                ('zip', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.login')),
            ],
        ),
    ]
