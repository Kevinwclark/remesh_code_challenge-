# Generated by Django 3.1.6 on 2021-02-13 02:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='message.message')),
            ],
        ),
    ]
