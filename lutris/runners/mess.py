import os
from lutris import settings
from lutris.util.log import logger
from lutris.runners.runner import Runner
from lutris.util import system
from gettext import gettext as _


class mess(Runner):
    human_name = "MESS"
    description = _("Multi-system (consoles and computers) emulator")
    # TODO: A lot of platforms/machines are missing
    platforms = (
        _("Acorn Atom"),
        _("Adventure Vision"),
        _("Amstrad CPC 464"),
        _("Amstrad CPC 6128"),
        _("Amstrad GX4000"),
        _("Apple I"),
        _("Apple II"),
        _("Apple IIGS"),
        _("Arcadia 2001"),
        _("Bally Professional Arcade"),
        _("BBC Micro"),
        _("Casio PV-1000"),
        _("Casio PV-2000"),
        _("Chintendo Vii"),
        _("Coleco Adam"),
        _("Commodore 64"),
        _("Creatronic Mega Duck"),
        _("DEC PDP-1"),
        _("Epoch Game Pocket Computer"),
        _("Epoch Super Cassette Vision"),
        _("Fairchild Channel F"),
        _("Fujitsu FM 7"),
        _("Fujitsu FM Towns"),
        _("Funtech Super ACan"),
        _("Game.com"),
        _("Hartung Game Master"),
        _("IBM PCjr"),
        _("Intellivision"),
        _("Interton VC 4000"),
        _("Matra Alice"),
        _("Mattel Aquarius"),
        _("Memotech MTX"),
        _("Milton Bradley MicroVision"),
        _("NEC PC-8801"),
        _("NEC PC-88VA"),
        _("RCA Studio II"),
        _("Sam Coupe"),
        _("SEGA Computer 3000"),
        _("Sega Pico"),
        _("Sega SG-1000"),
        _("Sharp MZ-2500"),
        _("Sharp MZ-700"),
        _("Sharp X1"),
        _("Sinclair ZX Spectrum"),
        _("Sinclair ZX Spectrum 128"),
        _("Sony SMC777"),
        _("Spectravision SVI-318"),
        _("Tatung Einstein"),
        _("Thomson MO5"),
        _("Thomson MO6"),
        _("Tomy Tutor"),
        _("TRS-80 Color Computer"),
        _("Videopac Plus G7400"),
        _("VTech CreatiVision"),
        _("Watara Supervision"),
    )
    machine_choices = [
        (_("Acorn Atom"), "atom"),
        (_("Adventure Vision"), "advision"),
        (_("Amstrad CPC 464"), "cpc464"),
        (_("Amstrad CPC 6128"), "cpc6128"),
        (_("Amstrad GX4000"), "gx4000"),
        (_("Apple I"), "apple1"),
        (_("Apple II"), "apple2ee"),
        (_("Apple IIGS"), "apple2gs"),
        (_("Arcadia 2001"), "arcadia"),
        (_("Bally Professional Arcade"), "astrocde"),
        (_("BBC Micro"), "bbcb"),
        (_("Casio PV-1000"), "pv1000"),
        (_("Casio PV-2000"), "pv2000"),
        (_("Chintendo Vii"), "vii"),
        (_("Coleco Adam"), "adam"),
        (_("Commodore 64"), "c64"),
        (_("Creatronic Mega Duck"), "megaduck"),
        (_("DEC PDP-1"), "pdp1"),
        (_("Epoch Game Pocket Computer"), "gamepock"),
        (_("Epoch Super Cassette Vision"), "scv"),
        (_("Fairchild Channel F"), "channelf"),
        (_("Fujitsu FM 7"), "fm7"),
        (_("Fujitsu FM Towns"), "fmtowns"),
        (_("Funtech Super A'Can"), "supracan"),
        (_("Game.com"), "gamecom"),
        (_("Hartung Game Master"), "gmaster"),
        (_("IBM PCjr"), "ibmpcjr"),
        (_("Intellivision"), "intv"),
        (_("Interton VC 4000"), "vc4000"),
        (_("Matra Alice"), "alice90"),
        (_("Mattel Aquarius"), "aquarius"),
        (_("Memotech MTX"), "mtx"),
        (_("Milton Bradley MicroVision"), "microvision"),
        (_("NEC PC-8801"), "pc8801"),
        (_("NEC PC-88VA"), "pc88va"),
        (_("RCA Studio II"), "studio2"),
        (_("Sam Coupe"), "samcoupe"),
        (_("SEGA Computer 3000"), "sc3000"),
        (_("Sega Pico"), "pico"),
        (_("Sega SG-1000"), "sg1000"),
        (_("Sharp MZ-2500"), "mz2500"),
        (_("Sharp MZ-700"), "mz700"),
        (_("Sharp X1"), "x1"),
        (_("ZX Spectrum"), "spectrum"),
        (_("ZX Spectrum 128"), "spec128"),
        (_("Sony SMC777"), "smc777"),
        (_("Spectravision SVI-318"), "svi318"),
        (_("Tatung Einstein"), "einstein"),
        (_("Thomson MO5"), "mo5"),
        (_("Thomson MO6"), "mo6"),
        (_("Tomy Tutor"), "tutor"),
        (_("TRS-80 Color Computer"), "coco"),
        (_("Videopac Plus G7400"), "g7400"),
        (_("VTech CreatiVision"), "crvision"),
        (_("Watara Supervision"), "svision"),
    ]
    runner_executable = "mess/mess"
    game_options = [
        {
            "option": "main_file",
            "type": "file",
            "label": _("ROM file"),
            "help": _("The game data, commonly called a ROM image."),
        },
        {
            "option": "machine",
            "type": "choice_with_entry",
            "label": _("Machine"),
            "choices": machine_choices,
            "help": _("The emulated machine."),
        },
        {
            "option": "device",
            "type": "choice_with_entry",
            "label": _("Storage type"),
            "choices": [
                (_("Floppy disk"), "flop"),
                (_("Floppy drive 1"), "flop1"),
                (_("Floppy drive 2"), "flop2"),
                (_("Floppy drive 3"), "flop3"),
                (_("Floppy drive 4"), "flop4"),
                (_("Cassette (tape)"), "cass"),
                (_("Cassette 1 (tape)"), "cass1"),
                (_("Cassette 2 (tape)"), "cass2"),
                (_("Cartridge"), "cart"),
                (_("Cartridge 1"), "cart1"),
                (_("Cartridge 2"), "cart2"),
                (_("Cartridge 3"), "cart3"),
                (_("Cartridge 4"), "cart4"),
                (_("Snapshot"), "snapshot"),
                (_("Hard Disk"), "hard"),
                (_("Hard Disk 1"), "hard1"),
                (_("Hard Disk 2"), "hard2"),
                (_("CDROM"), "cdrm"),
                (_("CDROM 1"), "cdrm1"),
                (_("CDROM 2"), "cdrm2"),
                (_("Snapshot"), "dump"),
                (_("Quickload"), "quickload"),
                (_("Memory Card"), "memc"),
                (_("Cylinder"), "cyln"),
                (_("Punch Tape 1"), "ptap1"),
                (_("Punch Tape 2"), "ptap2"),
                (_("Print Out"), "prin"),
                (_("Print Out"), "prin"),
            ],
        },
    ]
    runner_options = [
        {
            "option": "rompath",
            "type": "directory_chooser",
            "label": _("BIOS path"),
            "help": _(
                "Choose the folder containing MESS bios files.\n"
                "These files contain code from the original hardware "
                "necessary to the emulation."
            ),
        },
        {
            "option": "uimodekey",
            "type": "choice_with_entry",
            "label": _("Menu mode key"),
            "choices": [
                (_("Scroll Lock"), "SCRLOCK"),
                (_("Num Lock"), "NUMLOCK"),
                (_("Caps Lock"), "CAPSLOCK"),
                (_("Menu"), "MENU"),
                (_("Right Control"), "RCONTROL"),
                (_("Left Control"), "LCONTROL"),
                (_("Right Alt"), "RALT"),
                (_("Left Alt"), "LALT"),
                (_("Right Super"), "RWIN"),
                (_("Left Super"), "LWIN"),
            ],
            "help": _(
                "Key to switch between Full Keyboard Mode and "
                "Partial Keyboard Mode (default: Scroll Lock)"
            )
        },
    ]

    def get_platform(self):
        machine = self.game_config.get("machine")
        if machine:
            for index, machine_choice in enumerate(self.machine_choices):
                if machine_choice[1] == machine:
                    return self.platforms[index]
        return ""

    @property
    def working_dir(self):
        return os.path.join(os.path.expanduser("~"), ".mame")

    def play(self):
        rompath = self.runner_config.get("rompath") or ""
        if not system.path_exists(rompath):
            logger.warning(_("BIOS path provided in %s doesn't exist"), rompath)
            rompath = os.path.join(settings.RUNNER_DIR, "mess/bios")
        if not system.path_exists(rompath):
            logger.error(_("Couldn't find %s"), rompath)
            return {"error": "NO_BIOS"}
        machine = self.game_config.get("machine")
        if not machine:
            return {"error": "INCOMPLETE_CONFIG"}
        rom = self.game_config.get("main_file") or ""
        if rom and not system.path_exists(rom):
            return {"error": "FILE_NOT_FOUND", "file": rom}
        device = self.game_config.get("device")
        command = [self.get_executable()]
        if self.runner_config.get("uimodekey"):
            command += ["-uimodekey", self.runner["uimodekey"]]

        command += ["-rompath", rompath, machine]
        if device:
            command.append("-" + device)
        if rom:
            command.append(rom)
        return {"command": command}
