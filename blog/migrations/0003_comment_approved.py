from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'comment',
            name = 'approved',
            field = models.BooleanField(default=False),
        ),
    ]
