import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("--v", "--verbosity", action="store_true", help="Increase output verbosity")
args = parser.parse_args()
answer = args.square**2

if args.v:
	print(answer)
else:
	print(answer)