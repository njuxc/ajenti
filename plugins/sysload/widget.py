from ajenti.ui import *
from ajenti.plugins.dashboard.api import *
from ajenti.com import implements, Plugin
from ajenti.api import *
from ajenti import apis


class LoadWidget(Plugin):
    implements(IDashboardWidget)

    def get_ui(self):
        stat = self.app.get_backend(apis.sysstat.ISysStat)
        w = UI.Widget(
                UI.HContainer(
                    UI.Image(file='/dl/sysload/widget.png'),
                    UI.Label(text='System load:', bold=True),
                    UI.Label(text=' / '.join(stat.get_load()))
                )
            )
        return w
    

class MemWidget(Plugin):
    implements(IDashboardWidget)

    def get_ui(self):
        stat = self.app.get_backend(apis.sysstat.ISysStat)
        ru, rt = stat.get_ram()
        su, st = stat.get_swap()
        w = UI.Widget(
                UI.LayoutTable(
                    UI.LayoutTableRow(
                        UI.Image(file='/dl/sysload/widget_mem.png'),
                        UI.Label(text='RAM:', bold=True),
                        UI.ProgressBar(value=ru, max=rt, width=100),
                        UI.Label(text="%sM / %sM"%(ru,rt)),
                        spacing=4
                    ),
                    UI.LayoutTableRow(
                        UI.Image(file='/dl/sysload/widget_swap.png'),
                        UI.Label(text='Swap:', bold=True),
                        UI.ProgressBar(value=su, max=st, width=100) if int(st) != 0 else None,
                        UI.Label(text="%sM / %sM"%(su,st)),
                        spacing=4
                    )
                )
            )
        return w


class LoadContent(ModuleContent):
    module = 'sysload'
    path = __file__
