import argparse
import logging
import os
import pathlib
import json

logger = logging.getLogger()

lang_extension_lookup = {
    '.py': 'Python',
    '.ts': 'Typescript',
}

def add_examples(openapi_schema: dict, examples_dir: str):
    examples_path = pathlib.Path(examples_dir)
    for filename in os.listdir(examples_path):
        file_path = examples_path / filename
        if file_path.suffix in lang_extension_lookup:
            parts = file_path.stem.split('-')
            if len(parts) >= 2:
                breakpoint()
                _path = '/'.join(parts[:-1]) if len(parts[:-1]) > 1 else parts[0] + "/"
                route_method_schema = openapi_schema['paths']['/' + _path][parts[-1]]
                code_samples = route_method_schema.get('x-codeSamples', [])
                code_samples.append({
                    'lang': lang_extension_lookup[file_path.suffix],
                    'source': file_path.read_text()
                })
                route_method_schema['x-codeSamples'] = code_samples
            else:
                logger.warning('Example filename does not meet format of {route_path}-{http_method}.{lang_extension}')
        else:
            logger.warning(f'Not a valid example file: {filename}')

def main():
    parser = argparse.ArgumentParser(description='Add examples to OpenAPI schema based on files in a directory')
    parser.add_argument('--schema_path', type=str, required=True, help='The path to the OpenAPI schema file')
    parser.add_argument('--examples_dir', type=str, required=True, help='The directory containing example files')
    
    args = parser.parse_args()

    with open(args.schema_path, 'r') as schema_file:
        openapi_schema = json.load(schema_file)

    add_examples(openapi_schema, args.examples_dir)

    with open(args.schema_path, 'w') as schema_file:
        json.dump(openapi_schema, schema_file, indent=4)

if __name__ == '__main__':
    main()
