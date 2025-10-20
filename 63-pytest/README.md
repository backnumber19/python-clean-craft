## Case #63 - [Python] pytest

> 🧩 Reference: [LinkedIn Post](https://www.linkedin.com/posts/backnumber19lim_python-datascience-test-activity-7330465108311064576-tyaR?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC4i7ZsBMeUAH3UpBvhusYv1qkmTlPJ4E6E)  

pytest is a testing framework known for its simpler syntax compared to unittest(Case 23) and its wide range of plugins. It allows you to easily write test conditions using assert statements and supports the setup of multiple test cases through decorators like fixture and parametrize.

The images below show: the code that calculates one of the investment risk indicators called Maximum Drawdown (mddcalculator), the test code using pytest (test_mddcalculator), and the command-line output of running the tests.

1️⃣ mddcalculator

Maximum Drawdown (MDD) refers to the largest loss from a peak to a trough over a specific period within an asset's price history. It is implemented as a function called calc_mdd, which takes a list of prices and returns the MDD.

2️⃣ test_mddcalculator

After importing pytest and the calc_mdd function, test cases are constructed using the fixture and parametrize decorators. Fixture decorator allows the creation of reusable test data within the test script, while parametrize decorator enables the testing of multiple cases at once. Then, a function prefixed with test_ is defined to use assert statements to verify that the result of calc_mdd matches the expected MDD value.

3️⃣ Test Results

Tests are executed using the command start with 'pytest'. The -v (verbose) option displays the result of each test case. If any case fails, pytest shows exactly which assert statement failed and why.

While unittest is highly stable due to being part of the Python standard library, pytest has advantages in terms of features and development speed. Moreover, pytest supports various reporting plugins like pytest-html, offering mor

![pytest results](https://media.licdn.com/dms/image/v2/D4D22AQFecRjbr7quPw/feedshare-shrink_800/B4DZbsLKKlGwAo-/0/1747719073657?e=1762387200&v=beta&t=D1rANm8qdxIUCuAfhpwGJxQrgj4BiYN29ucTCw4ah1w)