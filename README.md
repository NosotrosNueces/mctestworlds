mctestworlds
============

Test world generation for minecraft in addition to examples.

Terraformer
-----------

Included is a script that hopefully will be of use. `terraformer.py` creates
server commands for rectangular areas. It can also feed server commands into a
tmux session hosting a minecraft server. Example scripts are provided in
`examples/`, and can be run with `terraformer.send_script`. You can use the
command `tmux ls` to find out which session your Minecraft server is running
on.

Examples
--------

Scripts are simply Minecraft server commands, but with added comment support.
Lines beginning with a `#` symbol are considered comments and are not parsed.

* `arena.txt`: creates a creeper arena at (0,0) equiped with overflow limiting
* `mining.txt`: creates large areas near (0,0) to test mining with different
tools
