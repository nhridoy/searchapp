from django.db import models
from userprofile.models import User


# Create your models here.
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_search_history')
    search_keyword = models.CharField(max_length=264, verbose_name='Keyword')
    search_results = models.IntegerField(verbose_name='Total Results')
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.search_keyword} at {self.search_date}'

    class Meta:
        verbose_name_plural = 'Search Histories'
        ordering = ('search_date',)
