from elan_objects.entity import Entity

class Study(Entity):
    def __init__(self, data,work_root):
        self.__dict__ = data
        self.work_root = work_root
        self.id = self.studyID
        self.name = self.name.strip().replace('/','-')

# StudyLarge {
# studyStatus (StudyStatus, optional),
# experimentCount (integer, optional),
# meta (Array[StudyMeta], optional),
# studyID (integer, optional),
# projectID (integer, optional),
# groupID (integer, optional),
# subgroupID (integer, optional),
# userID (integer, optional),
# name (string),
# statusChanged (string, optional),
# description (string, optional),
# notes (string, optional),
# approve (string, optional) = ['NOTREQUIRED', 'BYSTUDYMANAGER']stringEnum:"NOTREQUIRED", "BYSTUDYMANAGER",
# created (string, optional),
# deleted (boolean, optional)
# }StudyStatus {
# studyStatusID (integer, optional),
# groupID (integer, optional),
# color (string, optional),
# status (string, optional),
# studyStatusType (string, optional) = ['INIT', 'POSTINIT', 'PENDING', 'PROGRESS', 'OVERDUE', 'OTHER', 'COMPLETED']stringEnum:"INIT", "POSTINIT", "PENDING", "PROGRESS", "OVERDUE", "OTHER", "COMPLETED"
# }
# StudyMeta {
# studyMetaID (integer, optional),
# metaType (string, optional) = ['TEXT', 'FILE']stringEnum:"TEXT", "FILE",
# name (string, optional),
# value (string, optional),
# studyFileID (integer, optional),
# order (integer, optional)
# }
