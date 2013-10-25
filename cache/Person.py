from Collection import *

class Person(Collection):
   
    def __init__(self):
        self.collection = 'Person'
        self.skills = []
    
    def getId(self):
        return self.id
        
    def setId(self,id):
        self.id = id
    
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, firstName):
        self.firstName = firstName
        
    def getLastName(self):
        return self.lastName
    
    def setLastName(self, lastName):
        self.lastName = lastName
        
    def getLocationName(self):
        return self.locationName
    
    def setLocationName(self, locationName):
        self.locationName = locationName
        
    def getLocationCode(self):
        return self.locationCode
    
    def setLocationCode(self, locationCode):
        self.locationCode = locationCode
        
    def getEmailAddress(self):
        return  self.emailAddress
    
    def sertEmailAddress(self, emailAddress):
        self.emailAddress = emailAddress
        
    def getSkills(self):
        return self.skills
    
    def setSkills(self, skill):
        self.skills = skill
        
    def addSkill(self, skill):
        self.skills.append(skill)
        
    def getEducations(self):
        return self.educations
    
    def setEducations(self, educations):
        self.educations = educations
        
    def getDateOfBirth(self):
        return self.dateOfBirth
    
    def setDateOdBirth(self, date):
        self.dateOfBirth = date
        
    def getPhoneNumbers(self):
        return self.phoneNumbers
    
    def setPhoneNumbers(self, phone):
        self.phoneNumbers = phone
        
    def getMainAdress(self):
        return self.mainAddress
    
    def setMainAddress(self, address):
        self.mainAddress = address
        
    def getTwitterAccount(self):
        return self.primaryTwitterAccount
        
    def setTwitterAccount(self, account):    
        self.primaryTwitterAccount = account
        
    def getPictureUrl(self):
        return self.pictureUrl
    
    def setPictureUrl(self, picture):
        self.pictureUrl = picture
        
    def getPublicProfileUrl(self):
        return self.publicProfileUrl
    
    def setPublicProfileUrl(self, urlProfile):
        self.publicProfileUrl = urlProfile
        
    def getCompany(self):
        return self.company
    
    def setCompany(self, company):
        self.company = company
