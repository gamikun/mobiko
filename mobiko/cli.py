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
    parser.add_argument('--optimize', dest='optimize',
                        action='store_const',
                        const=True, default=False)
    parser.add_argument('--pngquant', dest='pngquant',
                        action='store_const',
                        const=True, default=False)
    args = parser.parse_args()

    filename = args.file
    dirname = os.path.dirname(filename)
    template = default_template
    basename = os.path.basename(filename)
    noextname = basename.split('.')[0]

    image = Image.open(filename).convert('RGBA')
    
    for t in template:
        size, scale = t
        absize = size * scale
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