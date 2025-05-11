import argparse
from utils.converter import convert_products

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--template', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

convert_products(args.input, args.template, args.output)
print("Dönüştürme tamamlandı.")
