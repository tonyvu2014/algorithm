def generate_outcome_count(Y, N):
    outcomeMap = {}
    outcomeMap.update({
        1: 1
    })
    if Y == 1:
        return outcomeMap

    previousOutcomeMap = generate_outcome_count(Y-1, N)
    outcomeMap.update(previousOutcomeMap)
    powerValue = Y**N
    if powerValue in outcomeMap:
        outcomeMap[powerValue] += 1
    else:
        outcomeMap[powerValue] = 1
    
    for v in previousOutcomeMap:
        newValue = v + powerValue
        if newValue in outcomeMap:
            outcomeMap[newValue] += previousOutcomeMap[v]
        else:
            outcomeMap[newValue] = previousOutcomeMap[v]

    return outcomeMap
     

def count_ways(X, N):
    max_base = int(X**(1/N))
    outcome = generate_outcome_count(max_base, N)
    return outcome.get(X, 0)

if __name__ == '__main__':
    print(count_ways(800, 2))
