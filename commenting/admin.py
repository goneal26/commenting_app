from django.contrib import admin

# Register your models here.
app = apps.get_app_config('commenting_app')

# Auto register all models using for loop
for model_name, model in app.models.items():
    admin.site.register(model)