# Generated by Django 2.1.4 on 2018-12-07 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('why', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='what',
            old_name='to',
            new_name='action',
        ),
        migrations.RenameField(
            model_name='what',
            old_name='etc',
            new_name='notes',
        ),
        migrations.RenameField(
            model_name='what',
            old_name='do',
            new_name='result',
        ),
        migrations.RemoveField(
            model_name='what',
            name='whom',
        ),
        migrations.AddField(
            model_name='what',
            name='for_whom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='for_whom', to='why.Who'),
        ),
        migrations.AddField(
            model_name='what',
            name='with_who',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='with_who', to='why.Who'),
        ),
        migrations.AddField(
            model_name='who',
            name='django_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]