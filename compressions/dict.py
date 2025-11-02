tea_prices={
    "masala chai":40,
    "cold coffee":100,
    "lemonade":50
}


dict = {item:price/10 for item,price in tea_prices.items()}
print(dict)