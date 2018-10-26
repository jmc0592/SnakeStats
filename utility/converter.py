class RequestConverter:

    @classmethod
    def convertFromFormDataToDictFormat(cls, formDataFormat):
        newDict = {}
        for item in formDataFormat:
            newDict[item['name']] = item['value']

        return newDict