class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        # ! enrol without logic
    # def enroll(self):
    #     self.is_rewards_member=True
    #     self.gold_card_points=200
    def enroll(self,logic):
        self.is_rewards_member=logic
        self.gold_card_points=200 
        if self.is_rewards_member==True:
            print("User already a member")  
            return False 
        else:
            return True
        return self
    def spend_points(self, amount):
        self.gold_card_points-=amount
        return self
        
user_1=User("firas","rouine","rouine.firas@gmail.com",25)
# user_1.enroll() #!without logic 
user_1.enroll(False)
user_2=User("mhamed","monser","@gmail.com",25)
user_3=User("montasar","moussa","@gmail.com",25)
user_1.spend_points(50)
# user_2.enroll()#!without logic 
user_2.enroll(True)
user_2.spend_points(80)
user_1.display_info()
user_2.display_info()
user_3.display_info()
        