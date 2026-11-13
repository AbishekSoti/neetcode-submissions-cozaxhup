class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        p1 = 0
        p2 = len(people)-1
        counter =0
        while p1<p2:

            if people[p2]+people[p1]<=limit:
                counter+=1
                p2-=1
                p1+=1

            elif people[p2]+people[p1]>limit:
                counter+=1
                p2-=1


        if p1 == p2:
            counter+=1
        return counter

            
