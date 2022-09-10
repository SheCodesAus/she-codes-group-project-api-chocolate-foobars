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
  ('Unsuccessful', 'Unsuccessful'),
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
  phone_number = models.CharField(max_length=10, unique=True, blank=True)
  cv = models.TextField(blank=True)
  state = models.CharField(max_length=20, choices=STATES, blank=True)
  interview_notes = models.TextField(blank=True)
  feedback_for_mentors = models.TextField(blank=True)
  mentor_comments = models.TextField(blank=True)
  position = models.CharField(max_length=20, choices=POSITIONS, blank=True)
  skills = MultiSelectField(choices=SKILLS, max_choices=3, blank=True)
  status = models.CharField(max_length=20, choices=STATUS, default='Application received')

  def __str__(self):
    return self.username 


