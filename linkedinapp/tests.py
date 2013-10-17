
from django.test import TestCase

def setUp(self):
	self.tech = ('actionscript','agile','ampq','android','angular.js','apache','asp.net','atlassianjira','avisynth','aws-ec2','aws-s3','backbone.js','c#',
					'c++','cassandra','css','cucumber','cuda','django','eclipse','ejb','express-framework','ffmpeg','flash','git','glassfish','gradle','hazelcast',
					'html','html5','java','javscript','jenkins','jboss','jboss-esb','jquery','junit','linux-administration','meteor','microsoft-azure','mongo-db',
					'mule-esb','mysql','neo4j','node.js','objective-c','online-video','oo-architecture','oo-design','opencl','oracle-db','oracle-soa','php','play-framework',
					'python','quality-center','rabbitmq','resteasy','restful-apis','ruby','ruby-on-rails','scala','selenium','sharepoint','soap','spring-framework',
					'spring-mvc','struts','testng','testrail','tomcat','tornado-web-server','urbanturtle','video-players','windows-administration','xslt')
	
class TechTestCase(TestCase):
        
    def test_technology_is_present(self):
<<<<<<< HEAD
        global tech
	for i in tech:

			# Get technology in list
			response = self.client.get('/list/'+list[i])

			# Check that the response is 200 OK.
			if self.assertEqual(response.status_code, 200):
				pass
			else:
			# Is not OK
				print (list[i]+'is not present')
=======
        
		for i in tech:

				# Get technology in list
				response = self.client.get('/list/'+list[i])

				# Check that the response is 200 OK.
				if self.assertEqual(response.status_code, 200):
					pass
				else:
				# Is not OK
					print (list[i]+'is not present')
>>>>>>> f642d022f703206b0c016baf309e7dd765be9f20
					
class ProvinceTestCase(TestCase):
    def setUp(self):
        self.prov = ('salta','jujuy','tucuman','corrientes','entre-rios','misiones','formosa','chaco','santiago-del-estero','sanjuan','larioja','catamarca',
					'mendoza','cordoba','santafe','buenos-aires','rio-negro','neuquen','chubut','santa-cruz','tierra-del-fuego')
        
    def test_province_is_present(self):
<<<<<<< HEAD
		global tech
		global prov
=======
   
>>>>>>> f642d022f703206b0c016baf309e7dd765be9f20
		for i in tech:
			for j in prov: 

				# Get technology and province in lists
				response = self.client.get('/list/'+list[i]+list[j])

				# Check that the response is 200 OK.
				if self.assertEqual(response.status_code, 200):
					pass
				else:
				# Is not OK
					print (list[j]+'is not present')
		 


	

       
