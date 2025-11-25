class Solution:
    def minSwapsCouples(self, row):
        #  número de CASAIS (metade do tamanho da fila)
        N = len(row) // 2
        
        # Inicialmente, cada casal é seu próprio "pai" (está em seu próprio conjunto)
        parent = list(range(N))
        
        # Função para encontrar o representante (raiz) do conjunto
        def find(i):
            if parent[i] == i:
                return i
            # Compressão de caminho
            parent[i] = find(parent[i])
            return parent[i]
        
        # Função para unir dois conjuntos
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            # Se já estão no mesmo conjunto, não faz nada
            if root_i == root_j:
                return False
            
            # Se são diferentes, une um ao outro
            parent[root_i] = root_j
            return True
        # -------------------------------

        # Inicialmente cada casal idealmente sozinho
        num_componentes = N
        
        # Percorremos o sofá de 2 em 2 lugares 
        for i in range(0, len(row), 2):
            # Quem está sentado aqui?
            pessoa1 = row[i]
            pessoa2 = row[i+1]
            
            # A divisão inteira por 2 dá o ID do casal. 
            # Ex: Pessoas 0 e 1 são casal 0. Pessoas 2 e 3 são casal 1.
            casal1 = pessoa1 // 2
            casal2 = pessoa2 // 2
            
            # Se as pessoas sentadas juntas NÃO são do mesmo casal,
            # isso cria uma "conexão" errada entre o Casal 1 e o Casal 2.
            # Nós unimos esses dois casais num mesmo componente do grafo.
            if union(casal1, casal2):
                # Se fizemos uma união, o num de componentes independentes diminui
                num_componentes -= 1
                
        # O número mínimo de trocas é o Total de Casais - Número de Ciclos (Componentes)
        return N - num_componentes