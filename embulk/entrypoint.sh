#!/bin/sh
 
# Install Embulk Plugins
if [ -n "$PLUGINS" ] ; then
  ~/.embulk/bin/embulk gem install $PLUGINS
fi

if [ ! -n "$CONFIG" ]; then
    echo "CONFIG variable is not defined!"
    exit 1   
fi

# Convert Embulk Config to generate seed.yml
python3 converter.py

~/.embulk/bin/embulk guess seed.yml
~/.embulk/bin/embulk run config.yml