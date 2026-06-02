# age = int(input("Enter age: "))

# if age >= 18:
    
#     has_id = input("Do you have an ID? (yes/no): ")

#     if has_id.lower() == "yes":
#         print("You can enter the club.")
#     else:
#         print("You need an ID to enter the club.")      
# else:
#     print("You are not old enough to enter the club.")


command = input("Enter command: ")

if command == "summarize":
    print("Summarizing text...")
elif command == "save":
    print("Saving data...")
elif command == "exit":
    print("Closing tool...")
else:
    print("Unknown command")