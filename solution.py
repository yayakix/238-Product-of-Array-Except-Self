class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currProd = 1
        arrOne = []
        for i in range(len(nums)):
            arrOne.append(currProd)
            currProd *= nums[i]

        reversedArr = nums[::-1]
        currProd = 1
        arrTwo = []
        for i in range(len(nums)):
            arrTwo.append(currProd)
            currProd *= reversedArr[i]

        arrTwoReversed = arrTwo[::-1]
        ansArr = []
        for i in range(len(nums)):
            ansArr.append(arrOne[i] * arrTwoReversed[i])
        return ansArr

