from django.core.management.base import BaseCommand
from agent_portal.models import HomepageHeading, HomepageBody, AboutpageHeading, AboutpageBody
import os


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        HomepageHeading.objects.create(
            main_heading='Hello world!',
            main_heading_en_us='Hello world!',
            main_heading_es='¡Hola Mundo!',
            sub_heading="Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.",
            sub_heading_en_us="Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.",
            sub_heading_es="Múltiples líneas de texto que forman el lede, informando a los nuevos lectores de manera rápida y eficiente sobre lo que es más interesante en el contenido de esta publicación."
        )

        for _ in range(3):
            HomepageBody.objects.create(
                description="This blog post shows a few different types of content that’s supported and styled with Bootstrap. Basic typography, images, and code are all supported.",
                description_en_us="This blog post shows a few different types of content that’s supported and styled with Bootstrap. Basic typography, images, and code are all supported.",
                description_es="Esta publicación de blog muestra algunos tipos diferentes de contenido compatible y diseñado con Bootstrap. La tipografía básica, las imágenes y el código son compatibles.",
                thumbnail='/dummy_img.jpg',
            )

        AboutpageHeading.objects.create(
            main_heading='About us!',
            main_heading_en_us='About us!',
            main_heading_es='Sobre nosotros',
            sub_heading="Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.",
            sub_heading_en_us="Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.",
            sub_heading_es="Múltiples líneas de texto que forman el lede, informando a los nuevos lectores de manera rápida y eficiente sobre lo que es más interesante en el contenido de esta publicación."
        )

        for _ in range(3):
            AboutpageBody.objects.create(
                description="This blog post shows a few different types of content that’s supported and styled with Bootstrap. Basic typography, images, and code are all supported.",
                description_en_us="This blog post shows a few different types of content that’s supported and styled with Bootstrap. Basic typography, images, and code are all supported.",
                description_es="Esta publicación de blog muestra algunos tipos diferentes de contenido compatible y diseñado con Bootstrap. La tipografía básica, las imágenes y el código son compatibles.",
                thumbnail='/dummy_img.jpg',
            )

        self.stdout.write(self.style.SUCCESS(
            "Dummy data has been loaded successfully!"))
