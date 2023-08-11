from easygraphics import *

max_height = 250 

def draw_map(MAP):
    set_color("white")
    for i in range(len(MAP)):
        for j, _ in enumerate(MAP[i]):
            move_to(i, j)
            value = int( (MAP[i][j] + max_height) / (2 * max_height) * 255 - 128)
            if value > 0:
                set_color(color_rgb( int( value / 1.2 ),255 - int( value / 1 ),0))
            else:
                ratio = int(-value/255*80)
                set_color(color_rgb( 80-ratio, 160-ratio * 2, 255 + int(value/2) ) )
            line_rel(0, 0) 

def main():
    HEIGTH = 0
    WIDTH = 0 
    MAP = []
    with open('map.txt') as f: 
        HEIGTH , WIDTH = [int(x) for x in next(f).split(" ")]
        for line in f:
            MAP.append([int(x) for x in line.split()])
    init_graph(HEIGTH, WIDTH)
    set_render_mode(RenderMode.RENDER_MANUAL)

    set_background_color("black")
    draw_map(MAP)

    while is_run():
        if has_kb_msg():
            key = get_key()
            if key.key == 16777216:
                # 16777216 is the ASCII code of Esc
                close_graph()
                exit()
        delay_fps(60)

    close_graph()   

if __name__ == "__main__":
    easy_run(main)
