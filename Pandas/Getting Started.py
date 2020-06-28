#better to use ipython for this file helps with visulization of data
#in cmd do ipython and run these commands
import pandas

df1 = pandas.DataFrame([[2,4,6], [10,20,30]])
print(df1, end="\n\n")
#     0   1   2
# 0   2   4   6
# 1  10  20  30

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price", "Age", "Value"], index=["First","Second"])
print(df1, end="\n\n")
#        Price  Age  Value
#First       2    4      6
#Second     10   20     30

df2 = pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])
print(df2, end="\n\n")
#   Name
#0  John
#1  Jack

df2 = pandas.DataFrame([{"Name":"John", "Surname":"Johns"},{"Name":"Jack"}])
print(df2, end="\n\n")
#   Name Surname
#0  John   Johns
#1  Jack     NaN

print(df1.mean())
#Price     6.0
#Age      12.0
#Value    18.0
#dtype: float64

print(df1.mean().mean())
#12.0

print(df1.Price)
#First      2
#Second    10
#Name: Price, dtype: int64