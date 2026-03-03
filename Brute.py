function findSeating(students):
    for each permutation P of students:
        valid = true
        
        for i from 1 to length(P)-1:
            if areFriends(P[i], P[i+1]) == true:
                valid = false
            if sameCity(P[i], P[i+1]) == true:
                valid = false
        
        if valid == true:
            return P
    
    return "No valid arrangement"
