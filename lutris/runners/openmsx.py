import os
from lutris.runners.runner import Runner
from gettext import gettext as _

class openmsx(Runner):
    human_name = "openMSX"
    description = _("MSX computer emulator")
    platforms = ["MSX, MSX2, MSX2+, MSX turboR"]
    game_options = [
        {
            "option": "main_file",
            "type": "file",
            "label": _("ROM file"),
            'help': _("The game data, commonly called a ROM image.")
        }
    ]

    def play(self):
        rom = self.game_config.get('main_file') or ''
        if not os.path.exists(rom):
            return {'error': 'FILE_NOT_FOUND', 'file': rom}
        return {'command': [self.get_executable(), rom]}
