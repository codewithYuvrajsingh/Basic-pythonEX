# just a simple truth or dare game 
game = input("choose Truth or Dare: ").lower()
if game == "truth":
    truth = input(" What is your biggest fear ? ")
elif game == "dare":
    dare = input("Do 10 push ups !")
else:
    print("Please choose either truth or dare.")       
# add more truths and dares 