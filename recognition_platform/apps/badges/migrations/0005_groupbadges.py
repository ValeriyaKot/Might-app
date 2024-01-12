# Generated by Django 3.2.3 on 2021-08-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('badges', '0004_employeebadge_isanonymous'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupBadges',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='')),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
    ]
