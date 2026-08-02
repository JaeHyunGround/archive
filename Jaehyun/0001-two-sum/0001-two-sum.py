class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            cur = target - num
            if cur in map:
                return [map[cur], i]
            map[num] = i
        

# 해쉬 맵 사용
# 순열 조합을 모두 뽑는 것은 어쨋든 전체 배열을 한 번 순환하기 때문에 효율 안좋음