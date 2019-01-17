import json
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if len(dislikes) <= 1:
            return True
        color = [-1] * (N + 1)
        neighbour = [[] for _ in range(N + 1)]
        visited = [False] * (N + 1)

        for i in dislikes:
            neighbour[i[0]].append(i[1])
            neighbour[i[1]].append(i[0])

        start = dislikes[0][0]
        color[start] = 1
        queue = []
        queue.append(start)

        for i in range(N + 1):
            if not visited[i]:
                queue.append(i)
            while queue:
                element = queue.pop()
                if not visited[element]:
                    visited[element] = True
                    for v in neighbour[element]:
                        if color[v] == -1:
                            color[v] = 1 - color[element]
                            queue.append(v)

                        if color[element] == color[v]:
                            return False
        return True


def stringToInt(input):
    return int(input)


def stringToInt2dArray(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            N = stringToInt(line)
            line = lines.next()
            dislikes = stringToInt2dArray(line)

            ret = Solution().possibleBipartition(N, dislikes)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()