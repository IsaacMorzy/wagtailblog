from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media settings for our custom website."""

    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    github = models.URLField(blank=True, null=True, help_text="Github Repo URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("github"),
        ], heading="Social Media Settings")
    ] 