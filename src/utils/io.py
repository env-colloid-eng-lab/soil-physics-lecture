from __future__ import print_function

import csv

import numpy as np


def scan_data_file(file_path, delimiter):
    reader = csv.reader(open(file_path, "rt"), delimiter=delimiter)
    nr_rows = 0
    for row in reader:
        if nr_rows == 0:
            nr_cols = len(row)
        elif len(row) != nr_cols:
            return (nr_rows, nr_cols, False)
        nr_rows += 1
    return (nr_rows, nr_cols, True)


def read_data_file(file_path, nr_header_fields, delimiter, is_print_screen):
    nr_rows, nr_cols, is_file_ok = scan_data_file(file_path, delimiter)
    if not is_file_ok:
        return (nr_rows, False)

    if nr_rows == 1:
        data = np.zeros((nr_rows, nr_cols - nr_header_fields))
    else:
        data = np.zeros((nr_rows - nr_header_fields, nr_cols))

    reader = csv.reader(open(file_path, "r"), delimiter=delimiter)
    i = 0
    for row in reader:
        if is_print_screen:
            print(row)
        if nr_rows == 1:
            for j in range(nr_header_fields, len(row)):
                data[i, j - nr_header_fields] = float(row[j])
        elif i >= nr_header_fields:
            for j in range(0, len(row)):
                data[(i - nr_header_fields), j] = float(row[j])
        i += 1

    return (data, True)


def read_generic_data_file(file_path, nr_header_rows, delimiter, is_print_screen):
    nr_rows, nr_cols, is_file_ok = scan_data_file(file_path, delimiter)
    if is_print_screen:
        print("nrRows =", nr_rows, " nrCols =", nr_cols)

    if not is_file_ok:
        return (nr_rows, False)

    reader = csv.reader(open(file_path, "rt"), delimiter=delimiter)
    data = []
    i = 0
    for row in reader:
        if is_print_screen:
            print(row)
        if i >= nr_header_rows:
            data.append(row)
        i += 1
    return (data, True)
