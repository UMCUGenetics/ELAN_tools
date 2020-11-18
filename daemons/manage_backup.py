from pathlib import Path
import os
import sys
import subprocess
import logging
import logging.handlers
from modules.fill_template import TEMPLATE_PATH,TEMPLATE_ENVIRONMENT,renderTemplate
from modules.send_mail import sendMail

def backup(elan,project_workdir, project_backup,admin_mail):

    smtp_handler = logging.handlers.SMTPHandler(mailhost=("localhost", 25),
                                            fromaddr=admin_mail,
                                            toaddrs=admin_mail,
                                            subject=u"ELAN_tools manage_backup error!")
    logger = logging.getLogger()
    logger.addHandler(smtp_handler)
    errors = []
    p = Path(project_workdir)
    backup_logs = {}
    for d in p.glob('*/*/backup'):
        relative_path = d.relative_to(project_workdir)
        if len(relative_path.parts) == 3:

            for link in d.iterdir():
                if link.is_symlink():
                    resolved_link = link.resolve()

                    if not resolved_link.exists():
                        errors.append (f'Linked file does not exist: {resolved_link}')
                        continue
                    print (f'Making backup of {resolved_link}')
                    try:
                        if len(resolved_link.relative_to(project_workdir).parts) >= 4:
                            backup_loc = Path(f'{project_backup}/{resolved_link.relative_to(project_workdir)}')
                            sync_result = None
                            if not backup_loc.parent.is_dir():
                                subprocess.run(["mkdir", "-p", f'{backup_loc.parent}'])

                            if resolved_link.is_file():
                                sync_result = subprocess.run (["rsync","-av","--out-format='%t;/%f;Last Modified %M'",f'{resolved_link}',f'{backup_loc}'],stdout=subprocess.PIPE)
                            elif resolved_link.is_dir():
                                sync_result = subprocess.run (["rsync","-av","--out-format='%t;/%f;Last Modified %M'",f'{resolved_link}/',f'{backup_loc}/'],stdout=subprocess.PIPE)


                            if sync_result and "Last Modified" in sync_result.stdout.decode('utf-8'):
                                if resolved_link.owner() not in backup_logs: backup_logs[resolved_link.owner()] = []
                                backup_logs[resolved_link.owner()].extend([x.replace('Last Modified ','').replace("'",'').split(";") for x in sync_result.stdout.decode('utf-8').split("\n") if "Last Modified" in x])

                    except Exception as e:
                        errors.append(f'An exception occurred while backing up {resolved_link} to {backup_loc} with message {e}')

    if errors:
        logger.exception("\n".join(errors))

    all_lines = []
    for user in backup_logs:
        lines = []
        for i,line in enumerate(backup_logs[user]):
            (backup_time,file,mod_time) = line
            file = Path(file).relative_to(project_workdir)
            lines.append([backup_time,file,mod_time])
            all_lines.append([backup_time,file,mod_time])
        mail_content = renderTemplate('backup_mail_template.html', {'user':user,'lines':lines, 'workdir':project_workdir, 'backupdir':project_backup})
        sendMail('Cuppen backup update', mail_content, admin_mail, [user])

    admin_mail_content = renderTemplate('backup_mail_template.html', {'user':'admin','lines':all_lines, 'workdir':project_workdir, 'backupdir':project_backup})
    sendMail('Cuppen backup update', admin_mail_content, admin_mail, ['sboymans'])

def run(elan,project_workdir, project_backup,admin_mail):

    backup(elan,project_workdir, project_backup,admin_mail)
