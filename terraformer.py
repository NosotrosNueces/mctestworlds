"""Maek arena."""

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
    print("/fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params))
    print("/fill {x_1} {y_1} {z_1} {x_1} {y_2} {z_2} minecraft:{material}".format(**params))
    print("/fill {x_2} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params))
    print("/fill {x_1} {y_1} {z_2} {x_2} {y_2} {z_2} minecraft:{material}".format(**params))
    print("")

def get_rectanglular_prism(params):
    print("/fill {x_1} {y_1} {z_1} {x_2} {y_2} {z_2} minecraft:{material}".format(**params))
    print("")

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

if __name__ == "__main__":
    get_arena(get_square_params())
