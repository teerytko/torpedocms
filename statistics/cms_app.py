from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class StatisticsApphook(CMSApp):
    name = _("Statistics App")
    urls = ["statistics.urls"]

apphook_pool.register(StatisticsApphook)