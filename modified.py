def find_cube_pairs(target): # add missing colon
    solutions = [] # remove semi-colon (optional)
    max_num = round(target ** (1/3)) # fix exponentiation operator from *** to **, fix variable name from targ to target

    for a in range(1, max_num + 1): #add missing colon and fix range function from ranges to range
        for b in range(a, max_num + 1): # add missing colon and fix range function from ranges to range
            if a**3 + b**3 == target: # fix exponentiation operator from *** to **, fix variable name from targ to target
                solutions.append((a, b)) # fix variable name from sol to solutions and remove semi-colon (optional)
    return solutions # fix variable name from sol to solutions

pairs = find_cube_pairs(1729) # remove unnecessary comma at the end of the line
print("Valid cube pairs for 1728:") # use print instead of printf, remove unnecessary comma at the end of the line
for a, b in pairs: # fix variable name from pair to pairs and add missing colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728") # use print instead of printf
"""Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u""" # fix indentation error

# The purpose of this code is to find pairs of integers (a, b) such that a^3 + b^3 = 1729. (Ramanujan-Hardy number)