# Minimum Operations

This Python script calculates the fewest number of operations needed to result in exactly 'n' H characters in a text file. The text editor can execute only two operations: Copy All and Paste.

## Prototype

```python
def minOperations(n):
    """Returns an integer"""
```

## Requirements

- Python 3.6 or higher

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/alx-interview.git
```

2. Navigate to the directory:

```bash
cd alx-interview/0x02-minimum_operations
```

3. Run the script with desired 'n' value:

```bash
python3 0-main.py
```

## Example

```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Output

```bash
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```

## Note

- If 'n' is impossible to achieve, the script returns 0.

For any questions or feedback, feel free to contact [your-name](https://github.com/your-username).