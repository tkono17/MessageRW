#-----------------------------------------------------------------------
# rw.py
# -----
# Readers and Writers
#-----------------------------------------------------------------------

class Reader:
    def __init__(self, inputStream=None, mode='text'):
        self.istream = inputStream
        pass

    def read(self):
        data = None
        if self.istream is not None:
            data = self.istream.read()
        return data

    def readLine(self, delim='\n'):
        if self.istream is not None:
            if hasattr(self.istream, 'readline'):
                data = self.readline()
            elif hasattr(self.istream, 'read_until'):
                data = self.read_until(delim)
            else:
                data = self.read()
        return data
    
class Writer:
    def __init__(self, outputStream=None, mode='text'):
        self.ostream = outputStream
        pass

    def write(self, data):
        if self.ostream is not None:
            self.ostream.write(data)
        pass
    
