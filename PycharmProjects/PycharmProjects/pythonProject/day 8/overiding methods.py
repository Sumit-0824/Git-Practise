class Bank:
    def rateofInterest(self):
        return 0
class XBank(Bank):
    def rateofInterest(self):
        return 10

class YBank(Bank):
    def rateofInterest(self):
        return 12

objx=XBank()
print(objx.rateofInterest())#10

objy=YBank()
print(objy.rateofInterest())#12