from __future__ import absolute_import
from mobiko.template import default_template
from mobiko.conversion import scale
from PIL import Image
import os


def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    filename = args.file
    dirname = os.path.dirname(filename)
    template = default_template
    basename = os.path.basename(filename)
    noextname = basename.split('.')[0]

    image = Image.open(filename)

    for t in template:
        size, scale = t
        absize = size * scale
        outfile = os.path.join(dirname, '{}-{}@{}x.png'\
                    .format(noextname, size, scale)
                  )

        img = image.resize((int(absize), int(absize)), Image.ANTIALIAS)
        img.save(outfile)


if __name__ == '__main__':
    main()