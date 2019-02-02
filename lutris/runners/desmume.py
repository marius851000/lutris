from lutris.runners.runner import Runner
from lutris.util import system
from gettext import gettext as _

class desmume(Runner):
    human_name = "DeSmuME"
    platforms = ["Nintendo DS"]
    description = _("Nintendo DS emulator")
    runner_executable = "desmume/bin/desmume"
    game_options = [
        {
            "option": "main_file",
            "type": "file",
            "label": _("ROM file"),
            "help": _("The game data, commonly called a ROM image."),
        }
    ]

    def play(self):
        """Run the game."""
        arguments = [self.get_executable()]
        rom = self.game_config.get("main_file") or ""
        if not system.path_exists(rom):
            return {"error": "FILE_NOT_FOUND", "file": rom}
        arguments.append(rom)
        return {"command": arguments}
