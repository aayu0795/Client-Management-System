from django.contrib import admin
from .models import (
    CustomUser,
    Customer,
    HomepageHeading,
    HomepageBody,
    AboutpageHeading,
    AboutpageBody,
)


admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(HomepageHeading)
admin.site.register(HomepageBody)
admin.site.register(AboutpageHeading)
admin.site.register(AboutpageBody)
