import re
import random
class RuleBot:
    ###Potential negetive responses
    negetive_responses=("no","nope","not a chance","sorry","nah","naw")
    
    ###Exit conversation responses
    exit_commands=("quit","pause","exit","goodbye","bye","later")
    
    random_questions=("Why are you here?","Are there many humans like you","What do you consume for sustanance","Is there intelligent life on this planet?","Does earth have a leader?","What planet have you visited?","What technology do you have on this planet?")
     
        
    def __init__(self):
        self.alienbabble = {'describe_planet_intent':r'.*\s*your planet.*','answer_why_intent':r'why\sare.*','about_intellipat':r'.*\s*intellipaat'}
     
    def greet(self):
        self.name = input("What is your name")
        will_help = input(
            f"Hi {self.name}, I am Rule-Bot. Will you help me learn about the planet?\n")
        if will_help in self.negetive_responses:
                print("OK, have a nice earth day")
                return
        self.chat()
        
    
    def make_exit(self,reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice day")
                return True
    
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    def match_reply(self,reply):
        for key,value in self.alienbabble.items():
            intent=key
            regex_pattern = value
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about intellipat':
                return self.about_intellipat()
            
        if not found_match:
            return self.no_match_intent()
        
    
    def describe_planet_intent(self):
        responses = ("My planet is a utopia of diverse organisms and species.\n",
                    "I am from Opidipous, the capital of Tasmin Galaxy.\n")
        return random.choice(responses)
    
    
    def answer_why_intent(self):
        responses = ("I come in peace\n","I am here to collect data on your planet and its inhabitants\n",
                    "I heard the coffee is good\n")
        return random.choice(responses)
    
    def about_intellipat(self):
        responses=("Intellipat is world's largest campus\n")
        return random.choice(responses)
    
    def no_match_intent(self):
        responses = (
        "Please tell me more\n","Tell me more\n","Why do you say that?\n","I see\n","Can you elaborate\n","Interesting can you tell me more\n",
        "Why\n","How do you think?\n"
        )
        return random.choice(responses)
    
AlienBot = RuleBot()
AlienBot.greet()