class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        targetNum = int("".join(map(str, digits))) + 1
        return [int(d) for d in str(targetNum)]
        
        
# "구분자".join(array) : 매개변수로 들어온 배열을 하나의 문자열로 구분자를 사용해서 합쳐주는 함수
# "".join() 는 문자열 리스트만 받기 때문에 map 함수를 통해 문자열 데이터로 변환