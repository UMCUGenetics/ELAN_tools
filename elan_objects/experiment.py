class Experiment(object):
    def __init__(self, data):
        self.__dict__ = data


# ExperimentLarge {
# studyID (integer, optional),
# projectID (integer, optional),
# experimentStatus (ExperimentStatus, optional),
# experimentID (integer, optional),
# groupID (integer, optional),
# subgroupID (integer, optional),
# userID (integer, optional),
# workflowStepID (integer, optional),
# name (string, optional),
# description (string, optional),
# notes (string, optional),
# created (string, optional),
# statusChanged (string, optional),
# dependencyExperimentID (integer, optional),
# due (string, optional),
# deleted (boolean, optional),
# template (boolean, optional)
# }ExperimentStatus {
# experimentStatusID (integer, optional),
# groupID (integer, optional),
# color (string, optional),
# status (string, optional),
# experimentStatusType (string, optional) = ['INIT', 'POSTINIT', 'PENDING', 'PROGRESS', 'OVERDUE', 'OTHER', 'COMPLETED']stringEnum:"INIT", "POSTINIT", "PENDING", "PROGRESS", "OVERDUE", "OTHER", "COMPLETED"
# }
