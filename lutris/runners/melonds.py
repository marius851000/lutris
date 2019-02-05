from lutris.runners.runner import Runner
from lutris.util import system
from gettext import gettext as _

class melonds(Runner):
    human_name = "melonDS"
    description = _("Nintendo DS Emulator")
    platforms = [_("Nintendo DS")]
    runner_executable = "melonDS/melonDS"
    game_options = [
        {
            "option": "main_file",
            "type": "file",
            "label": _("ROM file"),
            "default_path": "game_path",
        }
    ]

    def play(self):
        rom = self.game_config.get("main_file") or ""
        if not system.path_exists(rom):
            return {"error": "FILE_NOT_FOUND", "file": rom}
        return {"command": [self.get_executable(), rom]}
