import streamlit as st
import random
import sys

st.set_page_config(page_title="Roast Engine", page_icon="🔥")

# Combined Taunts
savage_taunts = [
    # Original 20
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
    # +50 more
    "Tu utna useful hai jitna underwater umbrella.",
    "Tere ideas toh expired memes jaise hain.",
    "Tujhe dekhke lagta hai universe ka bug fix hona baaki hai.",
    "Tera logic Windows Vista jaise slow hai.",
    "Tu vo auto-reply hai jo hamesha wrong hota hai.",
    "Tere jokes sunke crickets bhi so jaate hain.",
    "Tu toothpaste ka cap lose karne wala insan hai.",
    "Tere presence se WiFi ka signal kam ho jata hai.",
    "Tera self-esteem free trial pe chal raha hai.",
    "Tu vo buffering circle hai jo kabhi khatam nahi hota.",
    "Tere actions Ctrl+Z se bhi undo nahi hote.",
    "Tu utna rare hai jitna working government office phone line.",
    "Tera brain single-core processor pe chal raha hai.",
    "Tu vo pop-up ad hai jo sabko irritate karta hai.",
    "Tere advice ka value spam folder jaisa hai.",
    "Tujhe dekhke lagta hai common sense extinct ho gaya hai.",
    "Tere expressions low battery icon jaise hain.",
    "Tu vo playlist hai jisme bas skip-worthy songs hain.",
    "Tera style Windows 98 wallpaper jaisa hai.",
    "Tu utna reliable hai jitna rainy season ka umbrella.",
    "Tera existence ek unwanted app update jaisa hai.",
    "Tere answers 404 error jaise hain.",
    "Tu vo alarm hai jo kabhi ring nahi karta.",
    "Tera kaam half-downloaded file jaisa hai.",
    "Tere decisions coin toss se bhi bekaar hain.",
    "Tu vo keyboard key hai jo kabhi kaam nahi aati.",
    "Tera attitude USB 1.0 speed pe chal raha hai.",
    "Tere skills photocopy machine pe jam hua paper jaise hain.",
    "Tu vo notification hai jo sirf tension deta hai.",
    "Tere excuses recycled tissue paper jaise hain.",
    "Tera focus cricket match ke rain delay jaisa hai.",
    "Tu vo app hai jo phone slow kar deta hai.",
    "Tera contribution group project me zero hota hai.",
    "Tere plans expired milk jaisa kaam karte hain.",
    "Tu vo password hai jo hamesha galat hota hai.",
    "Tera attention span TikTok video se bhi short hai.",
    "Tere efforts software bug jaise hain—fix hone ke baad bhi problem.",
    "Tu vo elevator music hai jo bas bore karta hai.",
    "Tera impact wet tissue paper jaise hai.",
    "Tere promises Windows update ke restart time jaise hain.",
    "Tu vo charger hai jo sirf 2% charge deta hai.",
    "Tere arguments Bluetooth pairing error jaise hain.",
    "Tu vo cloud storage hai jo hamesha full hota hai.",
    "Tera output misprint newspaper jaisa hai.",
    "Tere responses spam call se bhi irritating hote hain.",
    "Tu vo search result hai jo irrelevant hota hai.",
    "Tere failures calendar reminder ban jaate hain.",
    "Tu vo elevator button hai jo kaam nahi karta.",
    "Tera logic magic trick ka fail version hai.",
    "Tere attempts slow internet ke page load jaisa hai."
]

