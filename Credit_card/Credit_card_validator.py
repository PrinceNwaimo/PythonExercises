class CardValidator:
    
card_number = input("Enter your card details: ")


def even_double_digits(self, credit_card_number):
    total_sum_of_even_digits = 0
    for i in range(len(self.credit_card_number) - 2, -1, -2):
        sum_even = int(self.credit_card_number[i]) * 2
        if sum_even > 9:
            new_sum = sum_even % 10 + sum_even // 10
            total_sum_of_even_digits += new_sum
        else:
            total_sum_of_even_digits += sum_even
    return total_sum_of_even_digits


def odd_digits(self, credit_card_number):
    total_odd = 0
    for i in range(len(self.credit_card_number) - 1, -1, -2):
        total_odd += int(self.credit_card_number[i])
    return total_odd


result_of_digits = odd_digits(card_number) + even_double_digits(card_number)
if result_of_digits % 10 == 0:
    print("Card is valid")
else:
    print("Card is invalid")


def length_validity(self, credit_card_number):
    if len(self, credit_card_number) < 13 or len(self, credit_card_number) > 19:
        return "invalid"
    else:
        return "valid"


print("**Credit Card Number: " + card_number)
print(f"**Credit Card Digit Length: {+len(card_number)}")
print("**Card validity status: " + length_validity(card_number))
