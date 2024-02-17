import streamlit as st
st.title("Welcome to the game")
s1=st.text_input("Enter the name: ")
s2=st.text_input("Enter the name :")
s1=list(s1)
s2=list(s2)
s="FLAMES"
res=["Friends","Lovers","Affectionate","Marriage","Enimies","Siblings"]
for i in range(len(s1)):
    for j in range(len(s2)):
        if (s1[i]==s2[j]):
            s1[i]='0'
            s2[j]='0'
            break
count=0
for i in s1+s2:
    if i!='0':
        count+=1


while len(res)>1:
    split=(count % len(res)-1)
    if split>0:
        right=res[split +1:]
        left=res[:split]
        res =right+left
    else:
        res=res[:len(res)-1]
        
if st.button('Submit'):
    st.success(res[0])
        
        
        

    
    
    