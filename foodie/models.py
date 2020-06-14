from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_l = models.CharField("大業態コード", max_length=10, blank=False)
    name = models.CharField("カテゴリ名", max_length=30, blank=False)

    def __str__(self):
        return str(self.name)

class Area(models.Model):
    areacode_m = models.CharField("エリアコード", max_length=10, blank=False)
    name = models.CharField("エリア名", max_length=10, blank=False)

    def __str__(self):
        return str(self.name)

class Review(models.Model):
    SCORE_CHOICES= [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    shop_id = models.CharField('レストランID', max_length=10, blank=False)
    shop_name = models.CharField('レストラン名', max_length=200, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField(verbose_name='口コミ', blank=False)
    score = models.PositiveSmallIntegerField(verbose_name='スコア', choices=SCORE_CHOICES, default='3')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_score_percent(self):
        score_percent = round(self.score / 5 * 100)
        return score_percent

    class Meta:
        unique_together = ('shop_id', 'user')

    def __str__(self):
        return str(self.shop_id)

