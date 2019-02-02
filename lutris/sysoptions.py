"""Options list for system config."""
import os
from collections import OrderedDict

from lutris import runners
from lutris.util import display, system
from gettext import gettext as _


def get_optirun_choices():
    """Return menu choices (label, value) for Optimus"""
    choices = [("Off", "off")]
    if system.find_executable("primusrun"):
        choices.append(("primusrun", "primusrun"))
    if system.find_executable("optirun"):
        choices.append(("optirun/virtualgl", "optirun"))
    return choices


system_options = [  # pylint: disable=invalid-name
    {
        "option": "game_path",
        "type": "directory_chooser",
        "label": _("Default installation folder"),
        "default": os.path.expanduser("~/Games"),
        "scope": ["runner", "system"],
        "help": _("The default folder where you install your games."))
    },
    {
        "option": "disable_runtime",
        "type": "bool",
        "label": _("Disable Lutris Runtime"),
        "default": False,
        "help": (
            _("The Lutris Runtime loads some libraries before running the "
            "game. Which can cause some incompatibilities in some cases. "
            "Check this option to disable it.")
        ),
    },
    {
        "option": "prefer_system_libs",
        "type": "bool",
        "label": _("Prefer system libraries"),
        "default": False,
        "help": (
            _("When the runtime is enabled, prioritize the system libraries"
            " over the provided ones.")
        ),
    },
    {
        "option": "reset_desktop",
        "type": "bool",
        "label": _("Restore resolution on game exit"),
        "default": False,
        "help": (
            _("Some games don't restore your screen resolution when \n"
            "closed or when they crash. This is when this option comes \n"
            "into play to save your bacon.")
        ),
    },
    {
        "option": "single_cpu",
        "type": "bool",
        "label": _("Restrict to single core"),
        "advanced": True,
        "default": False,
        "help": _("Restrict the game to a single CPU core."),
    },
    {
        "option": "restore_gamma",
        "type": "bool",
        "default": False,
        "label": _("Restore gamma on game exit"),
        "advanced": True,
        "help": (
            _("Some games don't correctly restores gamma on exit, making "
            "your display too bright. Select this option to correct it.")
        ),
    },
    {
        "option": "disable_compositor",
        "label": _("Disable desktop effects"),
        "type": "bool",
        "default": False,
        "advanced": True,
        "help": (
            _("Disable desktop effects while game is running, "
            "reducing stuttering and increasing performance")
        ),
    },
    {
        "option": "reset_pulse",
        "type": "bool",
        "label": _("Reset PulseAudio"),
        "default": False,
        "advanced": True,
        "condition": system.find_executable("pulseaudio"),
        "help": _("Restart PulseAudio before launching the game."),
    },
    {
        "option": "pulse_latency",
        "type": "bool",
        "label": _("Reduce PulseAudio latency"),
        "default": False,
        "advanced": True,
        "condition": system.find_executable("pulseaudio"),
        "help": (
            _("Set the environment variable PULSE_LATENCY_MSEC=60 "
            "to improve audio quality on some games")
        ),
    },
    {
        "option": "use_us_layout",
        "type": "bool",
        "label": _("Switch to US keyboard layout"),
        "default": False,
        "advanced": True,
        "help": _("Switch to US keyboard qwerty layout while game is running"),
    },
    {
        "option": "optimus",
        "type": "choice",
        "default": "off",
        "choices": get_optirun_choices,
        "label": _("Optimus launcher (NVIDIA Optimus laptops)",)
        "advanced": True,
        "help": (
            _("If you have installed the primus or bumblebee packages, "
            "select what launcher will run the game with the command, "
            "activating your NVIDIA graphic chip for high 3D "
            "performance. primusrun normally has better performance, but"
            "optirun/virtualgl works better for more games.")
        ),
    },
    {
        "option": "fps_limit",
        "type": "string",
        "size": "small",
        "label": _("Fps limit"),
        "advanced": True,
        "condition": bool(system.find_executable("strangle")),
        "help": _("Limit the game's fps to desired number"),
    },
    {
        "option": "gamemode",
        "type": "bool",
        "default": system.LINUX_SYSTEM.is_feature_supported("GAMEMODE"),
        "condition": system.LINUX_SYSTEM.is_feature_supported("GAMEMODE"),
        "label": _("Enable Feral gamemode"),
        "help": _("Request a set of optimisations be temporarily applied to the host OS"),
    },
    {
        "option": "dri_prime",
        "type": "bool",
        "default": False,
        "condition": display.USE_DRI_PRIME,
        "label": _("Use PRIME (hybrid graphics on laptops)"),
        "advanced": True,
        "help": (
            _("If you have open source graphic drivers (Mesa), selecting this "
            "option will run the game with the 'DRI_PRIME=1' environment variable, "
            "activating your discrete graphic chip for high 3D "
            "performance.")
        ),
    },
    {
        "option": "sdl_video_fullscreen",
        "type": "choice",
        "label": _("SDL 1.2 Fullscreen Monitor"),
        "choices": display.get_output_list,
        "default": "off",
        "advanced": True,
        "help": (
            _("Hint SDL 1.2 games to use a specific monitor when going "
            "fullscreen by setting the SDL_VIDEO_FULLSCREEN "
            "environment variable")
        ),
    },
    {
        "option": "display",
        "type": "choice",
        "label": _("Turn off monitors except"),
        "choices": display.get_output_choices,
        "default": "off",
        "advanced": True,
        "help": (
            _("Only keep the selected screen active while the game is "
            "running. \n"
            "This is useful if you have a dual-screen setup, and are \n"
            "having display issues when running a game in fullscreen.")
        ),
    },
    {
        "option": "resolution",
        "type": "choice",
        "label": _("Switch resolution to"),
        "choices": display.get_resolution_choices,
        "default": "off",
        "help": _("Switch to this screen resolution while the game is running."),
    },
    {
        "option": "terminal",
        "label": _("Run in a terminal"),
        "type": "bool",
        "default": False,
        "advanced": True,
        "help": _("Run the game in a new terminal window."),
    },
    {
        "option": "terminal_app",
        "label": _("Terminal application"),
        "type": "choice_with_entry",
        "choices": system.get_terminal_apps,
        "default": system.get_default_terminal(),
        "advanced": True,
        "help": (
            _("The terminal emulator to be run with the previous option."
            "Choose from the list of detected terminal apps or enter "
            "the terminal's command or path."
            "Note: Not all terminal emulators are guaranteed to work.")
        ),
    },
    {
        "option": "env",
        "type": "mapping",
        "label": _("Environment variables"),
        "help": _("Environment variables loaded at run time"),
    },
    {
        "option": "prefix_command",
        "type": "string",
        "label": _("Command prefix"),
        "advanced": True,
        "help": (
            _("Command line instructions to add in front of the game's "
            "execution command.")
        ),
    },
    {
        "option": "manual_command",
        "type": "file",
        "label": _("Manual command"),
        "advanced": True,
        "help": _("Script to execute from the game's contextual menu"),
    },
    {
        "option": "prelaunch_command",
        "type": "file",
        "label": _("Pre-launch command"),
        "advanced": True,
        "help": _("Script to execute before the game starts"),
    },
    {
        "option": "prelaunch_wait",
        "type": "bool",
        "label": _("Wait for pre-launch command completion"),
        "advanced": True,
        "default": False,
        "help": _("Run the game only once the pre-launch command has exited"),
    },
    {
        "option": "postexit_command",
        "type": "file",
        "label": _("Post-exit command"),
        "advanced": True,
        "help": _("Script to execute when the game exits"),
    },
    {
        "option": "include_processes",
        "type": "string",
        "label": _("Include processes"),
        "advanced": True,
        "help": (
            _("What processes to include in process monitoring. "
            "This is to override the built-in exclude list.\n"
            "Space-separated list, processes including spaces "
            "can be wrapped in quotation marks.")
        ),
    },
    {
        "option": "exclude_processes",
        "type": "string",
        "label": _("Exclude processes"),
        "advanced": True,
        "help": (
            _("What processes to exclude in process monitoring. "
            "For example background processes that stick around "
            "after the game has been closed.\n"
            "Space-separated list, processes including spaces "
            "can be wrapped in quotation marks.")
        ),
    },
    {
        "option": "killswitch",
        "type": "string",
        "label": _("Killswitch file"),
        "advanced": True,
        "help": (
            _("Path to a file which will stop the game when deleted \n"
            "(usually /dev/input/js0 to stop the game on joystick "
            "unplugging)")
        ),
    },
    {
        "option": "xboxdrv",
        "type": "string",
        "label": _("xboxdrv config"),
        "advanced": True,
        "condition": system.find_executable("xboxdrv"),
        "help": (
            _("Command line options for xboxdrv, a driver for XBOX 360 "
            "controllers. Requires the xboxdrv package installed.")
        ),
    },
    {
        "option": "sdl_gamecontrollerconfig",
        "type": "string",
        "label": _("SDL2 gamepad mapping"),
        "advanced": True,
        "help": (
            _("SDL_GAMECONTROLLERCONFIG mapping string or path to a custom "
            "gamecontrollerdb.txt file containing mappings.")
        ),
    },
    {
        "option": "xephyr",
        "label": _("Use Xephyr"),
        "type": "choice",
        "choices": (
            ("Off", "off"),
            ("8BPP (256 colors)", "8bpp"),
            ("16BPP (65536 colors)", "16bpp"),
            ("24BPP (16M colors)", "24bpp"),
        ),
        "default": "off",
        "advanced": True,
        "help": _("Run program in Xephyr to support 8BPP and 16BPP color modes"),
    },
    {
        "option": "xephyr_resolution",
        "type": "string",
        "label": _("Xephyr resolution"),
        "advanced": True,
        "help": _("Screen resolution of the Xephyr server"),
    },
    {
        "option": "xephyr_fullscreen",
        "type": "bool",
        "label": _("Xephyr Fullscreen"),
        "default": True,
        "advanced": True,
        "help": _("Open Xephyr in fullscreen (at the desktop resolution)"),
    },
]


def with_runner_overrides(runner_slug):
    """Return system options updated with overrides from given runner."""
    options = system_options
    try:
        runner = runners.import_runner(runner_slug)
    except runners.InvalidRunner:
        return options
    if not getattr(runner, "system_options_override"):
        runner = runner()
    if runner.system_options_override:
        opts_dict = OrderedDict((opt["option"], opt) for opt in options)
        for option in runner.system_options_override:
            key = option["option"]
            if opts_dict.get(key):
                opts_dict[key] = opts_dict[key].copy()
                opts_dict[key].update(option)
            else:
                opts_dict[key] = option
        options = [opt for opt in list(opts_dict.values())]
    return options
