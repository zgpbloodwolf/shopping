# Generated by Django 2.1.7 on 2019-06-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190627_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_user', models.CharField(max_length=20)),
                ('car_co', models.IntegerField()),
                ('car_number', models.IntegerField()),
                ('car_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_image', models.ImageField(default='aaa', upload_to='')),
                ('co_brief_introduction', models.CharField(default='a', max_length=50)),
                ('or_sele', models.IntegerField()),
                ('or_evaluate', models.IntegerField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
