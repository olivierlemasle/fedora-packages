from moksha.lib.base import Controller
from moksha.lib.helpers import MokshaApp
from tg import expose, tmpl_context
from fedoracommunity.widgets import SubTabbedContainer

class TabbedNav(SubTabbedContainer):
    tabs= (MokshaApp('Packages', 'fedoracommunity.packagemaint.packages'),
           MokshaApp('Builds', 'fedoracommunity.builds'),
           MokshaApp('Updates', 'fedoracommunity.updates'),
           MokshaApp('Package Groups', 'fedoracommunity.packagemaint.packagegroups'),
          )

class RootController(Controller):

    def __init__(self):
        self.widget = TabbedNav('packagemaintnav')

    @expose('mako:moksha.templates.widget')
    def index(self):
        tmpl_context.widget = self.widget
        return {'options':{}}