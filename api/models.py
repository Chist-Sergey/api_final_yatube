from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст",
        help_text="Текст вашего поста"
    )
    pub_date = models.DateTimeField(
        "date published",
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post",
    )
    group = models.ForeignKey(
        "Group",
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Группа",
        help_text="Выберите группу из уже существующих",
        related_name="post"
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Post"
        verbose_name_plural = "Post"

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField(
        max_length=10**3
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ("-created",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"],
                name="unique_follows",
            )
        ]

class Group(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Выберите группу"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.title
