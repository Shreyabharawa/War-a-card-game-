#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Card
#Suit , Rank, Value
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':1}


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return  self.rank   +  " of "  +   self.suit


# In[3]:


three_of_clubs = Card("Clubs",'Three')


# In[4]:


three_of_clubs


# In[ ]:





# In[ ]:





# In[57]:


two_hearts = Card("Hearts","Two")


# In[58]:


two_hearts


# In[59]:


print(two_hearts)


# In[60]:


two_hearts.suit


# In[61]:


two_hearts.rank


# In[62]:


two_hearts.value == three_of_clubs.value


# In[63]:


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #created the card object
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# In[64]:


mydeck = Deck()


# In[65]:


len(mydeck.all_cards)

mydeck.all_cards[0]
# In[66]:


print(mydeck.all_cards[0])


# In[67]:


mydeck.shuffle()


# In[68]:


print(mydeck.all_cards[0])


# In[69]:


my_card = mydeck.deal_one()


# In[70]:


print(my_card)


# In[ ]:





# In[71]:


class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #list of multiple card obj
            self.all_cards.extend(new_cards)
        else:
            #list of single card obj
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[72]:


jose = Player("Jose")


# In[73]:


jose


# In[74]:


print(jose)


# In[75]:


two_hearts


# In[76]:


jose.add_cards(two_hearts)


# In[77]:


print(jose)


# In[78]:


two_hearts


# In[79]:


jose.add_cards(two_hearts)


# In[80]:


jose.add_cards([two_hearts,two_hearts,two_hearts])


# In[81]:


print(jose)


# In[82]:


len(mydeck.all_cards)


# In[83]:


player_one = Player ("One")


# In[ ]:





# In[84]:


#Game Setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    


# In[ ]:





# In[85]:


import pdb
game_on = True


# In[86]:


round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


# In[ ]:





# In[ ]:





# In[ ]:




