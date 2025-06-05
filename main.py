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
brat_dir = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()
if brat_dir != current_dir:
    print("\033[31m❌ You must run BRAT from its own directory:\033[0m")
    print(f"   cd {brat_dir}")
    sys.exit(1)


def get_json():
    try:
        with open("./project_data/projects.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit("BRAT CLI is not initialized, use init to set up BRAT CLI")
def add_project(file):
    raise NotImplementedError("I didn't implement this")

def init_brat():
    os.makedirs("./data/", exist_ok=True)
    os.makedirs("./data/recordings/", exist_ok=True)
    os.makedirs("./data/scriptfiles/", exist_ok=True)
    file_path = os.path.join("./data/", "projects.json")
    if not os.path.exists(file_path):
      with open(file_path, 'w') as f:
        json.dump({"projects": []}, f)
    
    print("BRAT CLI has been set up")


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
if __name__ == "__main__":
  main()