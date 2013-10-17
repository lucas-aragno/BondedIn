
from django.test import TestCase

def setUp(self):
        self.tech = ('python','java')
		
class TechTestCase(TestCase):
        
    def test_technology_is_present(self):
        
		for i in self.tech:

				# Get technology in list
				response = self.client.get('/list/'+list[i])

				# Check that the response is 200 OK.
				if self.assertEqual(response.status_code, 200):
					pass
				else:
				# Is not OK
					print (list[i]+'is not present')
					
class ProvinceTestCase(TestCase):
    def setUp(self):
        self.prov = ('misiones','formosa','chaco','buenos-aires','salta','tucuman')
        
    def test_province_is_present(self):
   
		for i in self.tech:
			for j in self.prov: 

				# Get technology and province in lists
				response = self.client.get('/list/'+list[i]+list[j])

				# Check that the response is 200 OK.
				if self.assertEqual(response.status_code, 200):
					pass
				else:
				# Is not OK
					print (list[i]+list[j]'is not present')
		 


	

       
