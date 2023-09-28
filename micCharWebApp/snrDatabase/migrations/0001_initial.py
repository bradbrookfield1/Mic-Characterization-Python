# Generated by Django 4.1.2 on 2023-03-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('micCharacterization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SNRDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pure_Signal_SNR_Graph', models.CharField(default=None, max_length=1000, null=True)),
                ('system_Signal_SNR_Graph', models.CharField(default=None, max_length=1000, null=True)),
                ('given_Signal_SNR_Graph', models.CharField(default=None, max_length=1000, null=True)),
                ('given_Noise_SNR_Graph', models.CharField(default=None, max_length=1000, null=True)),
                ('average_SNR_Distance_Graph', models.CharField(default=None, max_length=1000, null=True)),
                ('mic_Data_Record', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='micCharacterization.micdatarecord')),
            ],
        ),
    ]