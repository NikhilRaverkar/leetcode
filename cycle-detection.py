class Graph:
    def __init__(self):
        self.edges={}
        self.vertices=[]
    def addNode(self,i,j):
        if i not in self.vertices:
            self.vertices.append(i)
            #self.edges.append(i)

        if i not in self.edges:
            self.edges[i] = []
        if j not in self.vertices:
            self.vertices.append(j)

       # if j not in self.edges:
       #     self.edges[j]=[]
        self.edges[i].append(j)
        #self.edges[j].append(i)


def cycleCheck(g):
    visited=[False]*(len(g.vertices)+1)
    for root in g.vertices:
        if visited[root]==False:
            return helper(g,visited,root)
    return True

def helper(g,visited,root):

    return dfs(g,root,visited)

def dfs(g,root,visited):
    visited[root]=True
    if root not in g.edges or len(g.edges[root])<=0:
        return True
    for v in g.edges[root]:
        if visited[v]==True:
            return False
        if dfs(g,v,visited) ==False:
            return False
    visited[root]=False
    return True


if __name__=="__main__":
    g=Graph()
    g.addNode(1,2)
    g.addNode(3,4)
    g.addNode(3, 5)
    g.addNode(1,3)
    #g.addNode(5,2)
    g.addNode(2,6)
    g.addNode(7,8)
    g.addNode(8,6)
    g.addNode(5,8)
    #g.addNode(4,1)
    print("Cycle Detected" if cycleCheck(g)==False else "Cyle Not Present")