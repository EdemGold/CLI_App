import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
x = parser.parse_args()

print(x.echo)

