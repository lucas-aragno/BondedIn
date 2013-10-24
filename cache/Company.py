
from pymongo import *
from Collection import *
# Clase que representa la compania

class Company(Collection):
   
    def __init__(self):
        self.collection = 'Companies'
        
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getEmailDomains(self):
        return self.emailDomains

    def setEmailDomains(self, emailDomains):
        self.emailDomains = emailDomains

    def getCompanyType(self):
        return self.companyType

    def setCompanyType(self, companyType):
        self.companyType = companyType

    def getTiker(self):
        return self.tiker

    def setTiker(self, tiker):
        self.tiker = tiker

    def getWebsiteUrl(self):
        return self.websiteUrl

    def setWebsiteUrl(self, websiteUrl):
        self.websiteUrl = websiteUrl

    def getIndustries(self):
        return self.industries

    def setIndustries(self, industries):
        self.industries = industries

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getLogoUrl(self):
        return self.logoUrl

    def setLogoUrl(self, logoUrl):
        self.logoUrl = logoUrl

    def getSquareLogoUrl(self):
        return self.squareLogoUrl

    def setSquareLogoUrl(self, squareLogoUrl):
        self.squareLogoUrl = squareLogoUrl

    def getBlogRssUrl(self):
        return self.blogRssUrl

    def setBlogRssUrl(self, blogRssUrl):
        self.blogRssUrl = blogRssUrl

    def getTwitterId(self):
        return self.twitterId

    def setTwitterId(self, twitterId):
        self.twitterId = twitterId

    def getEmployeeCountRange(self):
        return self.employeeCountRange

    def setEmployeeCountRange(self, employeeCountRange):
        self.employeeCountRange = employeeCountRange

    def getSpecialities(self):
        return self.specialities

    def setSpecialities(self, specialities):
        self.specialities = specialities

    def getLocations(self):
        return self.locations

    def setLocations(self, locations):
        self.locations = locations

    def getDescription(self):
        return self.descriptions

    def setDescription(self, description):
        self.description = description

    def getEndYear(self):
        return self.endYear

    def setEndYear(self, endYear):
        self.endYear = endYear

    def getNumFollowers(self):
        return self.numFollowers

    def setNumFollowers(self, numFollowers):
        self.numFollowers = numFollowers
    
    
    

