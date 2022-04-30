from os import chdir, listdir, system, remove
from os.path import isfile, join
from shutil import move
from pathlib import Path
import subprocess


def print_sign(text):
    top_bottom_bar = '=' * (len(text) + 8)
    space = '=' + ' ' * (len(text) + 6) + '='
    print(top_bottom_bar)
    print(space)
    print('=' + ' ' * 3 + text + ' ' * 3 + '=')
    print(space)
    print(top_bottom_bar)


def getFiles(folder):
    return [f for f in listdir(folder) if isfile(join(folder, f))]


def main():
    Path("./output").mkdir(parents=True, exist_ok=True)
    Path("./input").mkdir(parents=True, exist_ok=True)
    chdir("./input")

    for item in getFiles("."):

        file_name = item.replace("."+item.split('.')[-1], "")
        ffmpeg = f'ffmpeg -y -i "{item}" -map v -strict -2 -vf "scale=-1:\'min(1080,ih)\'" -pix_fmt yuv420p10le -f yuv4mpegpipe "{file_name}.y4m"'
        # ffmpeg = f'ffmpeg -y -i {item} -an -vf "scale=-1:\'min(1080,ih)\'" -pix_fmt yuv420p10le -f yuv4mpegpipe {file_name}.y4m"'
        svtav1 = f'SvtAv1EncApp.exe -i "{file_name}.y4m" --preset 8 --film-grain 2 --progress 5 -b "{file_name}.ivf"'
        rav1e = f'rav1e.exe "{file_name}.y4m" -v --speed 4 -o "{file_name}.ivf"'
        avif = f'ffmpeg.exe -i "{file_name}.ivf" -c copy -map 0 -brand avis -f mp4 "..\\output\\{file_name}.avif"'

        print_sign(f'Converting {item} to y4m')

        if (subprocess.run(ffmpeg, shell=True).returncode == 0):

            print_sign(f'Converting {item} to ivf using SVT-AV1')
            if (subprocess.run(svtav1, shell=True).returncode != 0):
                print_sign(f"Cannot convert {item} using SVT-AV1. Falling back to Rav1e")
                remove(f"{file_name}.ivf")
                subprocess.run(rav1e, shell=True)

            print_sign(f'Repacking {item} to avif')
            if (subprocess.run(avif, shell=True).returncode == 0):
                print_sign(
                    f'Convert done. Moving {item} to the output folder and cleaning up')
                # move(file_name+".avif", '../output/')
                for item in getFiles("."):
                    if (item.endswith(".y4m") or item.endswith(".ivf")):
                        remove(item)
        else:
            print_sign(f'{item} cannot be converted using ffmpeg')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    exit()
