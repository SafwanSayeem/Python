def fibonacci():
    terms=int(input("How many terms:"))
    n1=0
    n2=1
    sequence=[]
    for i in range(terms):
        sequence.append(n1)
        sum=n1+n2
        n1=n2
        n2=sum
    return(sequence)
sequence=fibonacci()
print(f"The sequence is {sequence}")