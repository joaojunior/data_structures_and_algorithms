from datetime import datetime

import matplotlib.pyplot as plt


def draw_bars(items, red_elements=None):
    size = len(items)
    bar = plt.bar(list(range(size)), items, color='b')
    if red_elements:
        for i in red_elements:
            bar[i].set_color('r')
    output = str(datetime.now().timestamp()).replace('.', '')
    plt.savefig(output, dpi=300)
    plt.close()


# ffmpeg -framerate 5 -pattern_type glob -i '*.png'   -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4 # noqa
# ffmpeg -i out.mp4 -filter_complex "[0:v] scale=480:-1" -f gif out.gif
