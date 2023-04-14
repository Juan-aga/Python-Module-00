def print_recipe():
    for recipe in coockbook:
        print(recipe)

def print_details():
    try:
        name = input("Please enter a recipe name to get it's details:\n>> ")
    except EOFError:
        return
    try:
        coockbook[name]
    except:
        print("Sorry, this recipe does not exist.")
    else:
        print("\nRecipe for %s:\n\tIngredients list:"%name, coockbook[name]["ingredients"])
        print("\tTo be eaten for %s."%coockbook[name]["meal"])
        print("\tTake %i minutes of cooking.\n"%coockbook[name]["prep_time"])

def del_recipe():
    try:
        name = input("Please enter a recipe name to delete it:\n>> ")
    except EOFError:
        return
    try:
       del  coockbook[name]
    except:
        print("Sorry, this recipe does not exist.")
    else:
        print("Recipe %s was deleted."%name)

def add_recipe():
    ingredients = []
    try:
        recipe = input(">>> Enter a name:\n")
    except EOFError:
        return
    print(">>> Enter ingredients:")
    while 42:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        ingredients.append(line)
    try:
         meal = input(">>> Enter a meal type:\n")
    except:
        return
    print(">>> Enter a preparation time:")
    while 42:
        try:
            line = input()
        except EOFError:
            print(">>> Please insert an integer:")
        else:
            try:
                line = int(line)
            except ValueError:
                print(">>> Please insert an integer:")
            else:
                prep_time = line
                break
    coockbook[recipe] = {'ingredients':ingredients, 'meal':meal, 'prep_time':prep_time}

def print_help():
    print("List of available option:\n\t1: Add a recipe\n\t2: Delete a recipe")
    print("\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit")

if __name__=='__main__':
    coockbook = {}

    coockbook['Sandwich'] = {'ingredients':["ham", "bread", "cheese", "tomatoes"], 'meal':"lunch", 'prep_time':10}
    coockbook['Cake'] = {'ingredients':["flour", "sugar", "egss"], 'meal':"dessert", 'prep_time':60}
    coockbook['Salad'] = {'ingredients':["avocado", "arugula", "tomatoes", "spinach"], 'meal':"lunch", 'prep_time':15}
    
    f_list = [add_recipe, del_recipe, print_details, print_recipe, print_help]

    print("Welcome to the Python Cookbook !")
    f_list[4]()
    while 42:
        try:
            choose = input("\nPlease select an option:\n>>> ")
        except EOFError:
            print("\nCookbook closed. Goodbye !")
            break
        try:
            choose = int(choose) - 1
        except ValueError:
            print("Sorry, this option does not exist.")
            f_list[4]()
        else:
            if choose < 0 or choose > 4:
                print("Sorry, this option does not exist.")
                f_list[4]()
            elif choose == 4:
                print("Cookbook closed. Goodbye !")
                break
            else:
                f_list[choose]()
