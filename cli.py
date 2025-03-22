from openai_funcs import get_prd
from dotenv import load_dotenv
load_dotenv()

def boldtext(text):
	return f"\033[1m{text}\033[0;0m"

print(f"\n\n{boldtext('1. About Your Product')}")
a1 = input("\nProduct Name\n> ")
a2 = input("\nFeature Name\n> ")
a3 = input("\nGive an Overview/Explanation\n> ")

print(f"\n\n{boldtext('2. Define Your Requirement')}")
b1 = input("\nFeature List\n> ")
b2 = input("\nUser Feedback\n> ")

query = f"Write a PRD for a product named {a1} that {a3} with features including {a2}, {b1}{', for which the users 	have given feedback of' + b2 if b2 != '' else ''}"
print(f"\n\n{boldtext('Query')}\n>{query}")

prd = get_prd(query)
print("\n\n")
print(prd)