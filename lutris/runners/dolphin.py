import os
from lutris.runners.runner import Runner
from gettext import gettext as _

class dolphin(Runner):
    description = _("Gamecube and Wii emulator")
    human_name = "Dolphin"
    platforms = [
        'Nintendo Gamecube',
        'Nintendo Wii',
    ]
    runnable_alone = True
    runner_executable = 'dolphin/dolphin-emu'
    game_options = [
        {
            "option": "main_file",
            "type": "file",
            "default_path": "game_path",
            "label": _("ISO file")
        },
        {
            'option': 'platform',
            'type': 'choice',
            'label': _('Platform'),
            'choices': (
                ('Nintendo Gamecube', '0'),
                ('Nintendo Wii', '1')
            )
        }
    ]
    runner_options = []

    def get_platform(self):
        selected_platform = self.game_config.get('platform')
        if selected_platform:
            return self.platforms[int(selected_platform)]
        else:
            return ''

    def play(self):
        iso = self.game_config.get('main_file') or ''
        if not os.path.exists(iso):
            return {'error': 'FILE_NOT_FOUND', 'file': iso}
        return {'command': [self.get_executable(), '-e', iso]}
