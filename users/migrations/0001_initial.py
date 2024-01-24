# Generated by Django 5.0.1 on 2024-01-24 02:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('business_name', models.CharField(max_length=100)),
                ('business_category', models.CharField(choices=[('individual', 'Individual/Freelancer'), ('accounting', 'Accounting and Bookkeeping'), ('agriculture', 'Agriculture'), ('association', 'Association/Club'), ('automobile', 'Automobile'), ('business_consulting', 'Business Consulting'), ('clinic_healthcare', 'Clinic and Healthcare Services'), ('construction_engineering', 'Construction and Engineering'), ('education', 'Education'), ('technology', 'Technology')], max_length=50)),
                ('transaction_currency', models.CharField(max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]