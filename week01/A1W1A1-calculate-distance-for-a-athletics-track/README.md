# A1W1A1 — Calculate distance for a athletics track

| | |
|---|---|
| **Code** | `A1W1A1` |
| **Soort** | Assignment |
| **Week** | 1 — ma 7 sep t/m vr 11 sep 2026 |
| **Open vanaf** | 31 aug 2026 |
| **Af op** | do 10 sep 2026, eind van de dag |
| **Inleveren** | vr 11 sep 2026 23:59 in CodeGrade |
| **CodeGrade sluit** | vr 8 jan 2027 23:59 |
| **CodeGrade** | https://app.codegra.de/courses/21582/assignments/455889 |

---

#### Objective
Write a Python program that calculates the total distance someone has run based on the number of laps on a standard athletics track.

#### Problem description
- A standard athletics track lap is **400 meters**.
- The program should ask (prompt) the user to input the number of laps in the following format:
  ```
  Laps: 7
  ```
- Be aware that the input is `Laps: 7` and not just `7`
- The program must extract the number from the input string, calculate the total distance in **meters**, and convert that to **kilometers** (as a decimal).
- Keep the program simple. No need for error handling (you can assume that the input will always be correct).

#### Expected Program Behaviour
- Prompt the user for user input. ask "Please enter the number of laps:", e.g., `Laps: 7`
- Extract the number `7` from the input
- Calculate the distance:
  - Meters: `7 * 400 = 2800`
  - Kilometers: `2800 / 1000 = 2.8`
- Print the result in the following format:
  ```
  Kilometers: 2.8, Meters: 2800
  ```
- Make sure the output format is exactly the same. CodeGrade is matching your output with the expected output. Outputs with the correct answer but in a different format are incorrectly calculated by CodeGrade.

##### Example Input
```
Laps: 7
```

##### Example Output
```
Kilometers: 2.8, Meters: 2800
```
