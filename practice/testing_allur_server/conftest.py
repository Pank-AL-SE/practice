import pytest
import random
import test_lib.func_api as api
from test_lib import gen_data_prj as generator


@pytest.fixture(scope='function')
def create_test_project():
    projects = []

    def _start(name_prj):
        api.create_project(name_prj)
        projects.append(name_prj)
    yield _start

    def _finish(projects):
        for project in projects:
            api.delete_test_project(str(project))

    _finish(projects)


