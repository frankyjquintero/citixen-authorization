# Generated by Django 2.2.3 on 2019-08-02 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('-created_at', '-updated_at')},
        ),
        migrations.AlterModelOptions(
            name='headquarter',
            options={'ordering': ('-created_at', '-updated_at')},
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='company',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='headquarter',
            name='city',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headquarter',
            name='country',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headquarter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headquarter',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='headquarter',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='headquarter',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='headquarter',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]