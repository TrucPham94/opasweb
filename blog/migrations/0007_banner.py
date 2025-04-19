# Generated by Django 5.1.4 on 2025-04-18 02:36

import blog.function
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_thongbao_loai_bai_viet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.function.RenameFileImage('banner', 'id'))),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
        ),
    ]
