'''  HackerMan has a message in form of digits but he wants to decode the message so that if enemies gets hold of the message they will not be completely able to decode the message.

Since the message consists only of number, So decoding involves reversing the number. The first digit becomes last and vice versa. For example, if there is 1245 in the code, it becomes 5421 now.

Note : All the leading zeros are omitted. That means if the number ends with a zero, the zero is lost by reversing (e.g. 1200 gives 21).

HackerMan is further thinking of complicating the process and he needs your help. Your task is to add the numbers after reversing and output the result after reversing the sum.

Input

The input consists of N cases. The first line of the input contains only positive integer N. Then follow the cases. Each case consists of exactly one line with two positive integers separated by space. These are the reversed numbers you are to add.

Output

For each case, print exactly one line containing only one integer - the reversed sum of two reversed numbers. Omit any leading zeros in the output.

Constraints

The value of N will be less than 10000.
The value of digits will be less than 5000.
Sample Input(Plaintext Link)
 3
24 1
4358 754
305 794
Sample Output(Plaintext Link)
 34
1998
1
Explanation
There are 3 test cases in the sample input. Following it are three lines that contains two numbers each, so the output also contains three lines that contain the reverse of the sum of the two reversed numbers.

In first Test case : 24 and 1 are reversed and added and finally reversed -> 42 + 1 -> 43 -> 34 '''

while True:
	try:
		T = raw_input()
		for t in range(9999):
	
			a,b = raw_input().split()
			total = str(int(a[::-1]) + int(b[::-1]))
			print int(total[::-1].lstrip("0"))
		
	except (EOFError):
		break
	



