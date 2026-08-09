class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set() # Set 자료형은 중복을 허용하지 않는다. 
        # for 문을 돌려서 만약에 값이 없으면 집어넣고 있으면 True, Set 안에 값이 없어서 집어넣었다면 False로 출력
        for num in nums:
            if(num in hashset):
                return True
            hashset.add(num)
        return False