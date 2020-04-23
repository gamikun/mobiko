from __future__ import absolute_import
from mobiko.template import default_template
from mobiko.conversion import scale
from PIL import Image
from subprocess import check_call, PIPE
import os

def optimize_png(filename):
    check_call(['pngquant', '--force', '--ext', '.png', filename],
              stdout=PIPE, stderr=PIPE)

def main():
    from argparse import ArgumentParser
    
    parser = ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('target', nargs='?')
    parser.add_argument('--optimize', dest='optimize',
                        action='store_const',
                        const=True, default=False)
    parser.add_argument('--pngquant', dest='pngquant',
                        action='store_const',
                        const=True, default=False)
    args = parser.parse_args()

    if args.target:
        if os.path.isdir(args.target):
            if args.target.endswith('.xcodeproj'):
                pass

    filename = args.file
    dirname = os.path.dirname(filename)
    template = default_template
    basename = os.path.basename(filename)
    noextname = basename.split('.')[0]
    android_path = os.path.join(dirname, noextname + '-android-icons')

    if not os.path.isdir(android_path):
        os.mkdir(android_path)

    image = Image.open(filename).convert('RGBA')
    
    for t in template:
        size, scale, in_folder = t
        absize = size * scale

        if in_folder:
            scale_path = os.path.join(
                android_path,
                in_folder
            )
            if not os.path.isdir(scale_path):
                os.mkdir(scale_path)

            outfile = os.path.join(
                scale_path,
                'ic_launcher.png'
            )

        else:
            outfile = os.path.join(dirname, '{}-{}@{}x.png'\
                        .format(noextname, size, scale)
                      )

        new_size = int(absize), int(absize)
        img = image.resize(new_size, resample=Image.BICUBIC)
        img.save(outfile, optimize=args.optimize)

        if args.pngquant:
            optimize_png(outfile)


if __name__ == '__main__':
    main()