vulgar_taunts = [
    # Original 20 vulgar ones
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
    # +50 more vulgar
    "Tera dimaag lagta hai download ke beech mein stuck ho gaya.",
    "Tu vo porn pop-up hai jo bandh hi nahi hota.",
    "Tere muh se nikalte hi words cancer ban jaate hain.",
    "Tera sense of style gali ke kachre se bhi ganda.",
    "Tu zindagi ka laggy server hai.",
    "Tere jokes sunke dustbin bhi ro deta hai.",
    "Tera dimaag g***u processor pe chal raha hai.",
    "Tere muh se badbu nikalti hai jaise expired samosa.",
    "Tere ideas utne bekaar hain jitna broken condom.",
    "Tu us b***d ka beta hai jisko network kabhi nahi milta.",
    "Tere liye insult words kam pad jaate hain.",
    "Tu itna slow hai ki snails bhi tujhe overtake karein.",
    "Tera muh ek permanent glitch hai.",
    "Tere actions g***u ka proof hain.",
    "Tu ek walking malware hai.",
    "Tere liye delete ka button banaya gaya.",
    "Tere existence se internet ka bandwidth waste hota hai.",
    "Tu ek gali ka upgraded version hai.",
    "Tera logic chut* ke example mein hota hai.",
    "Tu ek porn ad ka bhi reject version hai.",
    "Tere muh ka structure lagta hai crash hogaya.",
    "Tere actions ka result sirf disappointment hota hai.",
    "Tu ek live virus hai jo sabko irritate karta hai.",
    "Tere jokes toilet flush jaise hain.",
    "Tu ek permanent lag ka icon hai.",
    "Tere muh ka kaam sirf bakwaas nikalna hai.",
    "Tu ek la*de ka sample hai.",
    "Tere ideas kabhi load nahi hote.",
    "Tere presence se vibe khatam ho jaati hai.",
    "Tu ek b**dk ka best example hai.",
    "Tere liye dictionary mein alag gaali banani padegi.",
    "Tu ek STD ka meme hai.",
    "Tere muh ki shape failed emoji jaise hai.",
    "Tu ek accident ka upgraded version hai.",
    "Tere liye restart ka option bhi kaam nahi karta.",
    "Tu ek permanent disappointment hai.",
    "Tere actions poora system crash kar dete hain.",
    "Tu ek porn buffering screen hai.",
    "Tere muh ka scene ganda filter lagake nikala gaya hai.",
    "Tu ek ch***ya ka deluxe pack hai.",
    "Tere muh ka screenshot leak ho jaye toh log net bandh kar denge.",
    "Tu ek ganda caption ka live version hai.",
    "Tere muh se gaali bhi insult lagti hai.",
    "Tu ek la*de ka bhai hai.",
    "Tere liye insult quota khatam ho gaya.",
    "Tu ek g***u ka overhyped edition hai.",
    "Tere muh ka update kabhi release nahi hota.",
    "Tu ek porn ban ka reason hai.",
    "Tere muh ki lighting permanent blackout hai."
]

# UI
st.title("🔥 Roast Engine – Anger Release Tool")
st.write("Kabhi kabhi gussa nikalna bhi zaroori hota hai...")

# Input
name = st.text_input("Bol Bhai Kis Pr Tujhe Gussa Aarha Hai?", placeholder="Uska Naam Likho Yahan")

# Jainam check (case-insensitive)
if name and "jainam" in name.lower():
    st.markdown("**FUCK YOU**")
    st.stop()

level = st.radio(
    "Roast level choose kar:",
    options=["Non-Vulger", "Full-Vulger🌶️"],
    index=0
)

# Session state for taunts
if "taunts" not in st.session_state:
    st.session_state.taunts = []

def generate_taunts():
    taunt_list = savage_taunts if level == "Non-Vulger" else vulgar_taunts
    st.session_state.taunts = random.sample(taunt_list, 3)

if name:
    if st.button("Roast Start karo 💢"):
        generate_taunts()

    if st.session_state.taunts:
        st.subheader(f"🔥 Gussa Nikalne Ka Time Hai! {name} Ki Bajane Wala Roast Start 🔥")
        for t in st.session_state.taunts:
            st.write(f"💢 {name}, {t}")

        if st.button("Generate New Taunts 🔄"):
            generate_taunts()
            st.rerun()

        if st.button("Exit ❌"):
            sys.exit()
