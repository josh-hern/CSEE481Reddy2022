import pcbnew

def position_leds(footprints, coords):
    board = pcbnew.GetBoard()
    for foot_coord in zip(footprints, LED_coords):
        footprint, coord = foot_coord
        x, y = coord
        footprint.SetPosition(pcbnew.wxPointMM(x, y))
    pcbnew.Refresh()

def get_footprints():

    board = pcbnew.GetBoard()

    first_LED_number = 92
    last_LED_number = 191

    LEDs = [f'D{num}' for num in range(first_LED_number, last_LED_number + 1)]

    footprints = [board.FindFootprintByReference(footprint) for footprint in LEDs]

    return footprints

def get_led_positions(LED_spacing_mm=15):

    origin_x = 100
    origin_y = -400

    LED_coords = []

    for y in range(0, 10):
        for x in range(0, 10):
            LED_coords.append((x*LED_spacing_mm + origin_x, y*LED_spacing_mm + origin_y))

    return LED_coords
