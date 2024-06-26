# Generated by Django 4.2.11 on 2024-04-13 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='KJBCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KJBGoalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('what_did', models.TextField()),
                ('what_like', models.TextField()),
                ('what_not_like', models.TextField()),
                ('what_improve', models.TextField()),
                ('improve_reasons', models.TextField()),
                ('conclusion', models.TextField()),
                ('plan', models.TextField()),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okrapp.checklist')),
            ],
        ),
        migrations.CreateModel(
            name='KJBGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('goal_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okrapp.kjbgoaltype')),
                ('kjb_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okrapp.kjbcategory')),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okrapp.reflection')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='plan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okrapp.kjbgoal'),
        ),
    ]
