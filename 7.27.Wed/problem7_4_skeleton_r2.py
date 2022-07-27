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