import streamlit as st
import random

st.set_page_config(page_title="Roast Engine", page_icon="🔥")

# Lists of taunts
savage_taunts = [
    "Tu itna bekaar hai, tujhe dekhke traffic signal bhi ignore kar deta hai.",
    "Tera IQ room temperature se bhi kam hai.",
    "Tujhse zyada value toh expired curd mein hoti hai.",
    "Tu toh vo error hai jo restart se bhi theek nahi hota.",
    "Tere jaise logon ki wajah se warning labels zaroori hote hain.",
    "Tu bina Google ke bhi dumb reh jaata hai.",
    "Tujhe toh dictionary mein bhi 'waste' ke example mein likhna chahiye.",
    "Tera wajood WhatsApp forward jaisa hai—bina kaam ka aur irritating.",
    "Tu zindagi ka glitch hai—fix hone ka naam hi nahi leta.",
    "Tera dimaag toh demo version pe chal raha hai bhai.",
]

vulgar_taunts = [
    "Tere jaise ch***ye logon ki wajah se hi internet slow chalta hai.",
    "Tera muh dekh ke toh kutton ka bhi bhukh mar jaata hai, bh***di.",
    "Tujhe dekhke lagta hai bhagwan bhi sochta hoga — 'kya ch***a banaya maine!'",
    "Tera dimaag toh har baar format hone ke baad bhi ch***ya hi rehta hai.",
    "Tu zindagi ka woh b**dk hai jisko sab ignore karte hain.",
]

# UI
st.title("🔥 Roast Engine – Anger Release Tool")
st.write("Kabhi kabhi gussa nikalna bhi zaroori hota hai...")

# Get user input
name = st.text_input("Bol Bhai Kis Pr Tujhe Gussa Aarha Hai?", placeholder="Uska Naam Likho Yahan")

level = st.radio(
    "Roast level choose kar:",
    options=["Non-Vulger", "Full-Vulger🌶️"],
    index=0
)

if name:
    roast_button = st.button("Roast Start karo 💢")

    if roast_button:
        taunt_list = savage_taunts if level == "Non-Vulger" else vulgar_taunts

        st.subheader(f"🔥 Gussa Nikalne Ka Time Hai! {name} Ki Bajane Wala Roast Start 🔥")

        for _ in range(3):
            st.write(f"💢 {name}, {random.choice(taunt_list)}")
