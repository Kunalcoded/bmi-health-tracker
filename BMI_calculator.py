print("Welcome to BMI Health Tracker!")
print("Track your BMI history easily. Data saved automatically.\n")

from datetime import date
BOLD = "\033[1m"
RESET = "\033[0m"
bmi_history = []          #stores BMI history
FILENAME = "bmi_records.txt"

try:
     with open(FILENAME,"r") as file:
          for line in file:
               line = line.strip()
               if line:
                    parts = line.split("|")
                    if len(parts) == 7:
                        record = {
                             "Name": parts[0],
                        "Age": int(parts[1]),
                        "date": parts[2],
                        "BMI": float(parts[3]),
                        "raw_Weight": (parts[4]),
                        "raw_height": (parts[5]),
                        "category": parts[6]
                        }
                        bmi_history.append(record)
except FileNotFoundError:
     pass          

def bmi_calculator():      #BMI calculator code
                
                
                     
                     
                action = input("What do you want to do?\n1: Calculate new BMI\n2: View previous records\nChoose (1 or 2): ").strip()
                if action == "2":
                     if not bmi_history:
                          print(f"No BMI history available yet!")
                     else:
                          print("Your BMI history:")
                          for i, record in enumerate(bmi_history,1):
                               print(f"{i}.{record["Name"]} your BMI on {record["date"]} was {BOLD}{record["BMI"]}{RESET} ({record["category"]}), the weight was {record["raw_Weight"]} and the height was {record["raw_height"]}")
                                
                     return
                if action != "1":
                     print("Going back to main menu.\n")
                     return              
                
                try:
                    name = input("Enter your name?: ").strip().title()
                    age = int(input("Enter your age: "))
                    Weight= input("Weight(kg/lbs): ").lower()
                    value = 2.20462
                    if Weight.endswith("lb") or Weight.endswith("lbs"):
                        kg = float(Weight.replace("lbs", "").replace("lb", "").strip()) / value
                    else:
                        kg = float(Weight.replace("kg", "").strip())

                    height_raw = input("Enter your height(m,cm,ft)= ").strip()
                    if height_raw.endswith("cm"):
                        height = float(height_raw.replace("cm", "").strip()) / 100
                    elif height_raw.endswith("m"):
                        height = float(height_raw.replace("m", "").strip())
                    elif "ft" in height_raw or "'" in height_raw:
                        cleaned = height_raw.replace("ft", " ").replace("'", " ").replace('"', " ")
                        parts = cleaned.split()
                        feet = float(parts[0])
                        inches = float(parts[1]) if len(parts) > 1 else 0
                        height = (feet * 12 + inches) * 0.0254
                    else:
                        height = float(height_raw)  # assume meters
                    bmi = kg/height**2
                    bmi_rounded = round(bmi,1)
                    if bmi < 18.5:
                        Category = "Underweight"
                        message = "Eat more nutritious food to gain weight!"
                    elif 18.5 <= bmi <= 24.9:
                        Category = "Normal weight"
                        message ="Great job! Keep maintaining your healthy lifestyle."
                    elif 25.0 <= bmi <= 29.9:
                        Category = "Overweight"
                        message = "Try regular exercise and balanced diet to stay healthy."
                    elif 30 <= bmi <= 34.9:
                        Category = "Obesity (Class 1)"
                        message = "Consider consulting a doctor and starting a fitness plan."
                    elif 35 <= bmi <= 39.9:
                        Category = "Obesity (Class 2)"
                        message = "It's important to take action — talk to a healthcare professional."
                    else:
                        Category = "Extreme Obesity"
                        message = "Seek medical help immediately for your health."

                    records = {
                         "Name" : name,
                         "Age" : age,
                         "date" : date.today().strftime("%d %B %Y"),
                         "BMI" : bmi_rounded,
                         "raw_Weight" : Weight,
                         "raw_height" : height_raw,
                         "category" : Category
                   }
                    bmi_history.append(records)

                    with open(FILENAME,"a") as file:
                     line = f"{records['Name']}|{records['Age']}|{records['date']}|{records['BMI']}|{records['raw_Weight']}|{records['raw_height']}|{records['category']}\n"
                     file.write(line)

                   
                  
                    print(f"hey {name} your BMI comes out to be {bmi_rounded}, ({Category})") 
                    print(message)
                    print(f"\nBMI saved! Total records: {len(bmi_history)}")
                    print("You got this!") 

                except ValueError:
                     print("Please enter valid values!!")  


def History_remover():
      check = input("Are you sure(History can't be retrived after)\nyes or no: ").strip()
      if check.upper() == "YES":
        bmi_history.clear()
        with open(FILENAME, "w") as file:
            file.write("")
        print("History removed")

      elif check.upper() == "NO":
        print("Returning back to menu")

      else:
           print("Invalid entry")


           
                                 
        

        


use = input("Do you want to use the app? ").strip()

if use.upper() == "NO":
    print("No problem, maybe next time!")
else: 
    while True:
            print("\n-----Menu----")            #Main menu
            print("\noption 1: BMI calculator ")
            print("\noption 2: Delete History")
            print("\noption 3: Quit")
            print("\n")
            button = int(input("choose one option: "))

            try:

                if button == 1:
                    print("BMI Calculator\n")

                    bmi_calculator()

                elif button == 2:
                    History_remover()
                            
                elif button == 3:
                    print("Goodbye!Maybe next time")
                    print("Thanks for visiting")
                    break
            

                else:
                    print("Invalid entry") 


            except ValueError:
                 print("Invalid entry.Please enter a number 1-3")        

                
                        
                    
                        
                    





                   

                     
                    


                    
                
                
                        
            




     
          
     
     
     

          
        



