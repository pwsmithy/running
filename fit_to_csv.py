#! /usr/bin/env python
from argparse import ArgumentParser

from fitparse import FitFile
import pandas as pd

def convert_fit_to_csv(fit_path_in, csv_path_out):
    fitfile = FitFile(fit_path_in)


    timestamps = []
    fields = dict(
        speed=[],
        heart_rate=[],
    )

    for record in fitfile.get_messages("record"):
        timestamps.append(record.get_value("timestamp"))
        for key in fields:
            fields[key].append(record.get_value(key))

    pd.DataFrame(fields, timestamps).to_csv(csv_path_out)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("fit_file")
    parser.add_argument("--csv-out", required=True, help="path to which CSV file will be written")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    convert_fit_to_csv(args.fit_file, args.csv_out)
