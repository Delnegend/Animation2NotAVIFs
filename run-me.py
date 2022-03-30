from os import chdir, listdir, system, remove
from os.path import isfile, join
from shutil import move
from pathlib import Path

def sign(text):
    print("="*80)
    print("=\n"*2+"=")
    print("="+"      "+text)
    print("=\n"*2+"=")
    print("="*80)

Path("./output").mkdir(parents=True, exist_ok=True)
Path("./input").mkdir(parents=True, exist_ok=True)

chdir("./input")
# List all files
for item in [f for f in listdir(".") if isfile(join(".", f))]:
    extension = "."+item.split(".")[-1]
    filename = item.replace(extension, "")

    sign("Converting input(s) into YUV420p")

    if (system("ffmpeg.exe -y -i "+item+" -an -vf \"scale=-1:'min(1080,ih)'\" -pix_fmt yuv420p -f yuv4mpegpipe "+filename+".y4m") != 0):
        sign("There's something wrong with "+item)
        break

    # SVT-AV1: faster, can add film grains to improve visual (set to 30 by default in this script) but has problems with odd dimensions (https://github.com/AOMediaCodec/libavif/issues/544)
    # Rav1e: quite slower but it can work with any dimensions
    # Even though some people claims Rav1e has higher output quality (w/o film grains), but with my testing, both are same in quality and filesize.

    sign("The conversion is done. Now converting to AV1 with SVT-AVT")

    if (system("SvtAv1EncApp.exe -i "+filename+".y4m --preset 8 --film-grain 30 --progress 2 -b "+filename+".ivf") != 0):
        sign("Cannot convert "+item+" using SVT-AV1, falling back to Rav1e")
        system("rav1e.exe "+filename+".y4m -v --speed 4 -o "+filename+".ivf")

    sign("Done converting "+item+" to AV1. Now \"repacking\" to AVIF")

    system("ffmpeg.exe -i "+filename+".ivf -c copy -map 0 -brand avis -f mp4 ..\\output\\"+filename+".avif")

    sign("Done repacking "+item+" to AVIF, cleaning temporary files")

    for item in listdir("."):
        if (item.endswith(".y4m")):
            remove(item)
        if (item.endswith(".ivf")):
            remove(item)
