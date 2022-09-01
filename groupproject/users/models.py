from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


STATES = (
  ('QLD', 'QLD'),
  ('WA', 'WA'),
  ('NSW', 'NSW'),
)

POSITIONS = (
  ('Junior', 'Junior'),
  ('Lead', 'Lead'),
  ('Industry', 'Industry'),
)

STATUS = (
  ('Application received', 'Application received'),
  ('Unsucessful', 'Unsucessful'),
  ('Ready for interview', 'Ready for interview'),
  ('Position offered', 'Position offered'),
  ('Active', 'Active'),
  ('Inactive', 'Inactive'),
)

class CustomUser(AbstractUser):
  phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
  cv = models.TextField(blank=True, null=True)
  state = models.CharField(max_length=20, choices=STATES, blank=True, null=True)
  years_industry_experience = models.IntegerField(blank=True, null=True)
  interview_notes = models.TextField(default=None, blank=True, null=True)
  feedback_for_mentors = models.TextField(default=None, blank=True, null=True)
  mentor_comments = models.TextField(default=None, blank=True, null=True)
  # update to foreign keys when position and status models are created
  position = models.CharField(max_length=20, choices=POSITIONS, default=None, blank=True, null=True)
  status = models.CharField(max_length=20, choices=STATUS, default='Application received', blank=True, null=True)

  def __str__(self):
    return self.username 

class Skills(models.Model):
  skill = models.CharField(max_length=200)

class MentorSkills(models.Model):
  mentor_id = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name="mentor_skills"
  )
  skill_id = models.ForeignKey(
    'Skills',
    on_delete=models.CASCADE,
    related_name="skills_id"
  )