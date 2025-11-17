from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request



app = Flask(__name__)

bot = ChatBot("chatbot", read_only=False,
              logic_adapters =[
                {
                  "import_path":"chatterbot.logic.BestMatch",
                  "default_response":"Sorry I dont have an answer",
                  "maximum_similarity_threshold": 0.9
                 
                 
                }
                 ])
bot10 = ChatBot("chatbot", read_only=False,
              logic_adapters =[
                {
                  "import_path":"chatterbot.logic.BestMatch",
                  "default_response":"Sorry I dont have an answer",
                  "maximum_similarity_threshold": 0.9
                 
                 
                }
                 ])
list_to_train =(
    "hi",
    "hi there",
    "what's your name?",
    "I'm a chatbot",
    "how old are you?",
    "I'm ageless"


)
#scholarship
list_to_train3 =(
"Open days"
"MONDAY TO SATURDAY"
"Scholarship form submit karne ke baad confirmation kaise milega?"
"Aapko college ki website ya scholarship office se form lena hoga. Required documents jaise mark sheets, income certificate, ID proof attach karke deadline se pehle submit karna hota hai."
"Form submit karne ke baad aapko ek receipt ya acknowledgment milta hai. Kuch colleges email ya student portal pe status update karte hain."
"Scholarship ke documents mein kya-kya lagta hai?"
"Usually aapko ye documents dene hote hain: 1. Last exam ki mark sheet 2. Income certificate 3.Aadhaar card 4.Bank passbook copy 5.Passport-size photo"
"Agar scholarship reject ho jaye to kya karna chahiye?"
"Scholarship office se reason puchhiye. Agar documents incomplete ya eligibility issue ho to aap next cycle mein dobara apply kar sakte hain."

"Admission confirmation letter kahan se milega?"
"College office ya registrar section se milta hai. Aapko admission slip aur ID proof dikhana hota hai."
"College ke official documents mein correction kaise karwayein?"
"Office mein ek correction form bharna hota hai. Sahi details ke proof ke saath submit karna padta hai, jaise Aadhaar ya 10th ki mark sheet."
"Exam form bharne ki last date kaise pata chalegi?"
"Notice board, college website, ya student WhatsApp group mein updates milte hain. Office se bhi confirm kar sakte ho."
"College se migration certificate kaise milega?"
"Ek written application deni hoti hai principal ke naam. Saath mein clearance form aur ID proof attach karna hota hai."

)
#office
list_to_train4 =(
  "Where can I get my college ID card?",
  "Visit the administrative office or student services desk. You may need to fill out a form and submit a passport-size photo and proof of admission. Some colleges also allow online ID card requests.",
  "How do I get a bonafide certificate from the college?",
  "Submit a written application to the college office or fill out the bonafide request form. Include your name, roll number, course, and purpose (e.g., for passport, bank, internship). Processing usually takes 2–5 working days.",
  "Where do I submit my scholarship documents?",
  "Submit them at the college’s scholarship or financial aid office. Make sure all documents are signed and verified. Some colleges also accept digital submissions via their student portal.",
  "How can I get a fee receipt or payment confirmation?",
  "Visit the accounts section of the college office. If you paid online, log in to the student portal and download the receipt from the “Payments” or “Transactions” section.",
  "What should I do if my name is spelled wrong on official documents?",
  "Report it immediately to the college office. You’ll likely need to submit a correction request form along with valid ID proof (like Aadhaar or PAN card) showing the correct spelling.",
  "How do I apply for a transfer certificate (TC)?",
  "Write an application to the principal or registrar requesting the TC. Attach your ID proof and any required clearance forms (library, hostel, etc.). The process may take a few days.",
  "Who should I contact for exam-related queries?",
  "Reach out to the examination cell or controller of examinations office. They handle exam schedules, admit cards, revaluation forms, and result-related issues.",
  "College ID card kahan se milega?",
  "Aapko administrative office ya student services desk pe jaana hoga. Wahan ek form fill karna padega aur passport-size photo aur admission proof dena hoga. Kuch colleges online ID request bhi accept karte hain.",
  "Bonafide certificate kaise milega?",
  "Aapko ek written application deni hogi ya bonafide request form bharna hoga. Apna naam, roll number, course aur certificate ka purpose mention karna zaroori hai. Processing mein 2–5 din lag sakte hain.",
  "Scholarship ke documents kahan submit karne hain?",
  "Scholarship ya financial aid office mein documents submit karne hote hain. Sabhi documents verified hone chahiye. Kuch colleges student portal ke through online submission bhi allow karte hain.",
  "Fee receipt ya payment confirmation kaise milega?",
  "Accounts section mein jaake receipt le sakte hain. Agar online payment kiya hai, to student portal pe login karke “Payments” section se receipt download kar sakte ho.",
  "Agar mere naam mein spelling galat hai to kya karun?",
  "Turant college office ko inform karein. Correction request form bharna hoga aur sahi spelling ka proof (jaise Aadhaar ya PAN card) submit karna padega.",
  "Transfer certificate (TC) ke liye kaise apply karna hai?: Principal ya registrar ko ek application likhni hoti hai. Saath mein ID proof aur clearance forms (library, hostel, etc.) attach karne hote hain. Process mein kuch din lag sakte hain.",
  "Exam-related queries ke liye kahan contact karna chahiye?",
  "Examination cell ya controller of examinations office se contact karein. Wahi log exam schedule, admit card, revaluation forms aur result-related issues handle karte hain."

)


list_trainer = ListTrainer(bot10)
#list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train4)
list_trainer.train(list_to_train3)
list_trainer.train(list_to_train)

@app.route("/")
def main():
   return render_template("index.html")
   
#while True: 
 # user_response = input("user :")
  #print("Chartbot: " + str(bot4.get_response(user_response)))

@app.route("/get")
def get_chatbot_response():
   userText = request.args.get('userMessage')
   return str(bot10.get_response(userText))


if __name__ == "__main__":
  app.run(debug=True)  