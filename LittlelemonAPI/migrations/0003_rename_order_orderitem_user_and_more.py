# Generated by Django 4.1.7 on 2023-02-25 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LittlelemonAPI', '0002_alter_cart_quantity_alter_menuitem_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('user', 'menuitem')},
        ),
        migrations.AddField(
            model_name='order',
            name='orderitem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LittlelemonAPI.orderitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True, db_index=True),
        ),
    ]
