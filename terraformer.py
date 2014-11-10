"""Maek arena."""

def get_square_params():
    y_ground = 56#int(input("y_ground: "))
    x = int(input("x: "))
    z = int(input("z: "))
    width = int(input("width: "))
    length = width
    height = 3#int(input("height: "))-1
    material = input("material (no minecraft: prefix): ")
    return {'x': x, 'z': z, 'y_min': y_ground,
            'x_2': x+length, 'y_max': y_ground+height, 'z_2': z+width,
            'material': material}

def get_rectanglular_perimeter(params):
    print("/fill {x} {y_min} {z} {x_2} {y_max} {z} minecraft:{material}".format(**params))
    print("/fill {x} {y_min} {z} {x} {y_max} {z_2} minecraft:{material}".format(**params))
    print("/fill {x_2} {y_min} {z} {x_2} {y_max} {z_2} minecraft:{material}".format(**params))
    print("/fill {x} {y_min} {z_2} {x_2} {y_max} {z_2} minecraft:{material}".format(**params))
    print("")

def get_rectanglular_prism(params):
    print("/fill {x} {y_min} {z} {x_2} {y_max} {z_2} minecraft:{material}".format(**params))
    print("")

def get_arena(params):
    p = params.copy()
    p_2 = params.copy()

    get_rectanglular_prism(p)

    p_2['material'] = 'air'
    p_2['x'] += 1
    p_2['x_2'] -= 1
    p_2['z'] += 1
    p_2['z_2'] -= 1
    get_rectanglular_prism(p_2)

    #get_rectanglular_perimeter(p)
    p['y_max'] = p['y_min']-2
    p['y_min'] -= 4
    p['material'] = 'air'
    get_rectanglular_prism(p)

    p['y_max'] = p['y_min']-2
    p['y_min'] -= 4
    p['material'] = 'air'
    get_rectanglular_prism(p)

if __name__ == "__main__":
    get_arena(get_square_params())
