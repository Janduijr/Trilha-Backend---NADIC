from django.db import models

# Create your models here.
class topic(models.Model):
    '''O assunto no qual o usuario esta aprendendo'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''devolve o text'''
        return self.text

class entry(models.Model):
    topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return self.text[:50] + '...'
    
