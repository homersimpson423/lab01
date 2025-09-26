import streamlit as st

st.header("🍩 Homer Simpson Quiz 🍩")

st.write("Welcome to a fun BuzzFeed-style quiz all about Homer Simpson! "
         "Let's see how well you know Homer.")


st.subheader("1. Which food does Homer love the most?")
question1 = st.radio(
    "Choose one:",
    ["Pizza", "Donuts", "Burgers", "Cotton Candy"] #NEW
)


st.subheader("2. Which of these catchphrases belong to Homer?")
question2 = st.multiselect(
    "Select all that apply:",
    ["D’oh!", "Woo-hoo!", "Mmm...donuts", "I love you"] #NEW
)

st.subheader("3. How many hairs are on top of Homer’s head?")
question3 = st.number_input("Enter a number:", min_value=0, max_value=20) #NEW


st.subheader("4. On a scale of 1–10, how much does Homer love Donuts?")
question4 = st.slider("Slide to choose:", 1, 10)  #NEW


st.subheader("5. What is Homer’s favorite hobby?")
question5 = st.selectbox(
    "Please choose one:",
    ["Running", "Watching TV", "Painting", "Cooking"]  #NEW
)


st.image("Images/donuts.jpeg", caption="Mmm... Donuts!")  
st.image("Images/homer_duff.jpeg", caption="Homer and his favorite beer!")
st.image("Images/homer_watching_tv.jpeg", caption="Homer watching TV")


st.write("---")
st.subheader("Results")
if st.button("Submit"):  #NEW
    score = 0
    if question1 == "Donuts": score += 1
    if "D’oh!" in question2 and "Woo-hoo!" in question2 and "Mmm...donuts" in question2 and len(question2) == 3: score += 1
    if question3 == 2: score += 1
    if question4 >= 9: score += 1
    if question5 == "Watching TV": score += 1
    
    st.write(f"Your Score: {score}/5")

    if score == 5:
        st.balloons()  
        st.success("Perfect score!")
    elif score >= 3:
        st.info("You know Homer fairly well!")
    else:
        st.warning("Looks like you need to brush up on your Homer facts.")
