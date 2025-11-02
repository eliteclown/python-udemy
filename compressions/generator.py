#[exp for exp in iterable if condition]-> creates list in memory
#(exp for exp in iterable if condition)-> streamlines the code and saves memory
#{exp for exp in iterable if condition}-> creates set in memory 
#{key:exp for exp in iterable if condition}-> creates dict in memory


daily_sales=[100,200,300,400,500,600,700,800,900,1000]
sales_report = sum(sale for sale in daily_sales if sale>20)
print("\n",sales_report)