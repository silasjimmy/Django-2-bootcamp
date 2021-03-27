from django.db import models

class Job(models.Model):
    """
    Job model object.
    """

    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    # def __init__(self, arg):
    #     super(Job, self).__init__()
    #     self.arg = arg
