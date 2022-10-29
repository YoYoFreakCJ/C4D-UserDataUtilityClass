class UserData:

    __baseObject: c4d.BaseObject
    __userDataId: c4d.DescID
    __userDataContainer: c4d.BaseContainer

    @staticmethod
    def Create(baseObject: c4d.BaseObject, userDataId: c4d.DescID):
        """
        :param baseObject: The base object which holds the user data.
        :param userDataId: The ID of the user data parameter to hold.
        """
        self = UserData()
        self.__baseObject = baseObject

        userDataContainer = baseObject.GetUserDataContainer()

        try:
            foundTuple = next(x for x in userDataContainer if x[0][1].id == userDataId)
            self.__userDataId = foundTuple[0]
            self.__userDataContainer = foundTuple[1]
        except Exception:
            raise Exception(f"User data {userDataId} could not be found.")

        return self          

    def Show(self):
        self.__userDataContainer[c4d.DESC_HIDE] = False
        self.__baseObject.SetUserDataContainer(self.__userDataId, self.__userDataContainer)

    def Hide(self):
        self.__userDataContainer[c4d.DESC_HIDE] = True
        self.__baseObject.SetUserDataContainer(self.__userDataId, self.__userDataContainer)

    def GetValue(self):
        return self.__baseObject[c4d.ID_USERDATA, self.__userDataId[1].id]
    
    def SetValue(self, value):
        self.__baseObject[c4d.ID_USERDATA, self.__userDataId[1].id] = value
