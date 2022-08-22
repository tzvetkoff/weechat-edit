# weechat-edit

A weechat plugin that allows you to use `$EDITOR` to compose a [longer] message.

## Usage

``` sh
# Basic
/edit

# Edit your previous message
/edit --previous

# Add a key binding so you can edit your current input
/key bind meta-E /edit

# Tip: If your editor exits with code different than 0, current input won't be changed.
```

## Configuration

``` sh
/set plugins.var.python.edit.editor "vim -f"
```

## Installation

Just like any normal weechat plugin, copy it to `~/.weechat/python` and symlink it in `~/.weechat/python/autoload`.
