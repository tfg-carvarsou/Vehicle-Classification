# Generated by Django 4.2 on 2024-08-03 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vc_backend_app', '0004_vdimage_gen_time_alter_vdimage_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vdimage',
            old_name='gen_time',
            new_name='inf_time',
        ),
        migrations.AddField(
            model_name='vdimage',
            name='label_count_dict',
            field=models.JSONField(default=dict),
        ),
    ]
