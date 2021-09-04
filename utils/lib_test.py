#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import isfile
from json import dump, loads, dumps, load
from pprint import pprint, PrettyPrinter


class JsonManager:
    def __init__(self):
        pass

    def create_json(self, filepath, *args):
        data = {"Username": "", "Password": ""}
        if args:
            data = {"Username": f"{args[0]}", "Password": f"{args[1]}"}
        with open(filepath, 'w') as f:
            dump(data, f, indent=2, separators=(',', ':'))
        return True

    def read_json(self, filepath):
        if isfile(filepath):
            with open(filepath) as f:
                data = load(f)
            return data and True
        else:
            return False
    
    def update_json(self, filepath):
        if isfile(filepath):
            with open(filepath, 'w') as f:
                dump(data, f, indent=2, separators=(',', ':'))