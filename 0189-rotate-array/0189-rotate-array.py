class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k): ## 1. for문 리스트 탐색
        
        ## 2. 리스트의 마지막 원소를 제거
        ## 3. 제거해준 리스트의 마지막 원소를 리스트의 첫 번째 위치에 삽입
            nums.insert(0,nums.pop()) 