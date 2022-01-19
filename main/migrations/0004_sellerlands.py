# Generated by Django 4.0 on 2022-01-12 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_landinformation_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerLands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.landinformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seller')),
            ],
        ),
    ]