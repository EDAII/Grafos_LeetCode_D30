from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        # 1. Construção do Grafo
        adj = defaultdict(list)
        
        for origem, destino in tickets:
            adj[origem].append(destino)
        
        # 2. Ordenação
        for origem in adj:
            adj[origem].sort(reverse=True)
            
        itinerario = []
        
        # 3. Algoritmo DFS
        def dfs(u):
            while adj[u]:
                v = adj[u].pop()
                dfs(v)
            itinerario.append(u)

        dfs("JFK")
        
        return itinerario[::-1]

