class Wordrelay():
    # 1. words 리스트를 전달받아 인스턴스 변수로 만드는 생성자를 구현하세요
    def __init__(self,words):
        self.words = words #wordrelay.words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]

    # 2. 실패와 성공 여부를 결정하는 함수를 구현하세요
    # i번째 사람이 탈락을 했다
    # 혹시 탈락이 없건, 'done'을 만난다면 return -1
    def check_fail(self):
        past_words = [self.words[0]]
        if len(self.words) == 1:
            return -1

        for i in range(1,len(self.words)):
            #"done"을 만나면 return -1
            if self.words[i] =="done":
                return -1
            
            #바로 이전 단어의 끝말과 동일하지 않으면 fail
            if self.words[i][0] != past_words[-1][-1]:
                return i+1
            #이전 단어를 다시 말하면 fail
            elif self.words[i] in past_words:
                return i+1
            
            past_words.append(self.words[i])

        #전부 통과하면 return -1
        return -1
    # 3. 결과를 돌려주는 함수를 작성하세요.
    def get_result(self):
        #-1을 받으면 전부 통과
        # i라는 변수값을 받으면 i번쨰 사람이 탈락 문구 출력
        result = self.check_fail()
        if result == -1:
            return '탈락한 사람이 없다'
        else:
            return f'{result}번 째 사람이 탈락하였습니다.'
        
        #result = self.check_fail()
        #return '탈락한 사람이 없다' if result ==1 else f'{result}번째 사람이 탈락하였습니다.''


if __name__ == '__main__':
    words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
    wordrelay = Wordrelay(words)
    print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다.