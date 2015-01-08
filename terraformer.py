"""Maek arena."""
from subprocess import call
from time import sleep


GROUND_LEVEL = 56


def read_config(filename="SETTINGS.txt"):
    pass


def get_square_params():
    y_ground = 56#int(input("y_ground: "))
    x = int(input("x: "))
    z = int(input("z: "))
    width = int(input("width: "))
    length = width
    height = 4#int(input("height: "))-1
    material = input("material (no minecraft: prefix): ")
    return {'x_1': x, 'z_1': z, 'y_1': y_ground,
            'x_2': x+length, 'z_2': z+width, 'y_2': y_ground+height,
            'material': material}


def get_rectanglular_perimeter(params):
    commands = ["/fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params),
                "/fill {x_1} {y_1} {z_1} {x_1} {y_2} {z_2} minecraft:{material}".format(**params),
                "/fill {x_2} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params),
                "/fill {x_1} {y_1} {z_2} {x_2} {y_2} {z_2} minecraft:{material}".format(**params)]
    for _ in commands:
        print(_, end="\n\n")
    return commands


def get_rectanglular_prism(params):
    commands = ["/fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params)]
    for _ in commands:
        print(_, end="\n\n")
    return commands


def get_arena(params):
    p_1 = params.copy()
    p_2 = params.copy()
    p_3 = params.copy()

    # Walls
    commands = get_rectanglular_prism(p_1)

    # Floor
    p_3['y_2'] = p_3['y_1'] = p_3['y_1'] - 1
    commands += get_rectanglular_prism(p_3)
    p_3['y_2'] = p_3['y_1'] = p_3['y_1'] - 4
    commands += get_rectanglular_prism(p_3)

    p_2['material'] = 'air'

    # Arena
    p_2['x_1'] += 1
    p_2['x_2'] -= 1
    p_2['z_1'] += 1
    p_2['z_2'] -= 1
    commands += get_rectanglular_prism(p_2)

    # Room
    p_1['material'] = 'air'
    p_1['y_2'] = p_1['y_1'] - 2
    p_1['y_1'] -= 4
    commands += get_rectanglular_prism(p_1)

    # Room
    p_1['y_2'] = p_1['y_1'] - 2
    p_1['y_1'] -= 4
    commands += get_rectanglular_prism(p_1)

    return commands


def send_command(command, session, pane=0):
    call(["tmux", "send-keys", "-t" "{session}:{pane}".format(session=session, pane=pane),
          command, "C-m"])
    # screen -p 0 -S $session_name -X eval "stuff \015\"$*\"\015"


def send_commands(commands, session, pane=0):
    """Send a list of commands to the server."""
    for _ in commands:
        send_command(_, session, pane)
        sleep(0.1)


def send_file(filename, session, pane=0):
    """Send a file of server commands to the tmux session."""
    send_commands(open(filename, 'r').read().split('\n'), session, pane)


if __name__ == "__main__":
    get_arena(get_square_params())
