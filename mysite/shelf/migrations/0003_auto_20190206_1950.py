# Generated by Django 2.1.5 on 2019-02-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20190205_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last_name'),
        ),
        migrations.AlterField(
            model_name='bookedition',
            name='isbn',
            field=models.CharField(blank=True, max_length=17),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='cover_type',
            field=models.CharField(choices=[('soft', 'Soft'), ('hard', 'Hard')], max_length=4),
        ),
    ]
