from django.contrib import admin
from django.apps import apps

store_models = apps.get_app_config('store').get_models()

for model in store_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass