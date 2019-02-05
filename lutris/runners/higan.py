from os.path import expanduser
from lutris.runners.runner import Runner
from gettext import gettext as _

class higan(Runner):
    human_name = "higan"
    description = _("Multi-system emulator including NES, GB(A), PC Engine " "support.")
    platforms = [
        _("Nintendo Game Boy (Color)"),
        _("Nintendo Game Boy Advance"),
        _("Sega Game Gear"),
        _("Sega Genesis/Mega Drive"),
        _("Sega Master System"),
        _("Nintendo NES"),
        _("NEC PC Engine TurboGrafx-16"),
        _("NEC PC Engine SuperGrafx"),
        _("Nintendo SNES"),
        _("Bandai WonderSwan"),
    ]
    runner_executable = "higan/bin/higan"
    game_options = [
        {
            "option": "main_dir",
            "type": "directory_chooser",
            "label": _("ROM directory"),
            "help": _(
                "The game data directory. \n"
                'higan uses its own "Game Pak" system. Gamepaks are '
                "an attempt to simulate physical Nintendo Game Paks in digital form. "
                "The idea is that for each game, one folder acts as a gamepak, "
                "and contains all data that is specific to said game."
            ),
        },
        {
            "option": "subgame1",
            "type": "directory_chooser",
            "label": _("Secondary ROM directory"),
            "advanced": True,
            "help": _(
                "The game data directory for the secondary cart slot"
                "on either the Sufami Turbo, Satellaview or Super Game Boy."
            ),
        },
        {
            "option": "subgame2",
            "type": "directory_chooser",
            "label": _("Tertiary ROM directory"),
            "advanced": True,
            "help": _("The game data directory for the tertiary cart slot on the Sufami Turbo."),
        },
    ]
    runner_options = [
        {
            "option": "fs",
            "type": "bool",
            "label": _("Fullscreen"),
            "default": False
        },
        {
            "option": "region",
            "type": "choice",
            "label": _("Region"),
            "choices": [
                (_("Auto"), "auto"),
                (_("NTSC-U"), "NTSC-U"),
                (_("PAL"), "PAL"),
                (_("NTSC-J"), "NTSC-J"),
            ],
            "default": "auto",
            "help": _("The region of the console."),
        },
    ]

    def play(self):

        rom = self.game_config.get("main_dir") or ""
        fullscreen = self.runner_config.get("fs") or False
        region = self.runner_config.get("region") or "auto"
        subgame1 = self.game_config.get("subgame1") or ""
        subgame2 = self.game_config.get("subgame2") or ""

        command = [self.get_executable()]

        if fullscreen:
            command.append("--fullscreen")

        if region != "auto":
            command.append(region + "|" + expanduser(rom))
        else:
            command.append(expanduser(rom))

        if subgame1:
            command.append(expanduser(subgame1))
            if subgame2:
                command.append(expanduser(subgame2))

        launch_info = {"command": command}

        return launch_info
