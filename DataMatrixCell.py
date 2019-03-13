class DataMatrixCell():
    @property
    def currentStatus(self):
        return self._currentStatus

    @currentStatus.setter
    def currentStatus(self,value):
        if not isinstance(value,str):
            raise ValueError('Current status must be a string')
        elif value not in ['healthy','infected','recovered']:
            raise ValueError('Wrong current status for the cell')
        else:
            self._currentStatus=value

    @property
    def roundNumber(self):
        return self._roundNum

    @roundNumber.setter
    def roundNumber(self,value):
        if not isinstance(value,int):
            raise ValueError('rountNumber must be an int')
        else:
            self._roundNum=value

    @property
    def rowNumber(self):
        return self._rowNum

    @property
    def colNumber(self):
        return self._colNum

    def __init__(self,rowNum,colNum):
        self._roundNum=1
        self._rowNum=rowNum
        self._colNum=colNum
        print ('TBD')
