
from django.forms import widgets
from django.db import models
from django.conf import settings

class RichTextField(models.TextField):
    """
    Field is used just to distinguish a rich text field.
    This way, if you'd like to use the Ckeditor in your
    admin, you can just add the following to your ModelAdmin:

    formfield_overrides = {
        models.RichTextField: {'widget': fields.CkeditorWidget},
    }

    and your richtext field will use the Ckeditor.
    """
    pass

class CkeditorWidget(widgets.Textarea):
    """Ckeditor is a richtext editor. Most basic usage requires a class
    of ckeditor so the javascript knows what to change."""

    def __init__(self, attrs=None):
        default_attrs = {'class':"ckeditor"}
        if attrs:
            default_attrs.update(attrs)
        super(CkeditorWidget, self).__init__(default_attrs)

    class Media:
        css = {'all': (settings.STATIC_URL + "ckeditor/ckeditor.css",)}
        js = (settings.STATIC_URL + "ckeditor/ckeditor.js",)

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])
except ImportError:
    pass