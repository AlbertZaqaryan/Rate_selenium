from parser import parse_rate

class Change:

    def __init__(self, amd):
        self.amd = amd
        self.usd_rate, self.euro_rate, self.rub_rate = parse_rate()

    def amd_to_usd(self):
        return self.amd / self.usd_rate

    def amd_to_euro(self):
        return self.amd / self.euro_rate
    
    def amd_to_rub(self):
        return self.amd / self.rub_rate
    
Misak = Change(35000000)
print(Misak.amd_to_usd())
