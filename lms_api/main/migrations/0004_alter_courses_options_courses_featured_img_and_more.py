# Generated by Django 4.0.6 on 2023-01-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_address_teacher_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name_plural': '3.courses'},
        ),
        migrations.AddField(
            model_name='courses',
            name='featured_img',
            field=models.ImageField(null=True, upload_to='course_imgs/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='tech',
            field=models.TextField(null=True),
        ),
    ]