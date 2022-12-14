# Generated by Django 4.0.6 on 2022-08-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
                ('skill_verbose', models.TextField()),
                ('knowledge_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Skills Meta',
            },
        ),
    ]
