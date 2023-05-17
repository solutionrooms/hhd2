# Generated by Django 4.2.1 on 2023-05-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_carer_email_carer_groups_carer_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age_years',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='cold_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='course_of_action',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='current_weather',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='dehydrated_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='finder_name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='fleas_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='fluid_amount',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='fluids_given',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='fly_strike_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='incubator_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='incubator_starting_temp_c',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='limp_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='limping_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='maggots_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='microchip',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='poo_parasites',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='poo_sample',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='pus_or_infection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.TextField(blank=True, choices=[('Male', 'Male'), ('Femail', 'Femail'), ('Unknown', 'Unknown')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='smell_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='sneezing_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='snotty_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='ticks_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='underweight_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='vet_needed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='wants_back',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='wounds_flag',
            field=models.BooleanField(default=False),
        ),
    ]
