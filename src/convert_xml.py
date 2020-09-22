import argparse
import xml.etree.ElementTree as ET
import json
import csv

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
    data = xml_to_list(input_file_path)
    json_dict = {}
    json_dict['data'] = []
    for date, temp in data:
        json_dict['data'].append([date, float(temp)])
    with open(output_file_path, 'w') as output_file:
        json.dump(json_dict, output_file)

def convert_to_csv(input_file_path: str, output_file_path: str) -> None:
    data = xml_to_list(input_file_path)
    for date, temp in data:
        print(f'Date: {date} Temp: {temp}')

def xml_to_list(input_file_path: str) -> list:
    try:
        data_list = list()
        root = ET.parse(input_file_path).getroot()
        for data in root.findall('data'):
            year = data.find('year').text
            temp_degree_c = data.find('value').text
            data_list.append((year, temp_degree_c))
        return data_list
    except:
        print('Error: unable to parse data from input XML file.')
        exit(-1)
        

if __name__ == '__main__':
    main()