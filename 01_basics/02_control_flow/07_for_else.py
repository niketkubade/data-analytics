successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("sent")
        break
else:
    print("Not Sent")
