import streamlit as st

st.logo('resources/logo.png', size='large')

st.title('👨‍💻 About Us')

with st.container(border=True):
    "## Made By : "

    "### **Panchal Dev**"
    st.link_button("LinkedIn", "https://www.linkedin.com/in/dev-panchal-connect/", icon="🔗", use_container_width=True)
    st.link_button("GitHub", "https://github.com/DevPanchal2005", icon="🔗", use_container_width=True)

with st.container(border=True):
    "## GitHub Repository :"
    st.link_button("ConvoHub", "https://github.com/DevPanchal2005/ConvoHub", icon="🔗")

with st.container(border=True):
    """
    ## 🛠️ Technologies Used  
    - 📌 **Programming & Libraries :** Python 🐍, Streamlit, Pandas 📊, io, Pillow 🖼️ 
    - 💻 **IDE & Development :** VS Code 📝 
    - 🌍 **Version Control :** GitHub 🗄️ (Project Repository)  
    - 🤖 **Documentation Assistance :** ChatGPT 📝 (Generating Documentation) 
    - 📦 **Hosting Platform :** Streamlit Sharing 🌐 (Deployment)
    """