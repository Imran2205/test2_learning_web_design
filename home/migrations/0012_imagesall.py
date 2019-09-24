# Generated by Django 2.2.4 on 2019-09-02 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_images10_images2_images3_images4_images5_images6_images7_images8_images9'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image9', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('image10', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Post')),
            ],
        ),
    ]
