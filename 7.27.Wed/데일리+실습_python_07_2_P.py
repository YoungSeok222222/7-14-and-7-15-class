class Relay:
    def __init__(self,words):
        self. word = words


    def check_fail(self):
        past_word = [self.word[0]]
        if len(self.word) == 1:
            return -1
        for i in range(1,len(self.word)):
            if self.word[i] == 'done':
                return -1
            elif self.word[i][0] != past_word[-1][-1]:
                return i+1
            elif self.word[i] in past_word:
                return i+1
            past_word.append(self.word[i])
        return -1



    def get_result(self):
        result = self.check_fail()
        if result == -1:
            return "탈락한 사람이 없습니다."
        else:
            return f"{result}번째 사람이 탈락하였습니다."

if __name__ == '__main__':           
    words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
    wordrelay = Relay(words)
    print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다.