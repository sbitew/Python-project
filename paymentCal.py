print("Dear customers Welcome to Hana's Resturant")
Confir=input("are you ready to pay your bill? ")
bill=int(input("how much is your bill? "))
tip=float(input("how much percent do you want to tip? 10,15,20? "))
share=input("do you want to share with your friends? ")
friends=int(input("how many of you want to share the bill? "))
yourtotal= ((bill+(bill*tip/100))/friends)
print(f"your total is {yourtotal},thanks for coming Hana")

##height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))

#bmi= round(weight/height** 2)
#if bmi < 18.5:
   # print(f"Your BMI is {bmi}, you are underweight.")
#elif bmi <25:
    #print(f"Your BMI is {bmi}, you have a normal weight.")
#elif bmi< 30:
    #print(f"Your BMI is {bmi}, you are slightly overweight.")
#elif bmi <35:
    #print(f"Your BMI is {bmi}, you are obese.")
#else:
  #  print(f"Your BMI is {bmi}, you are clinically obese.")
 # print("V")