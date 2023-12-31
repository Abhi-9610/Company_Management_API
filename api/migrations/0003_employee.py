# Generated by Django 4.2.5 on 2023-10-22 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_updated_on_companyapi_added_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=2)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('position', models.CharField(choices=[('manager', 'Manager'), ('Software developer', 'Software developer'), ('product Manager', 'product manager'), ('Team Leader', 'Team Leader')], max_length=50)),
                ('address', models.TextField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.companyapi')),
            ],
        ),
    ]
