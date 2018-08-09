# Generated by Django 2.0.3 on 2018-03-25 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brewed_on', models.DateTimeField(auto_now_add=True)),
                ('grinder_setting', models.CharField(max_length=200)),
                ('volume_beans', models.PositiveIntegerField(help_text='in gram')),
                ('volume_water', models.PositiveIntegerField(help_text='in gram')),
                ('temperature', models.PositiveIntegerField(help_text='in Celsius')),
                ('extraction_time', models.DurationField(default='00:MM:ss', help_text='as HH:MM:ss')),
                ('description', models.TextField()),
                ('remark', models.TextField()),
                ('rating', models.IntegerField(default=0, help_text='use negative values for bad, positive for good results')),
            ],
        ),
        migrations.CreateModel(
            name='BrewType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('continent', models.PositiveIntegerField(choices=[(1, 'AFRICA'), (2, 'ASIA_TEMPERATE'), (3, 'ASIA_TROPICAL'), (4, 'AUSTRALASIA'), (5, 'EUROPE'), (6, 'PACIFIC'), (7, 'NORTH_AMERICA'), (8, 'SOUTH_AMERICA')])),
            ],
        ),
        migrations.CreateModel(
            name='Grinder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('volume', models.PositiveIntegerField(default=250, help_text='in gram')),
                ('roasted_on', models.DateField(blank=True, null=True)),
                ('opened_on', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cohi.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Roaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cohi.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cohi.Producer'),
        ),
        migrations.AddField(
            model_name='package',
            name='roaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cohi.Roaster'),
        ),
        migrations.AddField(
            model_name='brew',
            name='grinder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cohi.Grinder'),
        ),
        migrations.AddField(
            model_name='brew',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cohi.Package'),
        ),
        migrations.AddField(
            model_name='brew',
            name='technique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cohi.Technique'),
        ),
        migrations.AddField(
            model_name='brew',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cohi.BrewType'),
        ),
    ]