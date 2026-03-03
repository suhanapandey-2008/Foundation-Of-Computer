function heuristicSeating(students):

    for each student:
        compute conflictCount(student)

    sort students by conflictCount descending

    seating = empty list

    for each student S:
        placed = false
        
        for position from 1 to n:
            if placing S does not violate rules:
                place S
                placed = true
                break
        
        if placed == false:
            return "Heuristic failed"

    return seating
