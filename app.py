import streamlit as st
import random

st.set_page_config(page_title="Roast Engine", page_icon="🔥")

# ----------------------------
# TAUNTS LISTS
# ----------------------------

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
    "Tujhse milke lagta hai, insaan ka version rollback ho gaya hai.",
    "Tera logic Windows Vista se bhi outdated hai.",
    "Tu Google Maps hota toh sabko jungle mein le jaata.",
    "Tere jokes se zyada stale toh last week ka bread hai.",
    "Tera brain buffering mode mein atka hua hai.",
    "Tere saath rehna matlab battery drain mode on karna.",
    # --------------------
    # EXTRA 50 SAVAGE TAUNTS
    # --------------------
    "Tera dimaag Windows XP update ka intezar kar raha hai.",
    "Tu woh YouTube ad hai jo skip bhi nahi hota.",
    "Tere ideas Ctrl+Alt+Del se bhi nahi aate.",
    "Tu life ka low-battery notification hai.",
    "Tere saath friendship karna system crash karne jaisa hai.",
    "Tu offline mode ka human version hai.",
    "Tera confidence ek expired sim card jaisa hai.",
    "Tu emojis ka bhi mood kharab kar deta hai.",
    "Tera sense of humor recycle bin mein milta hai.",
    "Tere saath time pass matlab wasted investment.",
    "Tera personality Windows error sound jaisa hai.",
    "Tu woh pop-up hai jo hamesha galat waqt pe aata hai.",
    "Tere saath baat karke bandwidth waste hota hai.",
    "Tu charger ke bina phone jaisa hai – useless.",
    "Tere dreams bhi buffering pe atke hue hain.",
    "Tu ek walking spam folder hai.",
    "Tere ideas ek broken pencil jaisa – pointless.",
    "Tu WhatsApp ke ‘last seen’ jaisa – irrelevant.",
    "Tere presence se WiFi signal kam ho jaata hai.",
    "Tu life ka ‘Page Not Found’ error hai.",
    "Tu PowerPoint ka slide without content hai.",
    "Tere jokes par crickets bhi silence ho jaate hain.",
    "Tu battery saver mode ka bhi downgrade hai.",
    "Tera kaam hamesha ‘loading’ pe atka rehta hai.",
    "Tu ek expired OTP ka human form hai.",
    "Tere words ek failed captcha jaisa hai.",
    "Tu ek app update jaisa hai jo sirf bugs laya hai.",
    "Tu calculator ka bhi wrong answer hai.",
    "Tera brain ek muted microphone jaisa hai.",
    "Tere ideas ek hidden file ki tarah useless hain.",
    "Tu ek broken link ka insaan hai.",
    "Tere saath kaam karna slow motion video jaisa hai.",
    "Tere decisions auto-correct ki galti se bhi bure hain.",
    "Tu ek uncharged power bank hai.",
    "Tere excuses ek slow download jaisa hai.",
    "Tere jokes se log airplane mode pe chale jaate hain.",
    "Tu ek fake loading bar ka insaan hai.",
    "Tere presence se Google bhi answer dena band kar deta hai.",
    "Tu ek 404 ka permanent version hai.",
    "Tere plans ek failed startup jaisa hai.",
    "Tu ek cloud storage without space hai.",
    "Tera brain ek frozen screen hai.",
    "Tere saath life safe mode me chalti hai.",
    "Tu ek app crash ka live demo hai.",
    "Tere liye motivation quotes bhi kaam nahi karte.",
    "Tu ek lagging game ka insaan hai.",
    "Tere decisions ek spam call jaisa hai.",
    "Tu ek unsaved document ka insaan hai.",
    "Tere ideas ek blank page jaisa hai."
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
    "Tere jaise lo*de ka brain lagta hai 2G pe chal raha hai abhi bhi.",
    "Tera chehra dekh ke toh mirror bhi depression mein chala jaata hai.",
    "Tere jaise g***u logon ki wajah se warning sirens lagte hain.",
    "Tere muh se nikalta har shabd stupidity ka certificate hota hai.",
    "Tere dimaag mein ideas utne hi rare hain jitne Sahara desert mein paani.",
    "Tu IQ test karega toh result 'file not found' aayega.",
    # --------------------
    # EXTRA 50 VULGAR TAUNTS
    # --------------------
    "Tere jaise chut*ye ko toh captcha bhi reject kar deta hai.",
    "Tera muh dekhke paint peel ho jaata hai.",
    "Tu zindagi ka pop-up porn ad hai.",
    "Tera brain ek virus infected pendrive hai.",
    "Tere jokes se condom factories band ho jaati hain.",
    "Tere saath time waste karna masturbation se bhi zyada useless hai.",
    "Tu ek lagging porn video ka human version hai.",
    "Tere muh se nikalta har shabd low quality meme hota hai.",
    "Tu ek unpaid electricity bill ka insaan hai.",
    "Tera face 'before plastic surgery fail' jaisa hai.",
    "Tu ek glitchy porn website ka pop-up hai.",
    "Tere jokes pe toh porn stars bhi sharminda ho jaate hain.",
    "Tu ek broken dildo ka insaan hai.",
    "Tere ideas condom ke bina sex jaisa – risky aur bekaar.",
    "Tu ek expired viagra tablet ka insaan hai.",
    "Tere saath deal karna STD lene jaisa hai.",
    "Tu ek buffering porn scene ka bekaar climax hai.",
    "Tere saath romance karna matlab 2G internet pe Netflix chalana.",
    "Tu ek bekar nightstand story ka hero hai.",
    "Tere muh se aati baatein bathroom graffiti level ki hoti hain.",
    "Tu ek stuck toilet flush ka insaan hai.",
    "Tere plans utne hi useless hain jitna waterproof towel.",
    "Tu ek ganda socks ka bundle hai.",
    "Tere saath baithna fart smell ka permanent source hai.",
    "Tu ek ch***ya auto-correct ka example hai.",
    "Tera attitude public toilet ke smell jaisa hai.",
    "Tere saath friendship ek bad date ka sequel hai.",
    "Tu ek penis enlargement spam email ka human form hai.",
    "Tere saath kaam karna condom ke bina rollercoaster ride hai.",
    "Tu ek XXX tape ka deleted scene hai.",
    "Tere jokes toh porn par bhi copyright strike lagwa de.",
    "Tere saath romance karna ek horror movie ka twist hai.",
    "Tu ek anus pimple ka insaan hai.",
    "Tera hairstyle ek drunk barber ka kaam hai.",
    "Tere ideas se bas diarrhea hi ho sakta hai.",
    "Tu ek cumshot fail ka live version hai.",
    "Tere muh se bas cringe leak hota hai.",
    "Tu ek fake orgasm ka acting master hai.",
    "Tere saath life ek public washroom experience hai.",
    "Tu ek porn site ka permanently down server hai.",
    "Tere dimaag mein sirf hentai ka plot hota hai.",
    "Tere muh se badbu condom factory ko band karwa de.",
    "Tu ek adult toy ka rejected design hai.",
    "Tera face ek STD awareness poster ka example hai.",
    "Tere jokes toilet tissue ki tarah flimsy hain.",
    "Tere saath time pass gonorrhea lene jaisa hai.",
    "Tu ek XXX parody ka flop hero hai."
]

