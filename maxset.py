__author__ = 'psinha4'


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sumArr = []
        for i, elem in enumerate(A):
            if i == 0 and elem >= 0:
                sumArr.append(elem)
            elif elem >= 0:
                if sumArr[i-1] + elem > sumArr[i-1]:
                    sumArr.append(sumArr[i-1] + elem)
                else:
                    sumArr.append(0)
            else:
                sumArr.append(-1)
        if len(sumArr) == 0:
            return 0
        maxIndex = 0
        maxIndices = [0]
        for i, elem in enumerate(sumArr[1:]):
            if elem > sumArr[maxIndex]:
                maxIndex = i+1
                maxIndices = []
                maxIndices.append(i+1)
            elif elem == sumArr[maxIndex]:
                maxIndices.append(i+1)
        #reconstruct
        maxset = []
        for index in maxIndices:
            sum = sumArr[index]
            currentset = []
            while sum >= 0:
                if A[index] < 0:
                    break
                currentset.append(A[index])
                sum -= A[index]
                if index == 0:
                    break
                else:
                    index -= 1
            maxset.append(currentset)
        maxLen = len(maxset[0])
        maxLenIndex = 0
        if len(maxset) > 1:
            for index, set in enumerate(maxset):
                if len(set) > maxLen:
                    maxLenIndex = index
        result = []
        for i in reversed(maxset[maxLenIndex]):
            result.append(i)
        return result


if __name__ == '__main__':
    arr = [ 1, 2, 5, -7, 2, 5 ]
    soln = Solution()
    soln.maxset(arr)