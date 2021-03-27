from django.db import models

class Blog(models.Model):
    """
    Blog model object.
    """

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # def __init__(self, arg):
    #     super(Blog, self).__init__()
    #     self.arg = arg
