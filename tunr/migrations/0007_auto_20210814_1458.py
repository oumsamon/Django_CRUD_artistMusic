# Generated by Django 3.2.6 on 2021-08-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0006_alter_song_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Random',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_fields', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='preview_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
