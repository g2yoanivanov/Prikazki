# Generated by Django 3.2 on 2021-06-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommentsSection', '0004_alter_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]