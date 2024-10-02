#Pre-Medic-It's simple and conveys the idea of healthcare tailored to different age groups.
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
sex = input("Enter your sex: ") #note that there only 2 genders
print("What are you suffering with ?: ")
print("1.Fever")
print("2.Cold")
print("3.Headache")
print("4.Sore Throat")
print("5.StomachAche")
choice  = input("Enter your choice: ")
#1.Fever
if choice in ['1','2','3','4','5'] and choice == '1':
    if age <=12:
        if sex == 'Male' or 'Female':
            print("Medications: Paracetamol (Acetaminophen)\n")
            print("Natural Remedies: Keep the child hydrated with water\n\t\t2.juices or oral rehydration solutions\n\t\t3.Dress in lightweight clothing and use a cool compress on the forehead\n\t\t4.Lukewarm sponge bath to reduce body temperature.")
    elif age >=13 and age<=19:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Paracetamol: 500-1000 mg, every 4-6 hours, depending on the severity.\n\t\t 2.Ibuprofen: 200-400 mg, every 4-6 hours (with food).")
            print("Natural Remedies: 1.Drink plenty of water, herbal teas, or soups,\n\t\t 2.Rest in a cool environment.\n\t\t 3.Take a cool bath or apply a cold compress to the forehead.\n")
    elif age>=20 and age<=100: 
        if sex == 'Male' or 'Female':
            print("Medications: 1.Paracetamol:500-1000 mg, every 4-6 hours\n\t\t2.Ibuprofen: 400-600 mg, every 4-6 hours (with food).\n")
            print("Natural Remedies: 1.Stay hydrated with water, electrolyte solutions, or herbal teas.\n\t\t2.Rest and avoid physical exertion.\n\t\t3.Use a cool compress or take a tepid bath.")  
#2.Cold
if choice in ['1','2','3','4','5'] and choice == '2':
    if age<=12:
        if sex == 'Male' or 'Female':
            print("Medications: 1Saline nasal spray: Helps clear nasal congestion.\n\t\t2.Honey: Helps soothe sore throat and reduce coughing.")
            print("Natural Remedies: 1.Steam inhalation.\n\t\t2.Encourage fluid intake (water, soup, warm lemon water).\n\t\t3.Use a humidifier in the room to keep air moist.")
    elif age>=13 and age<=19:
        if sex =='Male' or 'Female':
            print("Medications: 1.Decongestants:(consult a doctor).\n\t\t2.Antihistamines: For runny nose and sneezing.")
            print("Natural Remedies: 1.Gargle with warm salt water for throat relief.\n\t\t2.Drink herbal teas (ginger, peppermint) or warm lemon honey water.\n\t\t3.Take steam inhalation to clear nasal passages.")
    elif age>=20 and age<=100:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Decongestants (tablets or sprays).\n\t\t2.Cough suppressants or lozenges.")
            print("Natural Remedies: 1.Stay hydrated by drinking water, herbal teas (ginger, chamomile).\n\t\t2.Gargle with salt water or use honey in warm water for sore throat relief.\n\t\t3.Inhale steam or use a humidifier to ease congestion.")
#3.HeadAChe
if choice in ['1','2','3','4','5'] and choice == '3':
    if age<=12:
        if sex == 'Male' or 'Female':
            print("Medications: Paracetamol: Safe for children with doctor-approved dosage.")
            print("Natural Remedies: 1.Ensure the child rests in a quiet, dark room.\n\t\t2.Provide fluids to prevent dehydration.\n\t\t3.Apply a cold compress to the forehead.")
    elif age>=13 and age<=19:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Paracetamol: 500 mg, every 4-6 hours.\n\t\t2.Ibuprofen: 200-400 mg, every 6 hours.")
            print("Natural Remedies: 1.Drink water or electrolyte-rich drinks if dehydration is a cause.\n\t\t2.Practice relaxation techniques (deep breathing, meditation).\n\t\t3.Apply a cool compress to the head or neck.")
    elif age>=20 and age<=100:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Paracetamol: 500-1000 mg.\n\t\t2.Ibuprofen: 400-600 mg.")
            print("Natural Remedies: 1.Drink plenty of water.\n\t\t2.Rest in a dark, quiet room.\n\t\t3.Apply a cold compress to the forehead or use essential oils like lavender.")
