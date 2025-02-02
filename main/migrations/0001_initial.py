# Generated by Django 5.1.2 on 2025-02-02 14:52

import django.db.models.deletion
import main.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('brands', models.CharField(choices=[('bmw', 'BMW'), ('mercedes benz', 'Mercedes Benz'), ('audi', 'Audi'), ('subaru', 'Subaru'), ('tesla', 'Tesla'), ('jaguar', 'Jaguar'), ('land rover', 'Land Rover'), ('bentley', 'Bentley'), ('bugatti', 'Bugatti'), ('ferrari', 'Ferrari'), ('lamborghini', 'Lamborghini'), ('honda', 'Honda'), ('toyota', 'Toyota'), ('chevrolet', 'Chevrolet'), ('porsche', 'Porsche')], default=None, max_length=24)),
                ('model', models.CharField(max_length=64)),
                ('vin', models.CharField(max_length=17)),
                ('mileage', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('engine', models.CharField(max_length=24)),
                ('transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=24)),
                ('image', models.ImageField(upload_to=main.utils.user_listing_path)),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='LikedListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listing')),
            ],
        ),
    ]
