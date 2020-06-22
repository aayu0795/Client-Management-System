from modeltranslation.translator import register, TranslationOptions
from .models import CustomUser, Customer


@register(CustomUser)
class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'username', )


@register(Customer)
class UserTranslationOptions(TranslationOptions):
    fields = ('name', 'age', 'gender', 'contact',)
