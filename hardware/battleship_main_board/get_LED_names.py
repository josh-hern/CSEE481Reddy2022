import pcbnew

class SwitchDiodePair:

    def __init__(
        self,
        identifier_number,
        diode_relative_x,
        diode_relative_y
    ):
        board = pcbnew.GetBoard()
        self.switch = board.FindFootprintByReference(f'SW{identifier_number}')
        self.diode = board.FindFootprintByReference(f'D{identifier_number}')
        self.d_rel_x = diode_relative_x
        self.d_rel_y = diode_relative_y

    def position_footprints(self, x, y):
        self.switch.SetPosition(pcbnew.wxPointMM(x, y))
        self.diode.SetPosition(pcbnew.wxPointMM(x + self.d_rel_x, y + self.d_rel_y))



def position_leds(footprints, coords):
    for foot_coord in zip(footprints, coords):
        footprint, coord = foot_coord
        x, y = coord
        footprint.SetPosition(pcbnew.wxPointMM(x, y))
    pcbnew.Refresh()

def get_led_footprints():

    board = pcbnew.GetBoard()

    first_LED_number = 1
    last_LED_number = 100

    LEDs = [f'LED{num}' for num in range(first_LED_number, last_LED_number + 1)]

    footprints = [board.FindFootprintByReference(footprint) for footprint in LEDs]

    return footprints

def get_led_positions(LED_spacing_mm=15):

    origin_x = 100
    origin_y = -300

    LED_coords = []

    for y in range(0, 10):
        for x in range(0, 10):
            LED_coords.append((x*LED_spacing_mm + origin_x, y*LED_spacing_mm + origin_y))

    return LED_coords


def get_switch_footprints():
    board = pcbnew.GetBoard()

    first_switch = 1
    last_switch = 100
    
    switches = [f'SW{num}' for num in range(first_switch, last_switch + 1)]

    footprints = [board.FindFootprintByReference(footprint) for footprint in switches]

    return footprints

def get_grid_positions(spacing=15):

    origin_x = 100
    origin_y = -100

    switches = []

    for y in range(0, 10):
        for x in range(0, 10):
            switches.append((x*spacing + origin_x, y*spacing + origin_y))

    return switches

def position_footprints(footprints, coords):
    for foot_coord in zip(footprints, coords):
        footprint, coord = foot_coord
        x, y = coord
        footprint.position_footprints(x, y)
    pcbnew.Refresh()

def position_switches(spacing):
    position_footprints(get_switch_footprints(), get_switch_positions(spacing))

def get_diode_switch_pairs(rel_x, rel_y):
    first = 1
    last = 100
    pairs = [SwitchDiodePair(identifier, rel_x, rel_y) for identifier in range(first, last + 1)]

    return pairs

def position_diode_pairs(spacing=20, rel_x=0, rel_y=0):
    positions = get_grid_positions(spacing)
    pairs = get_diode_switch_pairs(rel_x, rel_y)

    for pair, coord in zip(pairs, positions):
        x, y = coord
        pair.position_footprints(x, y)
    pcbnew.Refresh()
    
    

