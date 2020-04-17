import os
import requests
from urllib.parse import urljoin
from urllib.parse import urlencode
from elan_objects.project import Project
from elan_objects.experiment import Experiment
from elan_objects.study import Study
TIMEOUT=20

class Elan(object):

    def __init__(self, baseuri, key):

        self.baseuri = baseuri.rstrip('/') + '/'
        self.version = 'v1'
        self.cache = dict()
        self.key = key
        self.request_session = requests.Session()

        self.adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
        self.request_session.mount('http://', self.adapter)


    def get(self, uri, params=dict()):

        try:
            r = self.request_session.get(uri, params=params,
                headers={
                    'Accept' : 'application/json',
                    'X-Requested-With' : 'Swagger',
                    'Authorization' : self.key
                },
                timeout=TIMEOUT
            )
            r.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return r.json()


    def get_projects(self):
        parts = ['api', self.version, 'projects']
        url = urljoin(self.baseuri, '/'.join(parts))
        r = self.get(url)
        projects = []
        for p in r['data']:
            projects.append(Project(p))
        return projects

    def get_studies(self, project_id=None, study_id=None):
        parts = ['api', self.version, 'studies']
        url = urljoin(self.baseuri, '/'.join(parts))
        params = {}
        if project_id:
            params['projectID'] = project_id
        if study_id:
            params['studyID'] = study_id

        r = self.get(url, params)
        studies = []
        for s in r['data']:
            studies.append(Study(s))
        return studies

    def get_experiments(self, project_id=None, study_id=None):
        parts = ['api', self.version, 'experiments']
        url = urljoin(self.baseuri, '/'.join(parts))
        params = {}
        if project_id:
            params['projectID'] = project_id
        if study_id:
            params['studyID'] = study_id
        r = self.get(url, params)
        experiments = []
        for e in r['data']:
            experiments.append(Experiment(e))
        return experiments
    # response = request_session.get(elan_uri + '/api/v1/projects',
