import sublime
import sublime_plugin

class SettingsProcessor(object):
    ''' Class to make settings processing easier, it handles project/plugin
    settings split and validation '''

    VALID_CHECK_TYPES = ['cols', 'rows', 'cells']

    def __init__(self, window):
        self.window = window

    # Thanks to CucumberStepFinder for this method
    def _get_setting(self, name):
      # Get the plugin settings, default and user-defined.
      plugin_settings = sublime.load_settings('CloseMinimapOnMultiView.sublime-settings')
      # If this is a project, try to grab project-specific settings.
      if sublime.active_window() and sublime.active_window().active_view():
        project_settings = self.window.active_view().settings().get("CloseMinimapOnMultiView")
      else:
        project_settings = None
      # Grab the setting, by name, from the project settings if it exists.
      # Otherwise, default back to the plugin settings.
      return (project_settings or {}).get(name, plugin_settings.get(name))

    @property
    def check_type(self):
        check_type = self._get_setting('check_type')
        if check_type not in self.VALID_CHECK_TYPES:
            sublime.error_message(
                'Invalid check_type ({}) for CloseMinimapOnMultiView, valid ones are: {}'.format(check_type, self.VALID_CHECK_TYPES))
        return check_type

class MinimapVisibilitySetter(object):
    ''' Class to set minimap visibility based on groups number '''

    def __init__(self, window, check_type):
        self.window = window
        self.check_type = check_type

    def views_number(self):
        if self.check_type == 'cells':
            return len(self.window.get_layout()[self.check_type])
        else:
            return len(self.window.get_layout()[self.check_type]) - 1


    def set_visibility(self):
        if self.views_number() > 1 and self.window.is_minimap_visible() is True:
            self.window.set_minimap_visible(False)
        elif self.views_number() <= 1 and self.window.is_minimap_visible() is False:
            self.window.set_minimap_visible(True)

class CloseMinimapOnMultiView(sublime_plugin.EventListener):

    def on_post_window_command(self, window, cmd_name, _args):
        if cmd_name in ['set_layout', 'new_pane', 'close_pane']:
            settings = SettingsProcessor(window)
            visibility_setter = MinimapVisibilitySetter(window, settings.check_type)
            visibility_setter.set_visibility()

def plugin_loaded():
    for window in sublime.windows():
        settings = SettingsProcessor(window)
        visibility_setter = MinimapVisibilitySetter(window, settings.check_type)
        visibility_setter.set_visibility()
