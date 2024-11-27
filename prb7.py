# program that detect if p1,p2,p3,p4 in a message then it is a scam
# in is keyword use to check the sentance or word is there or not it returns true or false value
p1=",ake a lot mony"
p2="buy now"
p3="subscribe this"
p4="click this"
message = input("enter your message:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("message is spam")
else:
    print("you are on right way!!")

# program to check ekta is in post or not
post = input("enter your post")
if("ekta".lower()in post.lower()): #.lower() use for all upper case and lower case is compared with it
    print("it is talking about ekta")
else:
    print("it is talking not about ekta")
