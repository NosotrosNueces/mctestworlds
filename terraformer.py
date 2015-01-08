"""Maek arena."""
from subprocess import call


def get_square_params():
    y_ground = 56#int(input("y_ground: "))
    x = int(input("x: "))
    z = int(input("z: "))
    width = int(input("width: "))
    length = width
    height = 3#int(input("height: "))-1
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
        print(_)
    return commands


def get_rectanglular_prism(params):
    commands = ["/fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params)]
    for _ in commands:
        print(_)
    return commands


def get_arena(params):
    p_1 = params.copy()
    p_2 = params.copy()

    get_rectanglular_prism(p_1)

    p_2['material'] = 'air'

    p_2['x_1'] += 1
    p_2['x_2'] -= 1
    p_2['z_1'] += 1
    p_2['z_2'] -= 1
    get_rectanglular_prism(p_2)

    p_1['material'] = 'air'
    p_1['y_2'] = p_1['y_1']-2
    p_1['y_1'] -= 4
    get_rectanglular_prism(p_1)

    p_1['y_2'] = p_1['y_1']-2
    p_1['y_1'] -= 4
    get_rectanglular_prism(p_1)


def send_command(command, session):
    """Note: This function assumes that the server is started in pane 0."""
    call(["tmux", "send-keys", "-t" "{session}:0".format(session=session),
          command, "C-m"])
    # screen -p 0 -S $session_name -X eval "stuff \015\"$*\"\015"


def send_commands(commands, session):
    """Send a list of commands to the server."""
    for _ in commands:
        send_command(_, session)


if __name__ == "__main__":
    get_arena(get_square_params())
