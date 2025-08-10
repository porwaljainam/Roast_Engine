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
    "Tujhe dekhke toh log 'block' ka button dhundhte hain.",
    "Tu woh software update hai jisse sab kuch slow ho jata hai.",
    "Tera naam sunte hi mood off ho jata hai.",
    "Tu agar GPS hota toh sabko lost kar deta.",
    "Tere jaise logon ko toh charge bhi dena time ka waste hai.",
    "Tu toh ek walking red flag hai.",
    "Tera face dekhke toh mirchi bhi sharma jaaye.",
    "Tu jab bolta hai, toh lagta hai mute button invent kyun nahi hua tere liye.",
    "Tera attitude toh AirPods jaisa hai—mehenga bhi aur bekaar bhi.",
    "Tujhse milke lagta hai, insaan ka version rollback ho gaya hai."
]

vulgar_taunts = [
   "Tere jaise ch***ye logon ki wajah se hi internet slow chalta hai.",
    "Tera muh dekh ke toh kutton ka bhi bhukh mar jaata hai, bh***di.",
    "Tujhe dekhke lagta hai bhagwan bhi sochta hoga — 'kya ch***a banaya maine!'",
    "Tera dimaag toh har baar format hone ke baad bhi ch***ya hi rehta hai.",
    "Tu zindagi ka woh b**dk hai jisko sab ignore karte hain.",
    "Teri aukaat toh utni bhi nahi jitna ek expired p*rn site ka domain.",
    "Tu toh us g***u ka upgrade version hai jise duniya ne reject kiya hai.",
    "Tere jaise lo*de logo ko toh WiFi bhi password nahi deta.",
    "Tu bolta hai toh lagta hai ek ch***a TED Talk de raha ho.",
    "Tujh jaisa chutiya insaan ho hi nahi sakta — tu brand hai bro!",
    "Tera IQ toh negative mein hai, full g***u certified.",
    "Tu itna ch***ya hai ki agar stupidity Olympic hota toh gold medal pakka.",
    "Tujhe dekhke toh langoor bhi sochta hai, ‘main itna bhi bekaar nahi’",
    "Tera sense of humor wahi hai jo WhatsApp ke uncle forwards mein hota hai, ch***ya.",
    "Tujh mein dimaag dhoondhna matlab andhere mein mooh se torch jalana.",
    "Tera birth certificate sirf ek mazaak ka proof hai, bh***di.",
    "Tu woh ch***ya hai jisko Google pe bhi search karne se ‘No results found’ aata hai.",
    "Tere jaise bande ko toh log ‘delete for everyone’ ka real-life example bolte hain.",
    "Tu jab bhi bolta hai, ek ch***ye ka confidence sunai deta hai.",
    "Tere jaise lo*de ka brain lagta hai 2G pe chal raha hai abhi bhi."
]

# UI
st.title("🔥 Roast Engine – Anger Release Tool")
st.write("Kabhi kabhi gussa nikalna bhi zaroori hota hai...")

# Get user input
name = st.text_input("Bol Bhai Kis Pr Tujhe Gussa Aarha Hai?", placeholder="Uska Naam Likho Yahan")

if name == "jaianm":
   st.write("FUCK You")
   exit()
   
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
