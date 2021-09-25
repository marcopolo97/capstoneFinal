import os
import unittest
import json

OWNER = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRvazdyRW5DSC1SRWJTanNqemNrcyJ9.eyJpc3MiOiJodHRwczovL2Rldi10NmZwY3E1Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0NzM4YjQ0NDY3MmMwMDY5NGQwM2I3IiwiYXVkIjoiZm9vZCIsImlhdCI6MTYzMjYwMDkzOCwiZXhwIjoxNjMyNjA4MTM4LCJhenAiOiJWN1loT0plUEhtVGk3VWl0SkJyVVFjRmNKY1d1MzRpdyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmVudHJlZXMiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmVudHJlZXMiLCJwYXRjaDplbnRyZWVzIiwicG9zdDplbnRyZWVzIl19.UJKLu4iSG7t8xftJLRGYodGInl_CXJM_xtmoW0AXoGnE68n1IS673ulhC7bqKISPBFcBHeZFzr2jX9j-PqSjRzjaAXNI2JyAIxmavXEOCexO4sGQN-2SVrPo_GcNSzNSDTB8xCcedFBpgsgIkO82zX7e-b0aVW-SrcbpfZ2jYPXi3Gv8JR3vaHBcfhRJ-lxSpoQSN7lv6NyP66HOskqLgZMTnY7Aslcci1SDWCr3VXcrD7q5JA3PDsJx6GF6wSJsD-VeBL2lpcyhZzFOxfh4mgBXIJDkZgV8uR9x1-LlQXXlAs2wOGQi_3eOlgSaDA-44Y0vLxVgh3-7YrZO5NUy6g'

CUSTOMER = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRvazdyRW5DSC1SRWJTanNqemNrcyJ9.eyJpc3MiOiJodHRwczovL2Rldi10NmZwY3E1Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE0ZjVlNDVmZTM5YmIwMDY5MWNlM2QzIiwiYXVkIjoiZm9vZCIsImlhdCI6MTYzMjU5MzQ0MywiZXhwIjoxNjMyNjAwNjQzLCJhenAiOiJWN1loT0plUEhtVGk3VWl0SkJyVVFjRmNKY1d1MzRpdyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcyIsImdldDplbnRyZWVzIl19.O6ob9Edpraj7XPIyanfLeVvdsVKOMJ5XkPIHJ7nwF_qdrAi7pwmQ5MZkwnM83Xw_iNJroBejG2Ik8BU_Pkw7WeAwmdDpX6UzyJCVjpgpkZnk-1yr5DaH0BXIh0QsDyX7X9aq7sClYQ8-JvE8msyLbpWkroPChvzXTvleHElRKYEGEKet3FntzuOFPTHMTlAyjMUg5yFP5T2_01EbhMqmP0PQBY53cAB8P01r4dldUie0PGYkQo5KOvPDTqPp_ebE1NywdYKkx1A1kciublIcWIP03FITILo8BuNvZL7hRppZ6WmBjxb04TLCE7VskY8eRMLi94bfbJMklE-bw1DR8w'


# Test for getting entrees

def test_get_entrees(self):
        res = self.client().get('/entrees')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['entrees']))


def test_404__get_entrees(self):
        res = self.client().get('/entrees?food=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

## Tests for getting the category 

def test_get_drinks(self):
        res = self.client().get('/drinks')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['drinks']))

def drinks_404_not_found(self):
        res = self.client().get('/drinks/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')



## Tests for creating a entree

def test_create_entree(self):
    new_entree = {
        "meat": "Turkey",
        "side_1": "Mashed Potatoes",
        "side_2": "Green Beans",
        "price": "$9.80"
}

    res = self.client().post('/entrees', json=self.new_entree)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)


def test_error_when_creating_entree(self):
    new_entree_error = {
        "meat": "",
        "side_1": "",
        "side_2": "",
}
    res = self.client().post('/entrees', json=self.new_entree_error)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'bad request')

# Tests for deleting a question

def test_delete_entree(self):
    res = self.client().delete('/entrees/2')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)


def test_422_if_entree_does_not_exist(self):
    res = self.client().delete('/entrees/1000')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'not found')


## Tests for updating a entree

def test_update_entree(self):
    new_entree = {
        "meat": "Turkey",
        "side_1": "Mashed Potatoes",
        "side_2": "Green Beans",
        "price": "$10.80"
}

    res = self.client().patch('/entrees/2', json=self.new_entree)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)


def test_error_when_updating_entree(self):
    new_entree_error = {
        "meat": "",
        "side_1": "",
        "side_2": "",
}
    res = self.client().patch('/entrees/130', json=self.new_entree_error)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 400)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'bad request')


# Test for getting entrees RBAC OWNER

def test_get_entrees(self):
        res = self.client().get('/entrees', headers={"Authorization": "Bearer " + OWNER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['entrees']))


# Test for creating a entree RBAC OWNER

def test_create_entree(self):
    new_entree = {
        "meat": "Turkey",
        "side_1": "Mashed Potatoes",
        "side_2": "Green Beans",
        "price": "$9.80"
}

    res = self.client().post('/entrees', json=self.new_entree, headers={"Authorization": "Bearer " + OWNER})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

# Test for getting entrees RBAC CUSTOMER

def test_get_entrees(self):
        res = self.client().get('/entrees', headers={"Authorization": "Bearer " + CUSTOMER}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['entrees']))


# Test for creating a entree RBAC CUSTOMER

def test_create_entree(self):
    new_entree = {
        "meat": "Turkey",
        "side_1": "Mashed Potatoes",
        "side_2": "Green Beans",
        "price": "$9.80"
}

    res = self.client().post('/entrees', json=self.new_entree, headers={"Authorization": "Bearer " + CUSTOMER})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
