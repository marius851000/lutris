import os

from lutris.runners.runner import Runner
from gettext import gettext as _

class ags(Runner):
    human_name = "Adventure Game Studio"
    description = _("Graphics adventure engine")
    platforms = ['Linux']
    runner_executable = 'ags/ags.sh'
    game_options = [{
        'option': 'main_file',
        'type': 'file',
        'label': _('Game executable or directory')
    }]
    runner_options = [
        {
            'option': 'fullscreen',
            'type': 'bool',
            'label': _('Fullscreen'),
            'default': True
        },
        {
            'option': 'filter',
            'type': 'choice',
            'label': _('Graphics filter'),
            'choices': [
                ('None', 'none'),
                ('Standard scaling', 'stdscale'),
                ('HQ2x', 'hq2x'),
                ('HQ3x', 'hq3x'),
            ]
        }
    ]

    def play(self):
        """Run the game."""

        main_file = self.game_config.get('main_file') or ''
        if not os.path.exists(main_file):
            return {'error': 'FILE_NOT_FOUND', 'file': main_file}

        arguments = [self.get_executable()]
        if self.runner_config.get('fullscreen', True):
            arguments.append('--fullscreen')
        else:
            arguments.append('--windowed')
        if self.runner_config.get('filter'):
            arguments.append('--gfxfilter')
            arguments.append(self.runner_config['filter'])

        arguments.append(main_file)
        return {"command": arguments}
