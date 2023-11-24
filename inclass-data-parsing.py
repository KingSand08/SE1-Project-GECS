# Code generated from gpt-4

import csv
import json
import xml.etree.ElementTree as ET
import sys
import os

def read_tsv(file_name):
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file, delimiter='\t')
        headers = next(reader, None)
        content = [row for row in reader]
    return headers, content

def convert_to_csv(headers, content, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(content)

def convert_to_json(headers, content, output_file):
    data = [dict(zip(headers, row)) for row in content]
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def convert_to_xml(headers, content, output_file):
    root = ET.Element('Data')
    for row in content:
        row_elem = ET.SubElement(root, 'Row')
        for header, data in zip(headers, row):
            data_elem = ET.SubElement(row_elem, header)
            data_elem.text = data

    tree = ET.ElementTree(root)
    tree.write(output_file)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <filename> [-c|-j|-x]")
        sys.exit(1)

    file_name = sys.argv[1]
    format_flag = sys.argv[2]
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    
    headers, content = read_tsv(file_name)

    if format_flag == '-c':
        output_file = f"{base_name}.csv"
        convert_to_csv(headers, content, output_file)
    elif format_flag == '-j':
        output_file = f"{base_name}.json"
        convert_to_json(headers, content, output_file)
    elif format_flag == '-x':
        output_file = f"{base_name}.xml"
        convert_to_xml(headers, content, output_file)
    else:
        print("Invalid format. Use '-c' for CSV, '-j' for JSON, and '-x' for XML.")
        sys.exit(1)

    print(f"File has been converted to {output_file}")

if __name__ == "__main__":
    main()
