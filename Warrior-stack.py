from typing import List

class Warriors: 
    def warriors(self, strength :List[int], attack_range :List[int]):
        self.STH = strength
        self.RNG = attack_range
        ans=[]
        for index, sth in enumerate(self.STH):
            count = 1
            stackL = [index]
            stackR = [index]
            # 停止條件:
            # 1. 左邊或右邊已經沒站人了
            # 2. 左邊或右邊超出自己的攻擊範圍了
            # 3. 左邊或右邊的攻擊力比自己強了 
            # 策略:
            # 1. 由前後一格開始比，逐漸擴大比較範圍
            # 2. 再擴大範圍的次數還在攻擊範圍之內的時候，確定那一格子有站人，就比較攻擊力
            # 3. 若是對方攻擊力比自己低，就將對方的[攻擊力,跟格子(index)]放到stack
            # 4. 反之比自己高的話就pop stack 最後一個component的index存到ans stack
            # 5. 最後一個符合條件的
            while count <= self.RNG[index]:
                if (index-count) >= 0:
                    if sth > self.STH[index-count]: # 左邊比較
                        stackL.append(index-count) # 反之，代表已經比到最後，append

                if (index+count) <= len(self.STH)-1:
                    if sth > self.STH[index+count]: # 右邊比較
                        stackR.append(index+count)
        
                count+=1
            ans.append(stackL.pop())
            ans.append(stackR.pop())
        return ans

if __name__ == "__main__":
    sol = Warriors()
    print(sol.warriors([11, 13, 11, 7, 15],
                       [ 1,  8,  1, 7,  2]))
