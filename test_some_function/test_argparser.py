import argparse
parser=argparse.ArgumentParser(description="test")
parser.add_argument("echo")
args=parser.parse_args()
print(args.echo)