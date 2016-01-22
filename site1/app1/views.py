
from django.views.generic import TemplateView

from . import plots

class IndexView(TemplateView):
    template_name = "index.html"

class Plot1DView(TemplateView):
    template_name = "plot1d.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot1DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d()
        return context