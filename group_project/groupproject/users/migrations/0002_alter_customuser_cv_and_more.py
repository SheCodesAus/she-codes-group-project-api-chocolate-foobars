# Generated by Django 4.0.2 on 2022-08-31 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cv',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='feedback_for_mentors',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='interview_notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mentor_comments',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.CharField(blank=True, choices=[('Junior', 'Junior'), ('Lead', 'Lead'), ('Industry', 'Industry')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, choices=[('QLD', 'QLD'), ('WA', 'WA'), ('NSW', 'NSW')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(blank=True, choices=[('Application received', 'Application received'), ('Unsucessful', 'Unsucessful'), ('Ready for interview', 'Ready for interview'), ('Position offered', 'Position offered'), ('Active', 'Active'), ('Inactive', 'Inactive')], default='Application received', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='years_industry_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]