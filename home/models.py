from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
    FieldRowPanel,
)
from wagtail.core.models import Page, Orderable


from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.embeds.blocks import EmbedBlock 
from wagtail.images.blocks import ImageChooserBlock
from streams import blocks


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldRowPanel([
            ImageChooserPanel('carousel_image'),
            FieldPanel('caption'),
        ]),
    ]


class SidebarPage(Page):
    """sidebar page odel"""

    template = "home/sidebar_page.html"
    head = RichTextField(features=["bold", "italic"])
    content = StreamField(
        [
            ("two_columns", blocks.TwoColumnBlocks()),
        ],
        null=True,
        blank=True,
    )
    content_panels = [
        FieldPanel('head'),
        StreamFieldPanel('content')
    ]


class HomePage(RoutablePageMixin, Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField([("cta", blocks.CTABlock())], null=True, blank=True)

    api_fields = [
        APIField("banner_title"),
        APIField("banner_subtitle"),
        APIField("banner_image"),
        APIField("banner_cta"),
    ]
  
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),
            
            ("button", blocks.ButtonBlock()),
            ("two_columns", blocks.TwoColumnBlocks()),
            ('embedded_video', EmbedBlock(icon="media")),
            
            ('image', ImageChooserBlock(icon="image")),
        ],
        null=True,
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading="Banner Options",
        ),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images",
        ),
        StreamFieldPanel("content"),

       

    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        return render(request, "home/subscribe.html", context)


