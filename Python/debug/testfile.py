# Refer to README.md for the problem instructions


def computeGPA(scoreList):
    GPAs = []
    avg = 0.00
    for score in scoreList:            
        if score < 0.00 or score > 100.00:  
            return "INVALID SCORE"
        if score >= 93:                
            GPAs.append(4.00)
        elif score >= 90:
            GPAs.append(3.70)
        elif score >= 87:
            GPAs.append(3.30)
        elif score >= 83:
            GPAs.append(3.00)
        elif score >= 80:
            GPAs.append(2.70)
        elif score >= 77:
            GPAs.append(2.30)        
        elif score >= 73:
            GPAs.append(2.00)      
        elif score >= 70:
            GPAs.append(1.70)
        elif score >= 67:
            GPAs.append(1.30)
        elif score >= 65:
            GPAs.append(1.00)
        else:
            GPAs.append(0.00)
    
    GPAs.sort(reverse=True)
    GPAs.pop()
    GPAs.pop()         

    avg = sum(GPAs) / len(GPAs)
    
    finalGrade = ' '
    
    if avg == 4.0:              
        finalGrade = 'A'
    elif avg >= 3.7:             
        finalGrade = 'A-'
    elif avg >= 3.3:
        finalGrade = 'B+'
    elif avg >= 3:
        finalGrade = 'B'
    elif avg >= 2.7:
        finalGrade = 'B-'
    elif avg >= 2.3:
        finalGrade = 'C+'
    elif avg >=2:
        finalGrade = 'C'
    elif avg >= 1.7:
        finalGrade = 'C-'
    elif avg >= 1.3:
        finalGrade = 'D+'
    elif avg >= 1:
        finalGrade = 'D'
    else:
        finalGrade = 'F'
    
    return round(avg, 2), finalGrade   
