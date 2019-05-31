from django.contrib import admin
from .models import Author

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Portfolio)
admin.site.register(PortfolioBook)
admin.site.register(Category)
admin.site.register(Author)

