import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description='Convert a XML data file into a JSON or CSV file.')
    parser.add_argument('-m', '--mode', type=int, help='[Default] 1 = Convert to JSON, 2 = Convert to CSV', default=1)
    parser.add_argument('input', type=str, help='File path to the input file')
    parser.add_argument('output', type=str, help='File path to the output file location')
    args = parser.parse_args()
    
    if (args.mode == 2):
        convert_to_csv(args.input, args.output)
    else:
        convert_to_json(args.input, args.output)

def convert_to_json(input_file_path: str, output_file_path: str) -> None:
    pass

def convert_to_csv(input_file_path: str, output_file_path: str) -> None:
    pass

if __name__ == '__main__':
    main()