from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recce", "0002_installoption_who_when_fixedpower"),
    ]

    operations = [
        migrations.AddField(
            model_name="fixedviewmarker",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="fixedviewmarker",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="installphotomarker",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="installphotomarker",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        # Backfill nulls then set NOT NULL by recreating field without null (Django handles on DBs that support it)
        migrations.AlterField(
            model_name="fixedviewmarker",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="fixedviewmarker",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="installphotomarker",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="installphotomarker",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
