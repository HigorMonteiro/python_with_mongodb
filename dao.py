from pymongo import MongoClient


class ProjectsRepository(object):
    """
    Repository implementing CRUD operations on projects collection in MongoDB
    """

    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client['projects']

    def create(self, project):
        if project is not None:
            self.database.projects.insert(project.get_as_json())
        else:
            raise Exception(
                "Nothing to save, because project parameter is None")

    def read(self, project_id=None):
        if project_id is None:
            return self.database.projects.find({})
        else:
            return self.database.projects.find({"_id": project_id})

    def update(self, project):
        if project is not None:
            self.database.projects.save(project.get_as_json())
        else:
            raise Exception(
                "Nothing to update, because project parameter is None")

    def delete(self, project):
        if project is not None:
            self.database.projects.remove(project.get_as_json())
        else:
            raise Exception(
                "Nothing to delete, because project parameter is None")
