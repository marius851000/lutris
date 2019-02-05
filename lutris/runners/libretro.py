import os
from lutris.runners.runner import Runner
from lutris.util.libretro import RetroConfig
from lutris.util import system
from lutris.util.log import logger
from lutris import settings
from gettext import gettext as _

# List of supported libretro cores
# First element is the human readable name for the core with the platform's short name
# Second element is the core identifier
# Third element is the platform's long name
LIBRETRO_CORES = [
    (_("4do (3DO)"), "4do", _("3DO")),
    (_("atari800 (Atari 800/5200)"), "atari800", _("Atari 800/5200")),
    (_("blueMSX (MSX/MSX2/MSX2+)"), "bluemsx", _("MSX/MSX2/MSX2+")),
    (_("Caprice32 (Amstrad CPC)"), "cap32", _("Amstrad CPC")),
    (_("ChaiLove"), "chailove", _("ChaiLove")),
    (_("Citra (Nintendo 3DS)"), "citra", _("Nintendo 3DS")),
    (_("Citra Canary (Nintendo 3DS)"), "citra_canary", _("Nintendo 3DS")),
    (_("CrocoDS (Amstrad CPC)"), "crocods", _("Amstrad CPC")),
    (_("Daphne (Arcade)"), "daphne", _("Arcade")),
    (_("DesmuME (Nintendo DS)"), "desmume", _("Nintendo DS")),
    (_("Dolphin (Nintendo Wii/Gamecube)"), "dolphin", _("Nintendo Wii/Gamecube")),
    (_("EightyOne (Sinclair ZX81)"), "81", _("Sinclair ZX81")),
    (_("FB Alpha (Arcade)"), "fbalpha", _("Arcade")),
    (_("FCEUmm (Nintendo Entertainment System)"), "fceumm", _("Nintendo NES")),
    (_("fMSX (MSX/MSX2/MSX2+)"), "fmsx", _("MSX/MSX2/MSX2+")),
    (_("FreeJ2ME (J2ME)"), "freej2me", _("J2ME")),
    (_("Fuse (ZX Spectrum)"), "fuse", _("Sinclair ZX Spectrum")),
    (_("Gambatte (Game Boy Color)"), "gambatte", _("Nintendo Game Boy Color")),
    (_("Gearboy (Game Boy Color)"), "gearboy", _("Nintendo Game Boy Color")),
    (
        _("Gearsystem (Sega Maste System/Gamegear)"),
        "gearsystem",
        _("Sega Maste System/Gamegear"),
    ),
    (_("Genesis Plus GX (Sega Genesis)"), "genesis_plus_gx", _("Sega Genesis")),
    (_("Handy (Atari Lynx)"), "handy", _("Atari Lynx")),
    (_("Hatari (Atari ST/STE/TT/Falcon)"), "hatari", _("Atari ST/STE/TT/Falcon")),
    (_("higan accuracy(Super Nintendo)"), "higan_sfc", _("Nintendo SNES")),
    (_("higan balanced(Super Nintendo)"), "higan_sfc_balanced", _("Nintendo SNES")),
    (_("Kronos (Sega Saturn)"), "kronos", _("Sega Saturn")),
    (_("MAME (Arcade)"), "mame", _("Arcade")),
    (_("Mednafen GBA (Game Boy Advance)"), "mednafen_gba", _("Nintendo Game Boy Advance")),
    (_("Mednafen NGP (SNK Neo Geo Pocket)"), "mednafen_ngp", _("SNK Neo Geo Pocket")),
    (
        _("Mednafen PCE FAST (TurboGrafx-16)"),
        "mednafen_pce_fast",
        _("NEC PC Engine (TurboGrafx-16)"),
    ),
    (_("Mednafen PCFX (NEC PC-FX)"), "mednafen_pcfx", _("NEC PC-FX")),
    (_("Mednafen Saturn (Sega Saturn)"), "mednafen_saturn", _("Sega Saturn")),
    (
        _("Mednafen SGX (NEC PC Engine SuperGrafx)"),
        "mednafen_supergrafx",
        _("NEC PC Engine (SuperGrafx)"),
    ),
    (_("Mednafen WSWAN (Bandai WonderSwan)"), "mednafen_wswan", _("Bandai WonderSwan")),
    (_("Mednafen PSX (Sony Playstation)"), "mednafen_psx", _("Sony PlayStation")),
    (_("Mednafen PSX OpenGL (Sony Playstation)"), "mednafen_psx_hw", _("Sony PlayStation")),
    (_("Mesen (Nintendo Entertainment System)"), "mesen", _("Nintendo NES")),
    (_("mGBA (Game Boy Advance)"), "mgba", _("Nintendo Game Boy Advance")),
    (_("Mupen64Plus (Nintendo 64)"), "mupen64plus", _("Nintendo N64")),
    (_("Nestopia (Nintendo Entertainment System)"), "nestopia", _("Nintendo NES")),
    (_("Neko Project 2 (NEC PC-98)"), "nekop2", _("NEC PC-98")),
    (_("Neko Project II kai (NEC PC-98)"), "np2kai", _("NEC PC-98")),
    (_("O2EM (Magnavox Odyssey²)"), "o2em", _("Magnavox Odyssey²")),
    (_("ParaLLEl N64 (Nintendo 64)"), "parallel_n64", _("Nintendo N64")),
    (_("PCSX Rearmed (Sony Playstation)"), "pcsx_rearmed", _("Sony PlayStation")),
    (_("PicoDrive (Sega Genesis)"), "picodrive", _("Sega Genesis")),
    (_("Portable SHARP X68000 Emulator (SHARP X68000)"), "px68k", _("Sharp X68000")),
    (_("PPSSPP (PlayStation Portable)"), "ppsspp", _("Sony PlayStation Portable")),
    (_("ProSystem (Atari 7800)"), "prosystem", _("Atari 7800")),
    (_("Redream (Sega Dreamcast)"), "redream", _("Sega Dreamcast")),
    (_("Reicast (Sega Dreamcast)"), "reicast", _("Sega Dreamcast")),
    (_("RPG Maker 2000/2003 (EasyRPG)"), "easyrpg", _("RPG Maker 2000/2003 Game Engine")),
    (_("Snes9x (Super Nintendo)"), "snes9x", _("Nintendo SNES")),
    (_("Snes9x2010 (Super Nintendo)"), "snes9x2010", _("Nintendo SNES")),
    (_("Stella (Atari 2600)"), "stella", _("Atari 2600")),
    (_("Uzem (Uzebox)"), "uzem", _("Uzebox")),
    (_("VecX (Vectrex)"), "vecx", _("Vectrex")),
    (_("Yabause (Sega Saturn)"), "yabause", _("Sega Saturn")),
    (_("VBA Next (Game Boy Advance)"), "vba_next", _("Nintendo Game Boy Advance")),
    (_("VBA-M (Game Boy Advance)"), "vbam", _("Nintendo Game Boy Advance")),
    (_("Virtual Jaguar (Atari Jaguar)"), "virtualjaguar", _("Atari Jaguar")),
    (_("VICE (Commodore 128)"), "vice_x128", _("Commodore 128")),
    (_("VICE (Commodore 16/Plus/4)"), "vice_xplus4", _("Commodore 16/Plus/4")),
    (_("VICE (Commodore 64)"), "vice_x64", _("Commodore 64")),
    (_("VICE (Commodore VIC-20)"), "vice_xvic", _("Commodore VIC-20")),
]


