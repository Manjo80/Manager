from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recce", "0002_installoption_who_when_fixedpower"),
    ]

    operations = [
        migrations.AddField(
            model_name="installphotomarker",
            name="x2",
            field=models.FloatField(blank=True, help_text="0..1 (arrow end x)", null=True),
        ),
        migrations.AddField(
            model_name="installphotomarker",
            name="y2",
            field=models.FloatField(blank=True, help_text="0..1 (arrow end y)", null=True),
        ),
        migrations.AddField(
            model_name="fixedviewmarker",
            name="x2",
            field=models.FloatField(blank=True, help_text="0..1 (arrow end x)", null=True),
        ),
        migrations.AddField(
            model_name="fixedviewmarker",
            name="y2",
            field=models.FloatField(blank=True, help_text="0..1 (arrow end y)", null=True),
        ),
        migrations.AlterField(
            model_name="fixedviewmarker",
            name="marker_type",
            field=models.CharField(
                choices=[("rect", "Rechteck"), ("circle", "Kreis"), ("cross", "Kreuz"), ("arrow", "Pfeil")],
                default="rect",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="installphotomarker",
            name="marker_type",
            field=models.CharField(
                choices=[("rect", "Rechteck"), ("circle", "Kreis"), ("cross", "Kreuz"), ("arrow", "Pfeil")],
                default="rect",
                max_length=10,
            ),
        ),
    ]
