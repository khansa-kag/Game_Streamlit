#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import random

# Initialize session state variables if they don't exist
if 'secret_number' not in st.session_state:
    st.session_state['secret_number'] = random.randint(1, 50)
    st.session_state['attempts'] = 5

# Title and instructions
st.title('Number Guessing Game')
st.write("Welcome to 'Number Guessing Game'!")
st.write("Can you figure out the secret number hidden between 1 and 50?")
st.write("You have 5 attempts to guess it right.")
st.write("Good luck!")

# Input for user's guess
guess = st.number_input('Guess a number between 1 to 50', min_value=1, max_value=50, key='guess')

# Button to check the guess
if st.button('Submit'):
    if st.session_state['attempts'] > 0:
        if guess == st.session_state['secret_number']:
            st.success('Congratulations! You have guessed the number!')
            st.balloons()
            # Reset the game
            st.session_state['secret_number'] = random.randint(1, 50)
            st.session_state['attempts'] = 5
        elif guess < st.session_state['secret_number']:
            st.session_state['attempts'] -= 1
            st.error('Your guess is smaller than the secret number.')
        elif guess > st.session_state['secret_number']:
            st.session_state['attempts'] -= 1
            st.error('Your guess is bigger than the secret number.')

        if st.session_state['attempts'] == 0:
            st.error(f"You've run out of attempts! The number was: {st.session_state['secret_number']}")
            # Reset the game
            st.session_state['secret_number'] = random.randint(1, 50)
            st.session_state['attempts'] = 5
    else:
        # In case the attempts are somehow at 0, but the game has not been reset
        st.session_state['secret_number'] = random.randint(1, 50)
        st.session_state['attempts'] = 5
        st.info("A new game has started. Guess the number!")

# Display the number of attempts left
st.write(f"Attempts left: {st.session_state['attempts']}")

