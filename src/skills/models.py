from django.db import models

class SkillNode(models.Model):
	skill_name = models.CharField(max_length=200)
	skill_verbose = models.TextField()
	knowledge_count = models.PositiveIntegerField(null=False, default=0)


	class Meta:
		verbose_name = "Skills Meta"