# Generated by Django 4.0.2 on 2022-09-10 05:02

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_merge_20220906_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cv',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='feedback_for_mentors',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='interview_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mentor_comments',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.CharField(blank=True, choices=[('Junior', 'Junior'), ('Lead', 'Lead'), ('Industry', 'Industry')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('CSS/HTML', 'CSS/HTML'), ('Python', 'Python'), ('DJANGO/DRF', 'DJANGO/DRF'), ('JavaScript/ReactJS', 'JavaScript/ReactJS')], default='', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, choices=[('QLD', 'QLD'), ('WA', 'WA'), ('NSW', 'NSW')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('Application received', 'Application received'), ('Unsuccessful', 'Unsuccessful'), ('Ready for interview', 'Ready for interview'), ('Position offered', 'Position offered'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Application received', max_length=20),
        ),
    ]
