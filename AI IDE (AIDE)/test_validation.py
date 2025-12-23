
import sys
import os

# Add agents directory to path
sys.path.append(os.path.join(os.getcwd(), 'agents'))

from chat_agent import validate_calculator_logic

with open('calculator_test.py', 'r') as f:
    code = f.read()

print("Original Code:")
print(code)
print("-" * 20)

validated_code = validate_calculator_logic(code, 'calculator_test.py')

print("Validated Code:")
print(validated_code)

if "num1 = 0" in validated_code and "num2 = 0" in validated_code and "mainloop()" in validated_code and "main()" in validated_code:
    print("-" * 20)
    print("SUCCESS: All validation checks passed!")
else:
    print("-" * 20)
    print("FAILURE: Some validation checks failed.")
    if "num1 = 0" not in validated_code: print("Missing num1 init")
    if "num2 = 0" not in validated_code: print("Missing num2 init")
    if "mainloop()" not in validated_code: print("Missing mainloop")
    if "main()" not in validated_code: print("Missing main call")
