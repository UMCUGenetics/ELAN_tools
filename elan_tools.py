import sys
import argparse
import daemons
import requests
from config import elan_key,elan_uri,project_workdir,project_backup,admin_mail
from elan_objects import Elan
#Daemons
def updateProjectDirectories(args):
    daemons.update_project_directories.run(elan, project_workdir)

def manageBackup(args):
    daemons.manage_backup.run(elan,project_workdir, project_backup,admin_mail)

if __name__ == "__main__":

    elan = Elan(elan_uri, elan_key)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    #Daemon parsers
    parser_daemons = subparser.add_parser('daemons', help='Daemon scripts: update_projects')
    subparser_daemons = parser_daemons.add_subparsers()

    parser_update_projects = subparser_daemons.add_parser('update_projects', help='Update the project directories with information from the elabjournal')
    parser_update_projects.set_defaults(func=updateProjectDirectories)

    parser_manage_backup = subparser_daemons.add_parser('manage_backup', help='Run backup daemon')
    parser_manage_backup.set_defaults(func=manageBackup)

    args = parser.parse_args()
    args.func(args)
