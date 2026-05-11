# Import streamlit
import streamlit as st

# Import chatbot
from chatbot import CSVChatbot


# ======================================
# PAGE SETTINGS
# ======================================

st.set_page_config(
    page_title="AI CSV Assistant",
    page_icon="📊",
    layout="centered"
)

# ======================================
# TITLE
# ======================================

st.title("📊 AI-Powered CSV Assistant")

st.write(
    "Upload a CSV file and ask questions about your data."
)

# ======================================
# CHAT HISTORY
# ======================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================
# FILE UPLOAD
# ======================================

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# ======================================
# MAIN APP
# ======================================

if uploaded_file:

    # Save uploaded file temporarily
    with open("temp.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Create chatbot
    chatbot = CSVChatbot("temp.csv")

    # ==================================
    # BUTTONS
    # ==================================

    col1, col2 = st.columns(2)

    # Dataset Summary Button
    with col1:

        if st.button("📄 Summarize Dataset"):

            rows, cols = chatbot.df.shape

            summary = (
                f"This dataset contains "
                f"{rows} rows and {cols} columns."
            )

            st.info(summary)

    # Generate Chart Button
    with col2:

        if st.button("📊 Generate Salary Chart"):

            import matplotlib.pyplot as plt

            fig, ax = plt.subplots()

            ax.bar(
                chatbot.df["Name"],
                chatbot.df["Salary"]
            )

            ax.set_title("Salary Distribution")

            ax.set_xlabel("Employees")

            ax.set_ylabel("Salary")

            st.pyplot(fig)

    # ==================================
    # DISPLAY OLD MESSAGES
    # ==================================

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ==================================
    # CHAT INPUT
    # ==================================

    query = st.chat_input(
        "Ask something about your CSV..."
    )

    # ==================================
    # PROCESS QUESTION
    # ==================================

    if query:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        # Display user message
        with st.chat_message("user"):
            st.markdown(query)

        # Get chatbot answer
        answer = chatbot.ask(query)

        # Display assistant response
        with st.chat_message("assistant"):
            st.success(answer)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )