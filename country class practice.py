class country:
    def __init__(self,name,population,area):
        self.name=name
        self.population=population
        self.area=area
    
    def isbig(self):
        if self.population>250*10**6 or self.area>3*10**6:
            return True
        return False

    def compare_pd(self,country,another_country):
        density1=self.population/self.area
        