from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class TreeMenu(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name=_('Menu Name')
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_('Parent Menu'),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'menu:menu_list',
            kwargs={'menu_slug': self.slug}
        )

    class Meta:
        db_table = 'tree_menu'
        verbose_name = _('Tree Menu')
        verbose_name_plural = _('Tree Menu')
