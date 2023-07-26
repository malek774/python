class User():
    def __init__(self ,first_name ,last_name ,email ,age ,is_rewards_member= False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"first_name : {self.first_name}")
        print(f"last_name : {self.last_name}")
        print(f"email : {self.email}")
        print(f"age : {self.age}")
        print(f"is_rewards_member : {self.is_rewards_member}")
        print(f"gold_card_points : {self.gold_card_points}")
        print('---------------------------------------------')
        return self
    
    def enroll(self):
        if self.is_rewards_member == True :
            print('Your already a member')
            print('---------------------------------------------')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        if(self.gold_card_points > amount):
            self.gold_card_points-= amount
        else:
            print('Not Enough Points')
            print('---------------------------------------------')
        return self
    
    
    
user1 = User('kaabachi','abderrahim','abderrahimkaabachi@gmail.com',24)
user1.display_info().spend_points(20).enroll().spend_points(20).display_info().enroll()