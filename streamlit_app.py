import streamlit as st
import pyttsx3
tts = pyttsx3.init()
st.title("welcom to calculator!")
st.write("hello develop by Surya VS!")
st.write("this is a my first web app!")
n1 = st.text_input("enter num1:", 0)
n2 = st.text_input("enter num2:", 0)
num1 = int(n1)
num2 = int(n2)
b1=st.button("add")
if b1:
 ans1 = num1+num2
 st.write("your ans: ", ans1)
 tts.say("your ans: "+str(ans1))
 tts.runAndWait()

b2=st.button("subtract")
if b2:
  ans2=num1-num2
  st.write("your ans: ", ans2)
  tts.say("your ans: "+str(ans2))
  tts.runAndWait()

b3=st.button("multiply")
if b3:
   ans3 = num1*num2
   st.write("your ans: ", ans3)
   tts.say("your ans: "+str(ans3))
   tts.runAndWait()

b4=st.button("divide")
if b4:
    ans4=num1/num2
    st.write("your ans: ", ans4)
    tts.say("your ans: "+str(ans4))
    tts.runAndWait()
