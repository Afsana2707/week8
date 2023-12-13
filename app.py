import streamlit as st

def find_largest(x, y, z):
    # Compare the three numbers
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

def main():
    st.title("Find the Largest Number App")

    # Input fields for three numbers
    number1 = st.number_input("Enter the first number", value=0)
    number2 = st.number_input("Enter the second number", value=0)
    number3 = st.number_input("Enter the third number", value=0)

    # Button to find the largest number
    if st.button("Find Largest Number"):
        largest_number = find_largest(number1, number2, number3)
        st.success(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
