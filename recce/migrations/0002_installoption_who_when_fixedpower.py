from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("settingsapp", "0001_initial"),
        ("recce", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="installoption",
            name="installed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="recce_install_options",
                to="settingsapp.person",
                verbose_name="Wer",
            ),
        ),
        migrations.AddField(
            model_name="installoption",
            name="installed_on",
            field=models.DateField(blank=True, null=True, verbose_name="Wann"),
        ),
        migrations.AddField(
            model_name="installoption",
            name="fixed_power",
            field=models.BooleanField(default=False, verbose_name="Feststrom"),
        ),
    ]
