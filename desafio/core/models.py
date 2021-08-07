from django.db import models
from django.utils.translation import gettext_lazy as _

from desafio.utils import CommonModel


class State(CommonModel):
    code = models.CharField(verbose_name=_('Sigla do Estado'), max_length=2)
    name = models.CharField(verbose_name=_('Nome do Estado'), max_length=255)

    class Meta:
        verbose_name = _('Estado')
        verbose_name_plural = _('Estados')
        ordering = ('code',)
        constraints = [
            models.UniqueConstraint(
                fields=['code'],
                name='unique_state'
            )
        ]

    def __str__(self) -> str:
        return self.code


class City(CommonModel):
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, verbose_name=_('Cidade')
    )
    name = models.CharField(verbose_name=_('Nome da Cidade'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug Cidade'), default='')

    class Meta:
        verbose_name = _('Cidade')
        verbose_name_plural = _('Cidades')
        ordering = ('name',)
        constraints = [
            models.UniqueConstraint(
                fields=['state', 'name'],
                name='unique_city'
            )
        ]

    def __str__(self) -> str:
        return self.name
