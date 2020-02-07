# Generated by Django 3.0.3 on 2020-02-07 15:56

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_auto_20200207_1556'),
        ('internationalization', '0004_auto_20200207_1556'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='internationalization.Country'),
        ),
        migrations.AddField(
            model_name='location',
            name='map_bounds',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internationalization.LatLngBounds'),
        ),
        migrations.AddField(
            model_name='location',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locations', to='internationalization.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('country', 'code')},
        ),
    ]