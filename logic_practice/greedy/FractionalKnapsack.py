def maxFractionalWeights(values: list, weights: list, capacity: int) -> float:
    weighted_values = []
    for i in range(len(values)):
        weighted_values.append((values[i],weights[i]))
    
    weighted_values.sort(reverse=True, key=lambda x: x[0]/x[1])

    total = 0

    for val, wt in weighted_values:
        if wt > capacity:
            total += ((val/wt)*capacity)
            capacity =0
            break
        else:
            total += val
            capacity -= wt
    
    return total

if __name__ == '__main__':
    print(maxFractionalWeights([60, 100, 120],[10, 20, 30],50))
    print(maxFractionalWeights([10, 5, 15],[2, 3, 5],6))

