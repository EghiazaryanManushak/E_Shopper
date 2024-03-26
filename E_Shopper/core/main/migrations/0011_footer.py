# Generated by Django 4.0.5 on 2022-06-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='Footer about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Footer img')),
                ('name1', models.CharField(max_length=50, verbose_name='Footer name1')),
                ('name2', models.CharField(max_length=50, verbose_name='Footer name2')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footers',
            },
        ),
    ]