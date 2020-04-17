import sys
import argparse
import daemons
import requests
from config import elan_key,elan_uri,project_root
from elan_objects import Elan
#Daemons
def updateProjectDirectories(args):
    daemons.update_project_directories.run(elan, project_root)

if __name__ == "__main__":

    elan = Elan(elan_uri, elan_key)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    #Daemon parsers
    parser_daemons = subparser.add_parser('daemons', help='Daemon scripts: update_projects')
    subparser_daemons = parser_daemons.add_subparsers()

    parser_update_projects = subparser_daemons.add_parser('update_projects', help='Update the project directories with information from the elabjournal')
    parser_update_projects.set_defaults(func=updateProjectDirectories)

    args = parser.parse_args()
    args.func(args)
