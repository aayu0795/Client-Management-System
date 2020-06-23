from modeltranslation.translator import register, TranslationOptions
from .models import CustomUser, Customer, HomepageHeading, HomepageBody, AboutpageHeading, AboutpageBody


@register(CustomUser)
class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)


@register(Customer)
class UserTranslationOptions(TranslationOptions):
    fields = ('name', 'age', 'gender', 'contact',)


@register(HomepageHeading)
class UserTranslationOptions(TranslationOptions):
    fields = ('main_heading', 'sub_heading',)


@register(HomepageBody)
class UserTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(AboutpageHeading)
class UserTranslationOptions(TranslationOptions):
    fields = ('main_heading', 'sub_heading',)


@register(AboutpageBody)
class UserTranslationOptions(TranslationOptions):
    fields = ('description',)
