#-----------------------------------------------------------------------
# MessageIO.py
#-----------------------------------------------------------------------
import os

from .rw import Reader, Writer

class MessageFormat:
    PlainText = 'PlainText'
    Text = 'FormattedText'
    BinaryShort = 'BinaryShort'
    Binary = 'Binary'
    
class MessagePlainText:
    def __init__(self):
        self.messageFormat = MessageFormat.PlainText
        self.messageBody = ''
        self.messagePack = ''
        
    def pack(self, mtype, data):
        self.messageBody = data
        self.messagePack = data
        return self.messagePack

    def unpack(self, data):
        self.messagePack = data
        self.messageBody = data
        return (0, self.messageBody)
    
class MessageText:
    def __init__(self):
        self.messageFormat = MessageFormat.Text
        self.startSymbol = 'T'
        self.messageType = 0
        self.messageBody = ''
        self.messagePack = ''
        
    def pack(self, mtype, msg):
        self.messageType = mtype
        self.messageBody = msg
        n = len(self.messageBody)
        self.messagePack = f'{self.startSymbol}:{self.messageType}'
        self.messagePack += f':{n}:{self.messageBody}'
        return self.messagePack

    def unpack(self, data):
        self.messagePack = data
        self.messageType = 0
        self.messageBody = ''
        words = data.split(':')
        n0 = len(words)
        n1 = 0
        if n0 > 0: self.startSymbol = words[0]
        if n0 > 1: self.messageType = int(words[1])
        if n0 > 2: n1 = int(words[2])
        if n0 > 3: self.messageBody = words[3]
        return (self.messageType, self.messageBody)
    
class MessageBinaryShort:
    """ Message in a short binary format """
    def __init__(self):
        self.startSymbol = 'S'
        self.messageType = 0
        self.dataBytes = []
        
class MessageBinary:
    """ Message in a binary format """
    def __init__(self):
        self.startSymbol = 'M'
        self.messageType = 0
        self.dataBytes = []
        
class MessageIO:
    def __init__(self, reader=None, writer=None, messageFormat='PlainText'):
        self.message = None
        self.reader = None
        self.writer = None

        match messageFormat:
            case MessageFormat.PlainText: self.message = MessagePlainText()
            case MessageFormat.Text: self.message = MessageText()
            case MessageFormat.BinaryShort: self.message = MessageBinaryShort()
            case MessageFormat.Binary: self.message = MessageBinary()
        if self.reader is None:
            self.reader = Reader()
        if self.writer is None:
            self.writer = Writer()
        pass

    def pack(self, mtype, data):
        return self.message.pack(mtype, data)

    def unpack(self, data):
        return self.message.unpack(data)