#4.SoreThroat
if choice in ['1','2','3','4','5'] and choice == '4':
    if age<=12:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Paracetamol: Reduces throat pain.\n\t\t2.Honey: For children above 1 year (avoid in younger children due to risk of botulism).")
            print("Natural Remedies: 1.Warm water mixed with honey and lemon.\n\t\t2.Encourage fluids (broth, warm herbal teas).\n\t\t3.Gargle with warm salt water.")
    elif  age>=13 and age<=19:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Lozenges: Helps soothe throat irritation.\n\t\t2.Antihistamines: May help reduce throat swelling due to allergies.")
            print("Natural Remedies: 1.Drink herbal teas with honey or lemon.\n\t\t2.Gargle with warm salt water.\n\t\t3.Stay hydrated with warm fluids (soup, tea).")
    elif age>=20 and age<=100:
        if sex == 'Male' or 'Female':
            print("Medications: 1.Paracetamol: 500-1000 mg, for pain relief.\n\t\t2.Throat lozenges: Relieves throat irritation.")
            print("Natural Remedies: 1.Gargle with warm salt water several times a day.\n\t\t2.Drink warm liquids (broth, herbal teas).\n\t\t3.Use honey mixed with warm water for a soothing effect.   ")
#5.StomachAche
if choice in ['1','2','3','4','5'] and choice == '5':
    if age<=12:
        if sex == 'Male' or 'Female':
            print("Medications: Simethicone: Helps relieve gas and bloating (age-appropriate dosage).")
            print("Natural Remedies: 1.Warm compress on the stomach.\n\t\t2.Encourage the child to drink small amounts of water or herbal teas.\n\t\t3.Have the child lie down with legs elevated to relieve discomfort.")
    elif age>=13 and age<=19:
        if sex == 'Male':
            print("Medications: Antacids: For indigestion or acid reflux.")
            print("Natural Remedies:1.Drink ginger tea or peppermint tea to soothe the stomach.\n\t\t2.Avoid heavy, greasy foods.\n\t\t3.Use a warm compress on the abdomen.")
        if sex == 'Female' and age>=13:
            print("Medications: Antacids: For indigestion or acid reflux.")
            print("Natural Remedies:1.Drink ginger tea or peppermint tea to soothe the stomach.\n\t\t2.Avoid heavy, greasy foods.\n\t\t3.Use a warm compress on the abdomen.")
            print("\t\t\tWomen may experience stomach aches due to menstruation or hormonal changes, where heat therapy (warm compress) and herbal teas are particularly helpful.")
    elif age>=20 and age<=100:
        if sex == 'Male':
            print("Medications: 1.Antacids.\n\t\t2.Simethicone: For gas and bloating.")
            print("Natural Remedies: 1.Drink ginger tea or chamomile tea.\n\t\t2.Apply a hot water bottle or warm compress on the abdomen.\n\t\t3.Avoid rich, fatty, or spicy foods.")
        if sex == 'Female' and age>=13 and age<=50:
            print("Medications: 1.Antacids\n\t\t2.Simethicone: For gas and bloating.")
            print("Natural Remedies: 1.Drink ginger tea or chamomile tea.\n\t\t2.Apply a hot water bottle or warm compress on the abdomen.\n\t\t3.Avoid rich, fatty, or spicy foods.")
            print("\t\t4.Women may experience stomach aches due to menstruation or hormonal changes, where heat therapy (warm compress) and herbal teas are particularly helpful.")










