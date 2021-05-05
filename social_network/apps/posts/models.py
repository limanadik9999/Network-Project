from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post_title = models.CharField('Title', max_length = 150, blank = True)
    post_text = models.TextField('Description')
    post_image = models.ImageField('Image', blank = True, upload_to = 'images/post/')
    post_image_url = models.ImageField('Image URG', blank = True)
    post_time = models.DateTimeField('Creation date/time')
    post_like = models.ManyToManyField(User,
                                        related_name='post_liked',
                                        blank=True)
    post_dislike = models.ManyToManyField(User,
                                        related_name='post_disliked',
                                        blank=True)

    def __str__(self):
        return str(self.author)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


class Like(models.Model):
    LIKE_OR_DISLAKE_CHOICES = (
    ("LIKE", "like"),
    ("DISLIKE", "dislike"),
    (None, "None")
    )

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    for_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    like_or_dislike = models.CharField(max_length=7,
                  choices=LIKE_OR_DISLAKE_CHOICES,
                  default=None)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="post_comments")
    comment_author = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.CharField('Comment', max_length = 350)
    comment_pubdate = models.DateTimeField('Publication date')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
