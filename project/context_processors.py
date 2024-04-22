from django.conf import settings


def settings_context_processor(request):
    my_dict = {
        "SITE_TITLE": getattr(settings, "SITE_TITLE", "My Website"),
        "SITE_CONTACT_EMAIL": getattr(settings, "SITE_CONTACT_EMAIL", "combmichi@uc.edu"),
    }

    return my_dict
