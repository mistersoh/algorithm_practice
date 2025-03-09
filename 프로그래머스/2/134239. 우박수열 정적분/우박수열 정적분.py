def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    sequence.append(1)
    return sequence

def get_integrals(coords):
        integrals = []
        for i, coord in enumerate(coords[:-1]):
            y1, y2 = coord, coords[i + 1]
            integrals.append(min(y1, y2) + abs(y1 - y2) / 2)
        return integrals

def solution(k, ranges):
    answer = []
    
    coords = collatz_sequence(k)
    integrals = get_integrals(coords)
    
    n = len(coords)
    
    for x1, x2 in ranges:
        x2 = x2 if x2 > 0 else n + x2 - 1
        if x1 > x2:
            answer.append(-1)
            continue
        SUM = 0
        for i in range(x1, x2):
            SUM += integrals[i]
        answer.append(SUM)
    
    return answer