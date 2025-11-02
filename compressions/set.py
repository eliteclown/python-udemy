recipie ={
    "Masala chai": ["Tea leaves", "Water", "Milk", "Sugar", "Spices"],
    "Cold Coffee": ["Coffee", "Ice Cream", "Milk", "Sugar", "Ice cubes"],
    "Lemonade": ["Lemon", "Water", "Sugar", "Ice cubes"]
}

all = {spices for ingredients in recipie.values() for spices in ingredients}
print(all)