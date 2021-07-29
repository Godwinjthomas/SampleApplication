# Generated by Django 3.2.4 on 2021-06-10 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0004_auto_20210608_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('zip', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='loginid',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]