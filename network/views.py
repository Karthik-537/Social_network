from fb_post.models import User,Posts,Comments,Reactions
from django.db.models import Count
def create_post():
    user=User.objects.all().first()
    p=Posts.objects.create(posted_by=user,content='beautiful')
    c=p.pk
    return c
def create_comment():
    user=User.objects.all().first()
    post=Posts.objects.all().first()
    c=Comments.objects.create(content='good',commented_by=user,post_comment=post)
    return c.pk
def react_to_post():
    user=User.objects.all().first()
    post=Posts.objects.all().first()
    r=Reactions.objects.create(post_react=post,reacted_by=user,reaction='WOW')
    return r.pk
def get_total_reaction_count():
    t=Reactions.objects.aggregate(count=Count('reaction'))
    return t
def get_reaction_metrics():
    p=Posts.objects.all().first()
    r=Reactions.objects.filter(post_react=p).values('reaction').annotate(count=Count('reaction'))
    return {reaction['reaction']:reaction['count'] for reaction in r}
def get_posts_reacted_by_user(user_id):
    p=Reactions.objects.filter(reacted_by=user_id).values_list('post_react_id',flat=True)
    return p
def get_reactions_to_post(post_id):
    return Reactions.objects.filter(post_react=post_id).values('reacted_by_id','reacted_by__name','reacted_by__profile_pic','reaction')
def get_posts_with_more_comments_than_reactions():
    P=Posts.objects.annotate(count1=Count('comments'),count2=Count('reactions'))
    return [p.id for p in P if p.count1>p.count2]

def run():
    print(get_posts_with_more_comments_than_reactions())