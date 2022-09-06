from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


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

SKILLS = (
  ('CSS/HTML', 'CSS/HTML'),
  ('Python', 'Python'),
  ('DJANGO/DRF', 'DJANGO/DRF'),
  ('JavaScript/ReactJS', 'JavaScript/ReactJS')
)


class CustomUser(AbstractUser):
  phone_number = models.CharField(max_length=10, unique=True, blank=True, null=True)
  cv = models.TextField(blank=True, null=True)
  state = models.CharField(max_length=20, choices=STATES, blank=True, null=True)
  interview_notes = models.TextField(default=None, blank=True, null=True)
  feedback_for_mentors = models.TextField(default=None, blank=True, null=True)
  mentor_comments = models.TextField(default=None, blank=True, null=True)
  position = models.CharField(max_length=20, choices=POSITIONS, default=None, blank=True, null=True)
  skills = MultiSelectField(choices=SKILLS, max_choices=3, blank=True, null=True)
  status = models.CharField(max_length=20, choices=STATUS, default='Application received', blank=True, null=True)

  def __str__(self):
    return self.username 


