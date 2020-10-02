2.
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals[0])
        for j in range(n-1):
            for i in range(j+1, n):
                if((intervals[j][0] <= intervals[i][0]) and (intervals[j][1] >= intervals[i][0])):  # лежит ли в текущем интервале левая точка других интервалов
                    if(intervals[j][1] >= intervals[i][1]):
                        del intervals[i]  # удаление интервала, полностью входящего в текущий интервал
                        n = n - 1
                        i = j
                    else:
                        intervals[j][1] = intervals[i][1]  # слияние с интервалом, если он пересекается с текущем
                        del intervals[i]
                        n = n - 1
                        i = j
                elif((intervals[j][0] <= intervals[i][1]) and (intervals[j][1] >= intervals[i][1])):  # лежит ли в текущем интервале правая точка других интервалов
                    if(intervals[j][0] >= intervals[i][0]):
                        intervals[j][0] = intervals[i][0]
                        del intervals[i]
                        n = n-1
                        i = j
                else:
                    if((intervals[j][0] >= intervals[i][0]) and (intervals[j][1] <= intervals[i][1])):  # лежит ли текущий интервал в каком-нибудь интервале
                        intervals[j][0] = intervals[i][0]
                        intervals[j][1] = intervals[i][1]
                        del intervals[i]
                        n = n-1
                        i = j
        return intervals
        
3.
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        n = len(intervals[0])
        for j in range(n-1):
            for i in range(j+1, n):
                if((intervals[j][0] <= intervals[i][0]) and (intervals[j][1] >= intervals[i][0])):  # лежит ли в текущем интервале левая точка дргих интервалов
                    if(intervals[j][1] >= intervals[i][1]):
                        del intervals[i]  # удаление интервала, полностью вхдоящего в текущий интервал
                        n = n - 1
                        i = j
                    else:
                        intervals[j][1] = intervals[i][1]  # слияние с интервалом, если он пересекается с текущем
                        del intervals[i]
                        n = n - 1
                        i = j
                elif((intervals[j][0] <= intervals[i][1]) and (intervals[j][1] >= intervals[i][1])):  # лежит ли в текущем интервале правая точка дргих интервалов
                    if(intervals[j][0] >= intervals[i][0]):
                        intervals[j][0] = intervals[i][0]
                        del intervals[i]
                        n = n-1
                        i = j
                else:
                    if((intervals[j][0] >= intervals[i][0]) and (intervals[j][1] <= intervals[i][1])):  # лежит ли текущий интервал в каком-нибудь интервале
                        intervals[j][0] = intervals[i][0]
                        intervals[j][1] = intervals[i][1]
                        del intervals[i]
                        n = n-1
                        i = j
        return intervals
