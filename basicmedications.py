#Fever
def Fever(name,age,gender):
    if age <=12:
        if gender == 'M' or 'F':
            return f"{name} as kid,the recommended medication for fever is Paracetamol (based on weight) or Ibuprofen (for children over 6 months). Natural remedies include keeping hydrated and using a cool compress."
    elif age>=13 and age<=19:
        return f"{name} as a teenager, you can take Paracetamol (500-1000 mg) or Ibuprofen (200-400 mg). Stay hydrated and try a cool bath or compress."
    else:
        return f"{name} as an adult, you can take Paracetamol (500-1000 mg) or Ibuprofen (400-600 mg). Stay hydrated and rest."
#Cold
def Cold(name,age,gender):
    if age <=12:
        if gender == 'M' or 'F':
            return f"{name} as kid,  you can use saline nasal spray and honey (if over 1 year). Natural remedies include steam inhalation and warm fluids."
    elif age>=13 and age<=19:
        return f"{name} as a teenager, use decongestants or antihistamines for relief. Drink herbal teas and try saltwater gargles."
    else:
        return f"{name} as an adult, decongestants and lozenges will help. Use saline rinses and herbal teas for relief."
#HeadAche
def HeadAche(name,age,gender):
    if age <=12:
        if gender == 'M' or 'F':
            return f"{name} as kid, you can take Paracetamol (based on weight). Natural remedies include rest, fluids, and a cold compress."
    elif age>=13 and age<=19:
        return f"{name} as a teenager, you can take Paracetamol (500 mg) or Ibuprofen (200-400 mg). Drink water and apply a cold compress."
    else:
        return f"{name} as an adult, Paracetamol (500-1000 mg) or Ibuprofen (400-600 mg) is recommended. Rest in a quiet room and stay hydrated."
#SoreThroat
def SoreThroat(name,age,gender):
    if age <=12:
        if gender == 'M' or 'F':
            return f"{name} as kid, Paracetamol,Honey can be used,Warm water mixed with honey and lemon,Encourage fluids (broth, warm herbal teas),Gargle with warm salt water."
    elif age>=13 and age<=19:
        return f"{name} as a teenager, 1.Lozenges: Helps soothe throat irritation.\n\t\t2.Antihistamines: May help reduce throat swelling due to allergies\n\t\t1.Drink herbal teas with honey or lemon.\n\t\t2.Gargle with warm salt water.\n\t\t3.Stay hydrated with warm fluids (soup, tea)."
    else:
        return f"{name} as an adult,  1.Paracetamol: 500-1000 mg, for pain relief.\n\t\t2.Throat lozenges: Relieves throat irritation.1.Gargle with warm salt water several times a day.\n\t\t2.Drink warm liquids (broth, herbal teas).\n\t\t3.Use honey mixed with warm water for a soothing effect."
#StomachAche
def StomachAche(name,age,gender):
    if age <=12:
        if gender == 'M' or 'F':
            return f"{name} as kid,  Simethicone can help relieve gas. Natural remedies include small meals, ginger tea, and avoiding greasy foods."
    elif age>=13 and age<=19:
        return f"{name} as a teenager, antacids can help. Drink peppermint tea and avoid carbonated drinks."
    else:
        return f"{name} as an adult, antacids or proton pump inhibitors are effective. Natural remedies include ginger tea and avoiding trigger foods."
#Allergies
def Allergies(name,age,gender):
    if age <=12:
        if gender == 'M' or 'F':
            return f"{name} as kid, antihistamines like cetirizine are safe. Natural remedies include saline nasal spray and avoiding allergens."
    elif age>=13 and age<=19:
        return f"{name} as a teenager, you can take loratadine or use nasal corticosteroids. Natural remedies include nasal rinses and herbal teas. "
    else:
        return f"{name}as an adult,  antihistamines like cetirizine or nasal corticosteroids can help. Natural remedies include nasal irrigation and using an air purifier."
#Patient Details
name = input("What's your name? :  ")
age = int(input("What's your age? :  "))
gender = input("Enter your gender(M/F):  ").lower()
print("What are you suffering with ?: ")
print("1.Fever")
print("2.Cold")
print("3.Headache")
print("4.Sore Throat")
print("5.StomachAche")
print("6.Allergies")
choice  = input("Enter your choice: ")
if choice == '1':
    remedy = Fever(name,age,gender)
elif choice == '2':
    remedy = Cold(name,age,gender)
elif choice == '3':
    remedy = HeadAche(name,age,gender)
elif choice == '4':
    remedy = SoreThroat(name,age,gender)
elif choice == '5':
    remedy = StomachAche(name,age,gender)
elif choice == '6':
    remedy = Allergies(name,age,gender)
else:
    remedy = f"Sorry {name}, I don't have information on the selected illness."
print("\n"+remedy)
