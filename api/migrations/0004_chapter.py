# Generated by Django 3.2.5 on 2021-07-16 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_story_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=10000)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='api.story')),
            ],
        ),
    ]
