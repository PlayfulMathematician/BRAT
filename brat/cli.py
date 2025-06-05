#!/usr/bin/env python3
"""
BRAT CLI - Bringupyourpost's Recorder Audio Thing
Commands:
  -list_projects, lists projects
  -add_project, adds projects

"""
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import datetime
import argparse
import os
import threading
import sys
import json
import uuid
from platformdirs import user_data_dir
APP_NAME = "BRAT"
APP_AUTHOR = "bringupyourpost"
BRAT_DATA_DIR = user_data_dir(APP_NAME, APP_AUTHOR)
RECORDINGS_DIR = os.path.join(BRAT_DATA_DIR, "recordings")
SCRIPTS_DIR = os.path.join(BRAT_DATA_DIR, "scriptfiles")
PROJECTS_FILE = os.path.join(BRAT_DATA_DIR, "projects.json")
os.makedirs(RECORDINGS_DIR, exist_ok=True)
os.makedirs(SCRIPTS_DIR, exist_ok=True)

def get_json():
    data_dir = user_data_dir(APP_NAME, APP_AUTHOR)
    os.makedirs(data_dir, exist_ok=True)
    json_path = os.path.join(data_dir, "projects.json")
    with open(json_path, "r") as f:
        return json.load(f)
    

def write_json(a):
    data_dir = user_data_dir(APP_NAME, APP_AUTHOR)
    os.makedirs(data_dir, exist_ok=True)
    json_path = os.path.join(data_dir, "projects.json")
    with open(json_path, "w") as f:
        json.dump(a,f)
def add_project(file):
    raise NotImplementedError()

def init_brat():
    os.makedirs(RECORDINGS_DIR, exist_ok=True)
    os.makedirs(SCRIPTS_DIR, exist_ok=True)

    if not os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, 'w') as f:
            json.dump({"projects": []}, f)

    print(f"BRAT has been initialized at: {BRAT_DATA_DIR}")


def main():
    parser = argparse.ArgumentParser(description="BringUpYourPost's Audio Record Thingy")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("init", help="Initialize BRAT")
    add_parser = subparsers.add_parser("add_project", help="Adds a Project")
    add_parser.add_argument("file", help="The File of the Script that needs to be read out")
    args = parser.parse_args()
    if args.command == "add_project":
        add_project(args.file)
    elif args.command == "init":
        init_brat()
def entry_point():
    main()