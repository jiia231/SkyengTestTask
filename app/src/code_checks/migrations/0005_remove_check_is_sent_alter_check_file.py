# Generated by Django 4.2.4 on 2023-08-25 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_files", "0002_userfile_created_userfile_updated_and_more"),
        ("code_checks", "0004_remove_check_exit_code_check_result"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="check",
            name="is_sent",
        ),
        migrations.AlterField(
            model_name="check",
            name="file",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lint_check",
                to="user_files.userfile",
            ),
        ),
    ]
