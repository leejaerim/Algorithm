### 공약수들의 집합
- 숫자카드의 최대공약수를 먼저 구해야 합니다.
    - 공약수를 구할 때, 유클리드 호제법을 사용하여 구하도록 합니다. 꼭 기억해야 되는 알고리즘 입니다.
    - 유클리드 호제법의 시간복잡도는 O(logN) 입니다.
    
    <aside>
    💡 ***from math import gcd*** 
    gcd를  사용해서 쉽게 쓸 수 있지만, 알고리즘을 이해하고 쓰도록 합니다.
    
    </aside>
    
    ```python
    def calculate_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    ```

- ***숫자카드의 최대공약수의 약수집합이 모든 숫자카드를 나눌 수 있는 약수의 집합이 됩니다.***
    
    ```python
    def find_divisors(number):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)
        return divisors
    ```
- 약수 집합 끼리의 상대의 카드 집합에서 나눠지는지 체크하여 제거 합니다.
    
    ```python
    def isDivied(numbers:list,target:list):
        for i in target:
            temp = []
            for j in numbers:
                if i % j == 0:
                    temp.append(j)
            for j in temp:
                numbers.remove(j)
        if len(numbers) == 0 :
            return [0]
        else:
            return numbers
    ```
- 최종 소스
    
    ```python
    from math import gcd
    # def calculate_gcd(a, b):
    #     while b != 0:
    #         a, b = b, a % b
    #     return a
    def find_common_divisors(numbers):
        gcd_num = numbers[0]
        for number in numbers:
            gcd_num = gcd(gcd_num, number) # calculate_gcd(gcd_num, number)
        common_divisors = find_divisors(gcd_num)
        return common_divisors
    
    def find_divisors(number):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)
        return divisors
    def isDivied(numbers:list,target:list):
        for i in target:
            temp = []
            for j in numbers:
                if i % j == 0:
                    temp.append(j)
            for j in temp:
                numbers.remove(j)
        if len(numbers) == 0 :
            return [0]
        else:
            return numbers
    
    def solution(array1:list, array2:list)->int:
        a = isDivied(find_common_divisors(array1),array2)
        b = isDivied(find_common_divisors(array2),array1)
        return max(max(a),max(b))
    ```