from django.db import models
REACTION_CHOICES = [
    ('WOW', 'Wow'),
    ('LIT', 'Lit'),
    ('LOVE', 'Love'),
    ('HAHA', 'Haha'),
    ('THUMBS-UP', 'Thumbs Up'),
    ('THUMBS-DOWN', 'Thumbs Down'),
    ('ANGRY', 'Angry'),
    ('SAD', 'Sad')
]
class User(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=100)
class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
class Posts(models.Model):
    content = models.CharField(max_length=1000)
    posted_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    group_post = models.ForeignKey(Group,null=True,blank=True, on_delete=models.CASCADE)
class Comments(models.Model):
    content = models.CharField(max_length=1000)
    commented_at = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_comment = models.ForeignKey(Posts, null=True, blank=True, on_delete=models.CASCADE)
    self_comment = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
class Reactions(models.Model):
    post_react = models.ForeignKey(Posts, null=True, blank=True, on_delete=models.CASCADE)
    comment_react = models.ForeignKey(Comments, null=True, blank=True, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=100, choices=REACTION_CHOICES)
    reacted_at = models.DateTimeField(auto_now_add=True)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)
class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    class Meta:
        unique_together = ('group', 'user')