# A1W2A1 — Swimming tickets

| | |
|---|---|
| **Code** | `A1W2A1` |
| **Soort** | Assignment |
| **Week** | 2 — ma 14 sep t/m vr 18 sep 2026 |
| **Open vanaf** | 31 aug 2026 |
| **Af op** | do 17 sep 2026, eind van de dag |
| **Inleveren** | vr 18 sep 2026 23:59 in CodeGrade |
| **CodeGrade sluit** | vr 8 jan 2027 23:59 |
| **CodeGrade** | https://app.codegra.de/courses/21582/assignments/455959/submissions#home |

---

You want to write a program that can help you decide whether to buy a single swimming pool ticket every time you want to go swimming or to buy a monthly subscription

The program asks the user to input the following data:
- The price of a monthly subscription
- The price of a single ticket
- The number of visits they expect to make

 **Input example: **
```
> Enter subscription: 30.00
> Enter single price: 6.00
> Enter number of visits: 3
```

The program should:
1. Prompt the user for all three values
2. Calculate the total cost for single tickets
3. Compare it with the subscription price
4. Advise the user which option is cheaper
5. If they are the same, advise for single tickets
5. If the subscription is cheaper, also show how much money is saved
6. Validate the inputs with the functions `validate_int(input_str: str) -> bool` and `validate_float(input_str: str) -> bool`
   - Show the error `Invalid input` if the input format is invalid



##### Expected Output

If input is valid:
```
Single tickets: €18.0
Monthly subscription: €30.0
Advice: Buy single tickets
```

Or if subscription is cheaper:
```
Single tickets: €42.0
Monthly subscription: €30.0
Advice: Buy a subscription
You save €12.0
```

If input is invalid:
```
Invalid input
```
