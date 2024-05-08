import re
import random

class RuleBot:
    # Negative responses
    negative_responses = ("no", "nope", "nah", "sorry", "not a chance")
    # Exit keywords
    exit_commands = ("quit", "pause", "exit", "bye", "goodbye", "later")
    # Random questions starter
    random_questions = (
        "why are you here?",
        "what do you do?",
        "what did you eat today?",
        "where did you travel recently?",
        "what technology do you love more?",
        "do you play games?",
        "which is your favourite movie?"
    )  
    def __init__(self):
        self.alienbabble = {
            'describe_about_you': r'.*\s*who\sare.*',
            'answer_why_intent': r'why\sare.*',
            'about_techlanders': r'.*\s*techlanders'
        }

    def greet(self):
        self.name = input("what is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am a rulebot. Will you help me learn about yourself?\n")
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice day")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_about_you':
                return self.describe_about_you()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_techlanders':
                return self.about_techlanders()
        if not found_match:
            return self.no_match_intent()

    def describe_about_you(self):
        responses = ["My name is RuleBot and I am here to help you out",
                     "Hey Rulebot here and Sandeep has designed me"]
        return random.choice(responses)

    def answer_why_intent(self):
        responses = ["I come in gather knowledge",
                     "I am here to help you to solve your problems",
                     "I heard you India is a beautiful country"]
        return random.choice(responses)

    def about_techlanders(self):
        responses = ["Techlanders is the world's largest professional educational company",
                     "It helps people to upskill their knowledge base",
                     "Techlanders is where your career and skills grow"]
        return random.choice(responses)

    def no_match_intent(self):
        responses = ["tell me more",
                     "please tell me more",
                     "Why do you say that",
                     "Can you elaborate more",
                     "I see, how do you think",
                     "why",
                     "how do you think I feel when you say that?"]
        return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet()
