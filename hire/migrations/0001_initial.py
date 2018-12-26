# Generated by Django 2.1.1 on 2018-12-15 14:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{10,15}$')])),
                ('description', models.CharField(max_length=10000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_category', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('intake', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('description', models.CharField(max_length=10000)),
                ('other_requirements', models.CharField(max_length=10000)),
                ('perks', models.CharField(max_length=10000)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire.Company')),
            ],
        ),
        migrations.AddField(
            model_name='applications',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire.JobPost'),
        ),
        migrations.AddField(
            model_name='applications',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply.Student'),
        ),
    ]