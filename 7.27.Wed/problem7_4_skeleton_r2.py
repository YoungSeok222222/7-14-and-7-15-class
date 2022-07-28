class Fee():
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


    # 렌탈 비용 계산
    def get_total_rental(self):
        pass


    # 보험료 계산
    def get_total_insurance(self):
        pass

    
    # 주행 요금 계산
    def get_total_drive(self):
        pass


    def get_fee(self):
        pass


if __name__ == '__main__':
    time, distance = map(int, input('렌탈비용과 주행거리를 띄워쓰기로 구분하여 입력하세요 : ').split())
    fee_instance = Fee(time, distance)
    print(fee_instance.get_fee())
##################################
class Carsharing:
    def __init__(self,time, distance):   
        
        self.time = time
        self.distance = distance
    
    # @classmethod
    def fee(self):
        
        lent_fee =  (self.time//10) * 1200
        if self.time == 50:
            insurance_fee = 60*525
        else:
            insurance_fee = (self.time//30) * 525
        
        if self.distance >100:
            driving_fee =  100 * 170 +((self.distance - 100)*85)
        else:
            driving_fee = self.distance * 170
        result = lent_fee + insurance_fee + driving_fee
      
            
        return f"총액: {result}"


    
time, distance  = map(int, input("시간과 거리를 띄어쓰기로 구분하여 입력하세요").split())
car1 = Carsharing(time,distance)
print(car1.fee())
