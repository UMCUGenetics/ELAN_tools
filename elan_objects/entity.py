from pathlib import Path

class Entity(object):
    def __init__(self, data, work_root):
        self.__dict__ = data
        self.work_root = None
        self.id = None
        self.name = None
        self.work_dir = None

    def createDir(self):
        existing_dir = self._getDir()
        current_dir = Path(f'{self.work_root}/{self.id}:{self.name}')
        self.work_dir = current_dir
        if not existing_dir :
            current_dir.mkdir(exist_ok=True)
            current_dir.chmod(0o770)
        elif existing_dir != current_dir:
            existing_dir.rename(current_dir)

        return current_dir
    def _getDir(self):
        p = Path(self.work_root)
        for d in p.iterdir():
            (id,name) = d.name.split(':',1)
            if int(id) == int(self.id): return d
        return None