# ----------------------------
# UI
# ----------------------------
st.title("🔥 Roast Engine – Anger Release Tool")
st.write("Kabhi kabhi gussa nikalna bhi zaroori hota hai...")

# Input
name = st.text_input("Bol Bhai Kis Pr Tujhe Gussa Aarha Hai?", placeholder="Uska Naam Likho Yahan")

# Jainam detection
if "jainam" in name.lower():
    st.markdown("**FUCK YOU**")
    st.stop()

# Roast level
level = st.radio("Roast level choose kar:", options=["Non-Vulger", "Full-Vulger🌶️"], index=0)

# Session state
if "roast_started" not in st.session_state:
    st.session_state.roast_started = False
if "name" not in st.session_state:
    st.session_state.name = ""
if "level" not in st.session_state:
    st.session_state.level = ""

# Start roast
if name:
    if st.button("Roast Start karo 💢"):
        st.session_state.roast_started = True
        st.session_state.name = name
        st.session_state.level = level

if st.session_state.roast_started:
    taunt_list = savage_taunts if st.session_state.level == "Non-Vulger" else vulgar_taunts
    st.subheader(f"🔥 Gussa Nikalne Ka Time Hai! {st.session_state.name} Ki Bajane Wala Roast Start 🔥")
    st.write(f"💢 {st.session_state.name}, {random.choice(taunt_list)}")

    # New taunt
    if st.button("Generate New Taunt 🔄"):
        st.write(f"💢 {st.session_state.name}, {random.choice(taunt_list)}")

    # Exit
    if st.button("Exit ❌"):
        st.session_state.roast_started = False
        st.success("Program Stopped!")
        st.stop()
