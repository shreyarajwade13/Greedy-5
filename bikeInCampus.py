"""
sortedDict approach (refer notes section for details)

Worst case -- if there are unique distances between each worker and bike
TC - O(n * m) + log nm
 O(n * m) --> since nm entries in sortedDict
 log nm --> sorting
 SC - O(n * m)

 Avg case (optimal solution) --
 TC - O(m * m)
 SC - O(n * m)
"""


class Solution:
    def computeDistance(self, worker, bike):
        return (abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]))

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if workers is None or len(workers) == 0: return []

        distWorkerBikePairMap = SortedDict()

        for w in range(len(workers)):
            for b in range(len(bikes)):
                # compute manhattan distance
                manhattanDistance = self.computeDistance(workers[w], bikes[b])

                # if distance not in sorted map
                if manhattanDistance not in distWorkerBikePairMap:
                    distWorkerBikePairMap[manhattanDistance] = []

                # add worker, bike pair to distance list in map
                distWorkerBikePairMap[manhattanDistance].append([w, b])

        workersAllocated = [False for w in range(len(workers))]
        bikesAllocated = [False for b in range(len(bikes))]
        countAllocated = 0
        finalAllocations = [0 for w in range(len(workers))]

        for distance in distWorkerBikePairMap:
            # get current list of pairs
            currDistanceList = distWorkerBikePairMap[distance]
            # print("currDistanceList = ", currDistanceList)

            for eachPair in currDistanceList:
                # break when all workers are alloted with bikes
                if countAllocated == len(finalAllocations):
                    return finalAllocations

                # get ids from the pair
                workerID = eachPair[0]
                bikeID = eachPair[1]

                if workersAllocated[workerID] == False and bikesAllocated[bikeID] == False:
                    workersAllocated[workerID] = True
                    bikesAllocated[bikeID] = True
                    finalAllocations[workerID] = bikeID
                    countAllocated += 1

        return finalAllocations