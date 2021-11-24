import re
import phonenumbers

class validator(object):

    def isPhoneNumber(agentNumber):
        try:
            x = phonenumbers.parse(agentNumber, 'US')
            if phonenumbers.is_valid_number(x):
                return True
        except:
            return False
        else:
            return False

    def isState(agentState):
        states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS",
                  "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
                  "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
                  "WI", "WY", "AS", "FM", "GU", "MH", "MP", "PR", "PW", "VI", "UM")

        if agentState in states:
            return True
        else:
            return False

    def isEmail(agentEmail):
        regex = r'[^@]+@[^@]+\.[^@]+'

        if re.fullmatch(regex, agentEmail):
            return True
        else:
            return False

    def isNone(value):
        return None

    options = {'Agent Writing Contract Start Date': isNone,
               'Agent Writing Contract Status': isNone,
               'Agent Phone Number': isPhoneNumber,
               'Agent State': isState,
               'Agent Email Address': isEmail}