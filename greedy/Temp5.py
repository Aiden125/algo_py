"""
21314 민겸 수
1. 최대값 -> M끼리 최대한 뭉치고 K랑 콜라보, 만약 k안만나면 1로 출력
2. 최소값 -> 다 별도 출력
"""
import sys
input = sys.stdin.readline

given = input().strip()

min_v = ''
max_v = ''
m_count = 0

for c in given:
    if c == 'M':
        m_count += 1
    else:
        if m_count == 0:
            min_v += '5'
            max_v += '5'
        else:
            min_v += str(10 ** (m_count - 1)) + '5'
            max_v += str((10 ** (m_count - 1)) * 50)
            m_count = 0

if m_count != 0:
    min_v += str(10 ** (m_count - 1))
    max_v += '1' * m_count

print(max_v)
print(min_v)
"""
보류
"""