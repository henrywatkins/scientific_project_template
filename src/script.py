#!/usr/bin/env python
"""Script title.

This text describes the purpose of the script
"""
import argparse
from pathlib import Path

def load_input(location):
    """load in data or take input from stdin"""
    return "data"

def transform_data(data):
    """perform the necessary transformation on the input data"""
    return "transformed_data"

def analysis(data):
    """perform analysis on data"""
    return "inferred results"

def plot_result(data_to_plot):
    """plot the results"""

def output_results():
    """output analysis, save to file or send to stdout"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="KCL report CSV", type=Path)
    parser.add_argument("-o","--outdir", help="output directory", type=Path, default=Path.cwd())
    args = parser.parse_args()
    if not args.outdir.exists():
        args.outdir.mkdir()
    data = load_input(args.input)
    transformed_data = transform_data(data)
    results = analysis(transformed_data)
    plot_result(transform_data)
    output_results(results)

if __name__=="__main__":
    main()
