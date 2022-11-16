
# checks that users enter a number that is more than zero
def num_check(question):
    valid = False
    while not valid:
 
         error = "Please enter a number that is ,more than zero"

         try:

            # ask a user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
               return response

            # outputs error if input is invalid
            else:
              print(error)
            print()
 
         except ValueError:
          print(error)

print()
print("*** bits calculator ****")
print()

keep_going = ""
while keep_going == "":

    width = num_check ("img width: ")
    print()
    height = num_check ("img height: ")
    print()
    interger = num_check ("interger: ") 