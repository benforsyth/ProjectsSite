from django.test import TestCase
from plusfour.projects.models import Project, Technology


class ProjectViewTests(TestCase):
    def setUp(self):
        self.p1 = Project.objects.create(name='first', description='my first project', ranking=1)
        self.p2 = Project.objects.create(name='second', description='my other project', ranking=2)

        t1 = Technology.objects.create(framework='django', language='python')
        t1.project.add(self.p1, self.p2)
        t2 = Technology.objects.create(framework='stl', language='c++')
        t2.project.add(self.p1, self.p2)
        t3 = Technology.objects.create(framework='cocoa', language='objective c')
        t3.project.add(self.p2)

    def test_list_view(self):
        r = self.client.get('/api/v1/projects/')
        self.assertEqual(r.status_code, 200)
        projects = r.data
        self.assertEqual(len(projects), 2)
        self.assertEqual(projects[0].get('name'), 'first')
        self.assertEqual(projects[0].get('description'), 'my first project')
        self.assertEqual(projects[0].get('ranking'), 1)
        self.assertEqual(projects[0].get('pk'), self.p1.id)
        self.assertEqual(projects[1].get('name'), 'second')
        self.assertEqual(projects[1].get('description'), 'my other project')
        self.assertEqual(projects[1].get('ranking'), 2)
        self.assertEqual(projects[1].get('pk'), self.p2.id)

    def test_detail_view_project_first(self):
        r = self.client.get('/api/v1/projects/{}/'.format(self.p1.id))
        self.assertEqual(r.status_code, 200)
        project = r.data
        self.assertEqual(project.get('name'), 'first')

        technology = project.get('technology')
        self.assertEqual(len(technology), 2)
        self.assertEqual(technology[0].get('framework'), 'django')
        self.assertEqual(technology[0].get('language'), 'python')
        self.assertEqual(technology[1].get('framework'), 'stl')
        self.assertEqual(technology[1].get('language'), 'c++')


    def test_detail_view_project_second(self):
        r = self.client.get('/api/v1/projects/{}/'.format(self.p2.id))
        self.assertEqual(r.status_code, 200)

        projects = r.data
        self.assertEqual(projects.get('name'), 'second')

        technology = projects.get('technology')
        self.assertEqual(len(technology), 3)
        self.assertEqual(technology[0].get('framework'), 'django')
        self.assertEqual(technology[0].get('language'), 'python')
        self.assertEqual(technology[1].get('framework'), 'stl')
        self.assertEqual(technology[1].get('language'), 'c++')
        self.assertEqual(technology[2].get('framework'), 'cocoa')
        self.assertEqual(technology[2].get('language'), 'objective c')