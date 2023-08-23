# Generated by Django 4.0.3 on 2022-03-16 11:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_book', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('genere', models.CharField(max_length=64, null=True)),
                ('body', models.TextField()),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('state', models.PositiveIntegerField(choices=[(0, 'Presented'), (1, 'Accepted'), (2, 'Denied'), (3, 'Revision'), (4, 'Pending images'), (9, 'Translate'), (10, 'Pending published'), (11, 'Published')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('books', models.ManyToManyField(blank=True, related_name='escrip', to='eBook.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('assigned', models.ManyToManyField(blank=True, to='eBook.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Writer', 'Writer'), ('Editor', 'Editor'), ('Editor in chief', 'Editor in chief'), ('Client', 'Client')], max_length=25, verbose_name='Role')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('telefon', models.IntegerField()),
                ('codi_postal', models.IntegerField()),
                ('correo', models.CharField(max_length=64)),
                ('direccion', models.CharField(max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]