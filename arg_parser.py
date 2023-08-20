__all__ = ["parser"]

import argparse

parser = argparse.ArgumentParser(prog="Image To ASCII",
                                  description="'Convert' given image to ascii art",
                                  epilog="|Author: KonnorFrik|",
                                  )

parser.add_argument("filename") # positional - always required

parser.add_argument("-b", "--block_size",
                    type=int,
                    help="Merge a square of pixels with a side 'block_size' into one pixel",
                    default=1,
                    ) # flags - optional by default

parser.add_argument("-r", "--reverse",
                    action="store_true",
                    default=False,
                    )

#args = parser.parse_args()
#print(type(args.filename), args.filename)
#print(type(args.block_size), args.block_size)
#print(type(args.reverse), args.reverse)

