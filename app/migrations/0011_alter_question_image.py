# Generated by Django 5.0.4 on 2024-04-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_question_image_path_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(default='cot.jpg', upload_to='questions/'),
        ),
    ]
