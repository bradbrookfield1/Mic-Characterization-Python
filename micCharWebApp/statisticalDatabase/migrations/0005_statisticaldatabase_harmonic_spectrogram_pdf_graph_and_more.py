# Generated by Django 4.1.2 on 2023-03-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticalDatabase', '0004_statisticaldatabase_spectrogram_pdf_graph'),
    ]

    operations = [
        migrations.AddField(
            model_name='statisticaldatabase',
            name='harmonic_spectrogram_PDF_Graph',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='statisticaldatabase',
            name='percussive_spectrogram_PDF_Graph',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]