def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

def rightmost_non_zero_digit():
    test_number = int(input("몇 회 실행할 것인지 입력하세요."))
    for i in range(test_number):
        factorial_number = int(input("숫자를 입력해주세요."))
        factorial_result = factorial(factorial_number)
        operator_number = factorial_result
        while(operator_number > 0):
            if (operator_number % 10) != 0 :
                print("최우측 0이 아닌 수:",operator_number % 10)
                break
            operator_number = (operator_number // 10)

rightmost_non_zero_digit()
