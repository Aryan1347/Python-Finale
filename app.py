import streamlit as st
from main import Bank

bank = Bank()
st.title("🏦 Python Bank Management System")

menu = [
    "Create Account", "Deposit", "Withdraw", "View Details", "Update Details", "Delete Account"
]
choice = st.sidebar.selectbox("Choose an Operation", menu)

if choice == "Create Account":
    st.subheader("🆕 Create New Account")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0)
    email = st.text_input("Enter your email")
    pin = st.text_input("Set 4-digit PIN", max_chars=4, type="password")
    if st.button("Create Account"):
        success, msg = bank.create_account(name, age, email, pin)
        if success:
            st.success("Account created!")
            st.json(msg)
        else:
            st.error(msg)

elif choice == "Deposit":
    st.subheader("💰 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=0)
    if st.button("Deposit"):
        success, msg = bank.deposit_money(acc, pin, amt)
        st.success(f"Balance: ₹{msg}") if success else st.error(msg)

elif choice == "Withdraw":
    st.subheader("💸 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=0)
    if st.button("Withdraw"):
        success, msg = bank.withdraw_money(acc, pin, amt)
        st.success(f"Balance: ₹{msg}") if success else st.error(msg)

elif choice == "View Details":
    st.subheader("📄 View Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("View"):
        success, data = bank.view_details(acc, pin)
        st.json(data) if success else st.error(data)

elif choice == "Update Details":
    st.subheader("✏️ Update Account Info")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", max_chars=4, type="password")
    if st.button("Update"):
        success, msg = bank.update_details(acc, pin, name, email, new_pin)
        st.success("Details updated!") if success else st.error(msg)

elif choice == "Delete Account":
    st.subheader("⚠️ Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete Account"):
        success, msg = bank.delete_account(acc, pin)
        st.success(msg) if success else st.error(msg)
