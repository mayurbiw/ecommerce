# Generated by Django 3.1.4 on 2021-01-12 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_site', '0003_auto_20210106_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('placed', 'placed'), ('shipped', 'shipped'), ('delivered', 'delivered')], db_column='status__c', max_length=255)),
                ('Product2Id', models.ForeignKey(db_column='Product2Id__c', on_delete=django.db.models.deletion.DO_NOTHING, to='app_site.product')),
                ('user_id', models.ForeignKey(db_column='user_id__c', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ReviseOrder',
                'verbose_name_plural': 'ReviseOrders',
                'db_table': 'ReviseOrder__c',
            },
        ),
    ]
