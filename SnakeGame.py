#https://leetcode.com/problems/design-snake-game/submissions/

from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.score = 0
        self.food = deque(food)
        self.body = deque([(0,0)])
        self.bodySet = {(0,0)}

    def move(self, direction: str) -> int:
        if direction == "U":
            next_block = (self.body[-1][0]-1,self.body[-1][1])
        elif direction == "L":
            next_block = (self.body[-1][0],self.body[-1][1]-1)
        elif direction == "R":
            next_block = (self.body[-1][0],self.body[-1][1]+1)
        else:
            next_block = (self.body[-1][0]+1,self.body[-1][1])
        if next_block[0]>=0 and next_block[0]<self.height and next_block[1]>=0 and next_block[1]<self.width:
            if next_block in self.bodySet and next_block != self.body[0] and len(self.body)>4:
                return -1
            elif self.food and list(next_block) == self.food[0]:
                self.score +=1
                self.body.append(next_block)
                self.bodySet.add(next_block)
                self.food.popleft()

            else:
                a = self.body.popleft()
                self.bodySet.remove(a)
                self.body.append(next_block)
                self.bodySet.add(next_block)



        else:
            return -1

        return self.score
