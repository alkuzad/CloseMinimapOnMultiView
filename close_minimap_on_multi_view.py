import sublime
import sublime_plugin

def plugin_loaded():
    for window in sublime.windows():
        if window.num_groups() > 1:
            window.set_minimap_visible(False)

class CloseMinimapOnMultiView(sublime_plugin.EventListener):

    @staticmethod
    def minimap_visible(window):
        return window.is_minimap_visible()

    def on_post_window_command(self, window, cmd_name, args):
        num = None
        if cmd_name == 'set_layout':
            num = len(args['cols']) -1
        elif cmd_name in ['new_pane', 'close_pane']:
            num = window.num_groups()['cols']  -1
        if num is not None:
            if num > 1 and self.minimap_visible(window) is True:
                window.set_minimap_visible(False)
            elif num <= 1 and self.minimap_visible(window) is False:
                window.set_minimap_visible(True)
