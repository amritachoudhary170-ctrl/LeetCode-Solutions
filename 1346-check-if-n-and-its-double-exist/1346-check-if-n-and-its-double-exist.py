class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        arr1 = set()

        for num in arr:
            if num * 2 in arr1 or (num % 2== 0 and num // 2 in arr1):
                return True

            arr1.add(num)

        return False