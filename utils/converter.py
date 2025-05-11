import pandas as pd

def convert_products(input_file, template_file, output_file):
    df = pd.read_excel(input_file)
    df.to_excel(output_file, index=False)