def get_core_choices():
    return [(core[0], core[1]) for core in LIBRETRO_CORES]


def get_default_config_path(path=""):
    return os.path.join(settings.RUNNER_DIR, "retroarch", path)


class libretro(Runner):
    human_name = "Libretro"
    description = "Multi system emulator"
    runnable_alone = True
    runner_executable = "retroarch/retroarch"

    game_options = [
        {"option": "main_file", "type": "file", "label": "ROM file"},
        {
            "option": "core",
            "type": "choice",
            "label": _("Core"),
            "choices": get_core_choices(),
        },
    ]

    runner_options = [
        {
            "option": "config_file",
            "type": "file",
            "label": _("Config file"),
            "default": get_default_config_path("retroarch.cfg"),
        },
        {
            "option": "fullscreen",
            "type": "bool",
            "label": _("Fullscreen"),
            "default": True,
        },
        {
            "option": "verbose",
            "type": "bool",
            "label": _("Verbose logging"),
            "default": False,
        },
    ]

    @property
    def platforms(self):
        return [core[2] for core in LIBRETRO_CORES]

    def get_platform(self):
        game_core = self.game_config.get("core")
        if game_core:
            for core in LIBRETRO_CORES:
                if core[1] == game_core:
                    return core[2]
        return ""

    def get_core_path(self, core):
        return os.path.join(
            settings.RUNNER_DIR, "retroarch", "cores", "{}_libretro.so".format(core)
        )

    def get_version(self, use_default=True):
        return self.game_config["core"]

    def is_retroarch_installed(self):
        return system.path_exists(self.get_executable())

    def is_installed(self, core=None):
        if self.game_config.get("core") and core is None:
            core = self.game_config["core"]
        if not core or self.runner_config.get("runner_executable"):
            return self.is_retroarch_installed()

        is_core_installed = system.path_exists(self.get_core_path(core))
        return self.is_retroarch_installed() and is_core_installed

    def install(self, version=None, downloader=None, callback=None):
        def install_core():
            if not version:
                if callback:
                    callback()
            else:
                super(libretro, self).install(version, downloader, callback)

        if not self.is_retroarch_installed():
            super(libretro, self).install(
                version=None, downloader=downloader, callback=install_core
            )
        else:
            super(libretro, self).install(version, downloader, callback)

    def get_run_data(self):
        return {
            "command": [self.get_executable()] + self.get_runner_parameters(),
            "env": self.get_env(),
        }

    def get_config_file(self):
        return self.runner_config.get("config_file") or get_default_config_path(
            "retroarch.cfg"
        )

    @staticmethod
    def get_system_directory(retro_config):
        """Return the system directory used for storing BIOS and firmwares."""
        system_directory = retro_config["system_directory"]
        if not system_directory or system_directory == "default":
            system_directory = get_default_config_path("system")
        return os.path.expanduser(system_directory)

    def prelaunch(self):
        config_file = self.get_config_file()

        # Create retroarch.cfg if it doesn't exist.
        if not system.path_exists(config_file):
            f = open(config_file, "w")
            f.write(_("# Lutris RetroArch Configuration"))
            f.close()

            # Build the default config settings.
            retro_config = RetroConfig(config_file)
            retro_config["libretro_directory"] = get_default_config_path("cores")
            retro_config["libretro_info_path"] = get_default_config_path("info")
            retro_config["content_database_path"] = get_default_config_path("database/rdb")
            retro_config["cheat_database_path"] = get_default_config_path("database/cht")
            retro_config["cursor_directory"] = get_default_config_path("database/cursors")
            retro_config["screenshot_directory"] = get_default_config_path("screenshots")
            retro_config["input_remapping_directory"] = get_default_config_path("remaps")
            retro_config["video_shader_dir"] = get_default_config_path("shaders")
            retro_config["core_assets_directory"] = get_default_config_path("downloads")
            retro_config["thumbnails_directory"] = get_default_config_path("thumbnails")
            retro_config["playlist_directory"] = get_default_config_path("playlists")
            retro_config["joypad_autoconfig_dir"] = get_default_config_path("autoconfig")
            retro_config["rgui_config_directory"] = get_default_config_path("config")
            retro_config["overlay_directory"] = get_default_config_path("overlay")
            retro_config["assets_directory"] = get_default_config_path("assets")
            retro_config.save()
        else:
            retro_config = RetroConfig(config_file)

        core = self.game_config.get("core")
        info_file = os.path.join(
            get_default_config_path("info"), "{}_libretro.info".format(core)
        )
        if system.path_exists(info_file):
            core_config = RetroConfig(info_file)
            try:
                firmware_count = int(core_config["firmware_count"])
            except (ValueError, TypeError):
                firmware_count = 0
            system_path = self.get_system_directory(retro_config)
            notes = core_config["notes"] or ""
            checksums = {}
            if notes.startswith("Suggested md5sums:"):
                parts = notes.split("|")
                for part in parts[1:]:
                    checksum, filename = part.split(" = ")
                    checksums[filename] = checksum
            for index in range(firmware_count):
                firmware_filename = core_config["firmware%d_path" % index]
                firmware_path = os.path.join(system_path, firmware_filename)
                if system.path_exists(firmware_path):
                    if firmware_filename in checksums:
                        checksum = system.get_md5_hash(firmware_path)
                        if checksum == checksums[firmware_filename]:
                            checksum_status = _("Checksum good")
                        else:
                            checksum_status = _("Checksum failed")
                    else:
                        checksum_status = _("No checksum info")
                    logger.info(
                        _("Firmware '%s' found (%s)"), firmware_filename, checksum_status
                    )
                else:
                    logger.warning(_("Firmware '%s' not found!"), firmware_filename)

                # Before closing issue #431
                # TODO check for firmware*_opt and display an error message if
                # firmware is missing
                # TODO Add dialog for copying the firmware in the correct
                # location

        return True

    def get_runner_parameters(self):
        parameters = []

        # Fullscreen
        fullscreen = self.runner_config.get("fullscreen")
        if fullscreen:
            parameters.append("--fullscreen")

        # Verbose
        verbose = self.runner_config.get("verbose")
        if verbose:
            parameters.append("--verbose")

        parameters.append("--config={}".format(self.get_config_file()))
        return parameters

    def play(self):
        command = [self.get_executable()]

        command += self.get_runner_parameters()

        # Core
        core = self.game_config.get("core")
        if not core:
            return {
                "error": "CUSTOM",
                "text": _("No core has been selected for this game"),
            }
        command.append("--libretro={}".format(self.get_core_path(core)))

        # Ensure the core is available
        if not self.is_installed(core):
            self.install(core)

        # Main file
        file = self.game_config.get("main_file")
        if not file:
            return {"error": "CUSTOM", "text": _("No game file specified")}
        if not system.path_exists(file):
            return {"error": "FILE_NOT_FOUND", "file": file}
        command.append(file)
        return {"command": command}

    # Checks whether the retroarch or libretro directories can be uninstalled.
    def can_uninstall(self):
        retroarch_path = os.path.join(settings.RUNNER_DIR, 'retroarch')
        return os.path.isdir(retroarch_path) or super(libretro, self).can_uninstall()

    # Remove the `retroarch` directory.
    def uninstall(self):
        retroarch_path = os.path.join(settings.RUNNER_DIR, 'retroarch')
        if os.path.isdir(retroarch_path):
            system.remove_folder(retroarch_path)
        super(libretro, self).uninstall()
