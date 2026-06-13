# Day-25-Prime-Factors
Day 25/100 - Python Program to Find Prime Factors of a Number

# Find Prime Factors of a Number
A program to compute and display all the prime factors of a user-inputted integer using an optimized mathematical algorithm.

## 📝 Description

This program takes an integer input from the user and calculates its prime factors. A prime factor is a prime number that divides the original number exactly without leaving a remainder.

The algorithm is structured for efficiency. First, it extracts all factors of 2 (the only even prime number) using a `while` loop, repeatedly dividing the number by 2 as long as it is even. After the number is fully reduced to an odd number, a second `while` loop checks for odd prime factors starting from 3. It increments the divisor by 2 (`i += 2`) in each step, cleverly skipping all other even numbers to save computational time.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single integer value representing the number to be factorized.

### Output:

* A formatted string stating: "Prime factors of [num] are: [factors]" where `[factors]` is a Python list of the calculated prime factors.

### Rules:

1. The program must accept an integer input from the user.
2. The program must use a function (e.g., `prime_factors`) that returns a list of factors.
3. **Step 1:** Use a `while` loop to continuously check if the number is divisible by 2. If it is, append 2 to the list and divide the number by 2 using floor division (`//=`).
4. **Step 2:** Use another `while` loop starting from `i = 3` up to the current value of the number.
5. If the number is divisible by `i`, append `i` to the list and divide the number by `i` (do not increment `i` immediately, as `i` might divide the number multiple times).
6. If the number is not divisible by `i`, increment `i` by 2 to check the next odd number.

---

## 💡 Examples

### Example 1

**Input:**

```
12


```

**Output:**

```
Prime factors of 12 are: [2, 2, 3]


```

**Explanation:** 12 is divisible by 2 (12 / 2 = 6). 6 is divisible by 2 (6 / 2 = 3). 3 is an odd number, so the first loop ends. The second loop checks 3, which is divisible by 3 (3 / 3 = 1). The loop terminates.

### Example 2

**Input:**

```
315


```

**Output:**

```
Prime factors of 315 are: [3, 3, 5, 7]


```

**Explanation:** 315 is odd, so the factor 2 is skipped. It is divisible by 3 (315 / 3 = 105), divisible by 3 again (105 / 3 = 35), divisible by 5 (35 / 5 = 7), and finally divisible by 7 (7 / 7 = 1).

### Example 3 (Prime Number Input)

**Input:**

```
13


```

**Output:**

```
Prime factors of 13 are: [13]


```

**Explanation:** Since 13 is already a prime number, it is not divisible by 2, 3, 5, 7, 9, or 11. The loop increments until `i = 13`, at which point it divides perfectly and adds 13 to the list.

### Example 4 (Input of 1)

**Input:**

```
1


```

**Output:**

```
Prime factors of 1 are: []


```

**Explanation:** 1 has no prime factors. The `n % 2 == 0` condition fails, and the `i <= n` (3 <= 1) condition fails immediately. It returns an empty list.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-25-Prime-Factors.git
cd prime-factors


```

2. **Run the program**:

```bash
python main.py


```

Enter an integer when prompted to see its sequence of prime factors printed to the console.
