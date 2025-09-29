#  TASK FOUR: Name Organizer
name_request = input("Kindly enter 5 names separated by spaces only: ")
conv_name_request = name_request.lower().split()    #   converting to lowercase
conv_name_request.sort()
print(*conv_name_request, sep='\n')
