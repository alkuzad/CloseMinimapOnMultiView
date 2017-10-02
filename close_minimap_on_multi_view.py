import sublime
import sublime_plugin


class CloseMinimapOnMultiView(sublime_plugin.EventListener):

    @staticmethod
    def minimap_visible():
        return sublime.active_window().is_minimap_visible()

    def on_window_command(self, window, cmd_name, args):
        if cmd_name == 'set_layout':
            num = len(args['cells'])
            if num > 1 and self.minimap_visible() is True:
                window.set_minimap_visible(False)
            elif num <= 1 and self.minimap_visible() is False:
                window.set_minimap_visible(True)
