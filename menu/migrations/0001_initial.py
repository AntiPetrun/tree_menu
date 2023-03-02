# Generated by Django 4.1.7 on 2023-03-01 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Menu Name')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='menu.treemenu', verbose_name='Parent Menu')),
            ],
            options={
                'verbose_name': 'Tree Menu',
                'verbose_name_plural': 'Tree Menu',
                'db_table': 'tree_menu',
            },
        ),
    ]
