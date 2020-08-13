### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total.  (or more)

```python

class CardGame:


  def checkforAce(self, card):                
    if card.value = 1:                        # Err0: should be ==
      return true                             # Err1: booleans should be Capitalised --> return: True
    else                                      # Err2: missing ':'
      return false                            # Err1: return: False

  dif highest_card(self, card1 card2)         # Err3: method should be initiated by 'def' not 'dif' , Err4: missing comma between parameters card1 & card 2, Err2: missing at end of ':'
    if card1.value > card2.value              # Err2 missing ':'
      return card                             # Err5: speling - should be: return card1 
    else                                      # Err2  missing ':'
      return card2
 

 def cards_total(cards):                      # Err6 indetation of method incorrect, Err7 missing self in parentheses
   total                                      # Err8: shoud be : total = 0
   for card in cards:
     total += card.value
     return "You have a total of" + total     # Err8: cannot concatenate differet value types- should be f"You have a total of" {total}", Err9: Return statement indented incorrectly, should be aligned to for loop start.


```
