from pathlib import Path

def buildDirs(elan,project_root):

    projects = elan.get_projects()
    for p in projects:
        # print (p.name, p.projectID)
        project_name = p.name.strip().replace('/','-')
        project_path = f'{project_root}/{p.projectID}:{project_name}/'
        Path(project_path).mkdir(exist_ok=True)
        Path(project_path).chmod(0o770)
        studies = elan.get_studies(project_id=p.projectID)

        for s in studies:
            study_name = s.name.strip().replace('/','-')
            study_path = f'{project_path}/{s.studyID}:{study_name}'
            Path(study_path).mkdir(exist_ok=True)
            Path(study_path).chmod(0o770)
            Path(f'{study_path}/backup').mkdir(exist_ok=True)
            Path(f'{study_path}/backup').chmod(0o770)
            Path(f'{study_path}/raw').mkdir(exist_ok=True)
            Path(f'{study_path}/raw').chmod(0o770)
            Path(f'{study_path}/processed').mkdir(exist_ok=True)
            Path(f'{study_path}/processed').chmod(0o770)
            Path(f'{study_path}/analysis').mkdir(exist_ok=True)
            Path(f'{study_path}/analysis').chmod(0o770)

def run(elan,project_root):
    buildDirs(elan,project_root)
