# Generated by Django 3.1b1 on 2021-06-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20210610_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='educational_qualification',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('Ssce', 'SSCE'), ('Nd', 'ND'), ('Hnd', 'HND'), ('BSc', 'BSc/BEng'), ('MASTERS', 'Masters')], max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='jod_title',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('PHPWEB', 'PHP Web Developer'), ('DJANGOWEB', 'Django Web Developer'), ('APP DEVELOPER', 'App Developer'), ('SOFTWARE DEVELOPER', 'Software Developer'), ('AI DEVELOPER', 'Artificial Intelligent Engineer'), ('ELECT/ELECT', 'Electrical/Electronic Engineer'), ('RECEPTIONIST', 'Receptionist'), ('DATA_SCIENTIST', 'Data Scientist'), ('FRONT_END_DEV.', 'Front End Developer'), ('MACHINE LEARNING ENGR,', 'Machine Learning Engineer'), ('PYTHON_DEV', 'Python Developer')], max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='state',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'), ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'), ('Im', 'Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'), ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'), ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'), ('Zamfa', 'Zamfara'), ('FCT', 'Abuja')], max_length=30),
        ),
        migrations.AlterField(
            model_name='it',
            name='cgpa',
            field=models.CharField(choices=[('choose...', 'choose CGPA range...'), ('first class', '4.50 - 5.00'), ('second class upper', '3.50 - 4.49'), ('second class lower', '2.50 - 3.49'), ('others', '1.00 - 2.49')], max_length=30),
        ),
        migrations.AlterField(
            model_name='it',
            name='state',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'), ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'), ('Im', 'Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'), ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'), ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'), ('Zamfa', 'Zamfara'), ('FCT', 'Abuja')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ordernow',
            name='state',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('ab', 'Abia'), ('ada', 'Adamawa'), ('aks', 'Akwa Ibom'), ('bau', 'Bauchi'), ('bay', 'Bayelsa'), ('ben', 'Benue'), ('bor', 'Borno'), ('crs', 'Cross River'), ('del', 'Delta'), ('ebo', 'Ebonyi'), ('Ed', 'Edo'), ('Eki', 'Ekiti'), ('Enu', 'Enugu'), ('Gom', 'Gombe'), ('Im', 'Imo'), ('Jiga', 'Jigawa'), ('Kadu', 'Kaduna'), ('Kan', 'Kano'), ('Kat', 'Katsina'), ('Keb', 'Kebbi'), ('Kog', 'Kogi'), ('Kwa', 'Kwara'), ('Lag', 'Lagos'), ('Nasa', 'Nasarawa'), ('Nig', 'Niger'), ('Ogu', 'Ogun'), ('Ond', 'Ondo'), ('Osu', 'Osun'), ('Oy', 'Oyo'), ('Pla', 'Plateau'), ('Rs', 'Rivers'), ('Sok', 'Sokoto'), ('Tara', 'Taraba'), ('Yob', 'Yobe'), ('Zamfa', 'Zamfara'), ('FCT', 'Abuja')], max_length=30),
        ),
    ]
