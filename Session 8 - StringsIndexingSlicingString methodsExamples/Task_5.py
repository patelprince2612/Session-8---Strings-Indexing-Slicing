# 5.
# Create a function mask_phone_number(phone) that takes a 10-digit phone number as a string and returns it in the 
# format '******1234', showing only the last 4 digits like Paytm does.<br><br><em><strong>Hint:</strong> Use string slicing 
# and concatenation.</em>

phone_num = input("Ente rhte phone number : ")[:10]

print(f"phone number : {phone_num}")

def  mask_phone_number(phone):

    last_four = phone[6:]

    masked_number = "******" + last_four

    print(masked_number)
    
mask_phone_number(phone_num)