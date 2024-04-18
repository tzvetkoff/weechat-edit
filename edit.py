# Open $EDITOR to compose a message.
#
# Usage:
#   /edit
#   /edit --previous
#
# Settings:
# /set plugins.var.python.edit.editor 'vim -f'

import os
import os.path
import shlex
import subprocess
import weechat

def cmd_edit(_cb_data, buf, args):
    prev = args in ('-p', '--prev', '--previous', 'prev', 'previous', '-l', '--last', 'last', '-o', '--old', 'old')
    editor = weechat.config_get_plugin('editor') or os.environ.get('EDITOR', 'vim -f')

    path = os.path.join(os.path.expanduser(os.environ.get('WEECHAT_HOME', '~/.weechat/')), 'message.txt')

    if not prev:
        with open(path, 'w+') as f:
            f.write(weechat.buffer_get_string(buf, 'input'))

    code = subprocess.Popen(shlex.split(editor) + [path]).wait()
    if code == 0:
        with open(path) as f:
            data = f.read().strip()

        weechat.buffer_set(buf, 'input', data)
        weechat.buffer_set(buf, 'input_pos', str(len(data)))

    weechat.command(buf, "/window refresh")

    return weechat.WEECHAT_RC_OK


def main():
    if not weechat.register(
        'edit',                                 # Plugin name
        'Latchezar Tzvetkoff',                  # Author
        '1.0.0',                                # Version
        'MIT',                                  # License
        'Open $EDITOR to compose a message',    # Description
        '',                                     # Shutdown callback
        '',                                     # Character set
    ):
        return weechat.WEECHAT_RC_ERROR

    weechat.hook_command(
        'edit',                                 # Command
        'Open $EDITOR to compose a message',    # Command description
        '[--previous]',                         # Arguments
        '--previous: edit last message',        # Arguments description
        '--previous',                           # Completion template
        'cmd_edit',                             # Callback
        '',                                     # Callback data
    )


if __name__ == '__main__':
    main()
