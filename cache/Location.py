from Entity import Entity
class Location(Entity):
    description
    isHeadquarters
    isActive
    addressStreet1
    addressStreet2
    addressCity
    addressState
    addressPostalCode
    addressCountryCode
    addressRegionCode

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getIsHeadquarters(self):
        return self.isHeadquarters

    def setIsHeadquarters(self, isHeadquarters):
        self.isHeadquarters = isHeadquarters

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, isActive):
        self.isActive = isActive

    def getAddressStreet1(self):
        return self.addressStreet1

    def setAddressStreet1(self, addressStreet1):
        self.addressStreet1 = addressStreet1

    def getAddressStreet2(self):
        return self.addressStreet2

    def setAddressStreet2(self, addressStreet2):
        self.addressStreet2 = addressStreet2

    def getAddressCity(self):
        return self.addressCity

    def setAddressCity(self, addressCity):
        self.addressCity = addressCity

    def getAddressState(self):
        return self.addressState

    def setAddressState(self, addressState):
        self.addressState = addressState

    def getAddressPostalCode(self):
        return self.addressPostalCode

    def setAddressPostalCode(self, addressPostalCode):
        self.addressPostalCode = addressPostalCode

    def getAddressCountryCode(self):
        return self.addressCountreCode

    def setAddressCountryCode(self, addressCountryCode):
        self.addressCountryCode = addressCountryCode

    def getAddressRegionCode(self):
        return self.addressRegionCode

    def setAddressRegionCode(self, addressRegionCode):
        self.addressRegionCode = addressRegionCode
