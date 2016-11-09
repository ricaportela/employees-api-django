import rest_framework.test


class TestEmployeesApi(rest_framework.test.APITestCase):
    def setUp(self):
        self.client = rest_framework.test.APIClient()

    def test_employee_list(self):
        response = self.client.get("/employees/")
        self.assertEqual(response.status_code, 200)

    def test_employee_data(self):
        url = 'employees'
        data = {"name":"Roberto Antonio Brito","email":"robertoempregado@empresa.com.br","departament":1},{"name":"Maria Ines","email":"mariainesempregado@empresa.com.br","departament":2},{"name":"Joao Pereira","email":"joao_pereira@empresa.com.br","departament":3}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.data, data)

