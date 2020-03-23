from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.core.models import Orderable
from wagtail.core.blocks import (
  CharBlock, PageChooserBlock, StructValue, StructBlock,
  TextBlock, URLBlock, RichTextBlock
)
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail_localize.models import TranslatablePageMixin, TranslatablePageRoutingMixin

from grapple.models import (
    GraphQLString,
    GraphQLStreamfield,
)

class HomePage(TranslatablePageRoutingMixin, TranslatablePageMixin, Page):
    body = StreamField([
        ('text', blocks.RichTextBlock(features=[
         'h2', 'bold', 'italic', 'link'])),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    subpage_types = ['basecms.ContentPage']

    graphql_fields = [
        GraphQLString('title'),
        GraphQLStreamfield('body'),
    ]

class ContentPage(TranslatablePageMixin, Page):
    LAYOUT_VALUES = (
        ('col1', '1 Col'),
    )
    layout = models.CharField(_('Layout'), max_length=20, choices=LAYOUT_VALUES, default="col1")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('text', blocks.RichTextBlock(features=[
         'h2', 'bold', 'italic', 'ul', 'ol', 'link', 'image', 'document-link']))
    ])

    content_panels = [
        MultiFieldPanel([
            FieldPanel('layout'),
        ], heading=_('Meta')),
    ] + Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['basecms.HomePage']
    subpage_types = ['basecms.ContentPage']

    graphql_fields = [
        GraphQLString('title'),
        GraphQLString('layout'),
        GraphQLStreamfield('body'),
    ]
