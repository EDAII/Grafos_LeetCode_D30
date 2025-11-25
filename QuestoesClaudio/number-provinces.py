class Solution:
    def findCircleNum(self, isConnected):
        # número de cidades 
        n = len(isConnected)
        
        # Iniicio ninguém foi visitado (False)
        visited = [False] * n
        
        provinces = 0
        
        # (DFS)
        def dfs(cidade_atual):
            # Explorar todos os vizinhos possíveis
            for vizinho in range(n):
                # Se existe conexão direta (é 1) E o vizinho não foi visitado ainda
                if isConnected[cidade_atual][vizinho] == 1 and not visited[vizinho]:
                    
                    visited[vizinho] = True
                    # Recursão: vamos visitar os vizinhos deste vizinho
                    dfs(vizinho)
        
        # Percorre cada cidade da lista
        for i in range(n):
            # Se a cidade 'i' ainda não foi visitada, encontramos uma NOVA província
            if not visited[i]:
                provinces += 1   
                visited[i] = True 
                dfs(i)           
                
        return provinces

