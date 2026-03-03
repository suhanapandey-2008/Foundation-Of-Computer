from z3 import *

# Let's define our sets
# Assume 7 students (IDs 1-7) and 4 clubs (IDs 1-4)
students = [1,2,3,4,5,6,7]
clubs = [1,2,3,4]

# Membership list (StudentID, ClubID)
# This is what we want to check constraints on
# For example, we already have some memberships
existing_memberships = [(1,1), (2,2), (1,2), (3,1), (4,3), (5,1), (2,3), (6,2), (3,4), (7,4)]

# Create Z3 variables for a new membership
StudentID = Int('StudentID')
ClubID = Int('ClubID')

# Create solver
s = Solver()

# Constraint 1: StudentID must be in students
s.add(Or([StudentID == s_id for s_id in students]))

# Constraint 2: ClubID must be in clubs
s.add(Or([ClubID == c_id for c_id in clubs]))

# Constraint 3: Student cannot join same club twice
for mem in existing_memberships:
    s.add(Or(StudentID != mem[0], ClubID != mem[1]))

# Example: Check if adding (Student 1, Club 1) is allowed
s.push()  # Save current state
s.add(StudentID == 1, ClubID == 1)

if s.check() == sat:
    print("Allowed")
else:
    print("Not allowed - Duplicate membership")

s.pop()  # Remove last test

# Example: Check if adding (Student 7, Club 2) is allowed
s.add(StudentID == 7, ClubID == 2)

if s.check() == sat:
    print("Allowed")
    print(s.model())
else:
    print("Not allowed - Duplicate membership")