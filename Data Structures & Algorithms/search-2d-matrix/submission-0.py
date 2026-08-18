class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) - 1
        n = (len(matrix[0])) - 1
        m_start = 0
        n_start = 0

        while m_start <= m:

            m_mid = m_start + (m - m_start) // 2

            if matrix[m_mid][0] <= target and matrix[m_mid][n] >= target:
                while n_start <= n:
                    n_mid = n_start + (n - n_start) // 2
                    if matrix[m_mid][n_mid] == target:
                        return True
                    elif matrix[m_mid][n_mid] < target:
                        n_start = n_mid + 1
                    else:
                        n = n_mid - 1
                else:
                    return False
            
            if matrix[m_mid][0] < target:
                m_start = m_mid + 1
            else:
                m = m_mid - 1

        return False