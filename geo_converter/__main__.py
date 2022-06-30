import argparse
import logging

from geo_converter.factory import GeoConverterFactory


def main():
    logging.basicConfig(
        format='%(levelname)s:%(message)s', level=logging.DEBUG
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='?', required=True)
    parser.add_argument('-o', '--output', nargs='?')
    args = parser.parse_args()

    factory = GeoConverterFactory(args.input, args.output)
    converter = factory.get_converter()
    converter.convert()


if __name__ == "__main__":
    main()
