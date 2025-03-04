import math

def min_max(curdepth, Index,
            maxturn, scores,
            targetdepth):
    if (curdepth == targetdepth):
        return scores[Index]
    
    if (maxturn):
        return max(min_max(curdepth + 1, Index * 2, False, scores, targetdepth),
                   min_max(curdepth + 1, Index * 2 + 1, False, scores, targetdepth))
    else:
        return min(min_max(curdepth + 1, Index * 2, True, scores, targetdepth),
                   min_max(curdepth + 1, Index * 2 + 1, True, scores, targetdepth))
    
scores = [3,5,7,11,15,20,23,23]    
treedepth = math.log(len(scores), 2)
print("Optimal Value is :", end=" ")
print(min_max(0, 0, True, scores, treedepth))