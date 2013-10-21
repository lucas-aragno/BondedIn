from django.test import TestCase

tech = ('actionscript','agile','ampq','android','angular.js','apache','asp.net','atlassianjira','avisynth','aws-ec2','aws-s3','backbone.js','c#',
		'c++','cassandra','css','cucumber','cuda','django','eclipse','ejb','express-framework','ffmpeg','flash','git','glassfish','gradle','hazelcast',
		'html','html5','java','javscript','jenkins','jboss','jboss-esb','jquery','junit','linux-administration','meteor','microsoft-azure','mongo-db',
		'mule-esb','mysql','neo4j','node.js','objective-c','online-video','oo-architecture','oo-design','opencl','oracle-db','oracle-soa','php','play-framework',
		'python','quality-center','rabbitmq','resteasy','restful-apis','ruby','ruby-on-rails','scala','selenium','sharepoint','soap','spring-framework',
		'spring-mvc','struts','testng','testrail','tomcat','tornado-web-server','urbanturtle','video-players','windows-administration','xslt')

prov = ('salta','jujuy','tucuman','corrientes','entre-rios','misiones','formosa','chaco','santiago-del-estero','sanjuan','larioja','catamarca',
		'mendoza','cordoba','santafe','buenos-aires','rio-negro','neuquen','chubut','santa-cruz','tierra-del-fuego')
					
class ProvinceTestCase(TestCase):
        
	def test_province_is_present(self):
		present = False
		global tech
		global prov
		for i in tech:
			for j in prov:
				present = self.province_is_present(i,j)
				if (present == False):
					ausent = True
		self.assertFalse(ausent)
		
	def province_is_present(self, tech, prov):
		
			# Get province in list
		response = self.client.get('/list/'+prov)

			# Check that the response is OK
		statusprov = response.status_code == 200
		if (statusprov == False):
			print tech + ' not found at ' + prov
		return statusprov

class TechTestCase(TestCase):		
		
	def technology_is_present(self, tech):
	
			# Get technology in list
		response = self.client.get('/list/'+tech)

			# Check that the response is OK
		statustech = response.status_code == 200
		if (statustech == False):
			print tech + ' not found!!!'
		return statustech
		
	def test_technology_is_present(self):
		failed = False
		global tech
		global itech
		for i in tech:
			works = self.technology_is_present(i)
			if (works == False):
				failed = True
		self.assertFalse(failed)		
	
