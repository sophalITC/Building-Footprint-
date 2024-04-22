from utils.report_gen import SummaryObject
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
    help="input path of csv with .csv extension")
arg = vars(ap.parse_args())


SummaryObject(arg['input'], arg["input"])
