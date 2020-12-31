# Practice: Conditionals Recap

## Directions

Complete these questions. Retry questions until you have the correct answer on each. Use any resource to answer these questions (including notes, other code, the Internet, assistance from others).

When you finish, write down any remaining questions you have in your notes, and bring them to class.

# Practice!

<!-- Question 1 -->
<!-- If -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 246422d2-e06a-4ed9-83e1-602e4acfaca8
* title: If Statements

##### !question

A grocery store's point of sale system generates notifications when an item reaches low inventory levels. For this example, the low inventory threshold is 10 units. Select the option that best describes the logic for this notification.

##### !end-question

##### !options

* 
```python

def check_inventory_level():
    if len(item) < 10:
        print(item + " is low in stock.")
```

* 
```python
def check_inventory_level():
    if len(item) <= 10:
        print(item + " is low in stock.")
```
* 
```python
def check_inventory_level():
    if len(item) == 10:
        print(item + " is low in stock.")
```

##### !end-options

##### !answer

* 
```python
def check_inventory_level():
    if len(item) <= 10:
        print(item + " is low in stock.")
```

##### !end-answer


#### !hint 
Make assumptions! There are several reasons why an item decreases in inventory. Think about whether the item count can be lower than the low inventory threshold.

#### !end-hint 
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 2 -->
<!-- If/else -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: b6ed651c-a170-47c6-a57f-d3e22e7e7f0d
* title: If Else Statement

##### !question

Netflix allows basic plan subscribers to stream on one device at a time. Which option would notify basic plan subscribers when they go over this limit?

##### !end-question

##### !options

* 
``` Python
def check_streaming_limit():
    if len(streaming_devices) > 1:
        print("Your Netflix account is in use on too many devices. Please stop playing on other devices to continue. Visit netflix.com/help for more information.")
    else:
        open_browse_page()
```

* 
``` Python
def check_streaming_limit():
    if len(streaming_devices) >= 1:
        print("Your Netflix account is in use on too many devices. Please stop playing on other devices to continue. Visit netflix.com/help for more information.")
    else:
        open_browse_page()
```

* 
``` Python
def check_streaming_limit():
    if len(streaming_devices) == 1:
        print("Your Netflix account is in use on too many devices. Please stop playing on other devices to continue. Visit netflix.com/help for more information.")
    else:
        open_browse_page()
```

##### !end-options

##### !answer

* 
``` Python
def check_streaming_limit():
    if len(streaming_devices) > 1:
        print("Your Netflix account is in use on too many devices. Please stop playing on other devices to continue. Visit netflix.com/help for more information.")
    else:
        open_browse_page()
```

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 3 -->
<!-- if elif else statements -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 4dd59372-ea02-4809-94fe-4fd42a4cb172
* title: If Elif Else

##### !question

Select the option that best describes how a smart car would behave when detecting a traffic light.

##### !end-question

##### !options

* 
``` Python
if traffic_light_color == "green":
    print("continue driving at current speed")
elif traffic_light_color == "red":
    print("reduce speed to stop")
elif traffic_light_color == "yellow":
    print("reduce speed by half and check traffic_light_color again")
else:
    print("prepare to reduce speed")
```

* 
``` Python
if traffic_light_color == "green":
    print("Tailgate car in front of you just in case the light turns yellow")
elif traffic_light_color == "red":
    print("Stop immediately")
elif traffic_light_color == "yellow":
    print("Initiate inner dialogue about whether to speed up before the traffic light turns red.")
else:
    print("Continue at current speed.")
```

* 
``` Python
if traffic_light_color = "green":
    print("continue driving at current speed")
elif traffic_light_color = "red":
    print("reduce speed to stop")
elif traffic_light_color = "yellow":
    print("reduce speed by half and check traff_light_color again")
else:
    print("prepare to reduce speed")
```

##### !end-options

##### !answer

* 
``` Python
if traffic_light_color == "green":
    print("continue driving at current speed")
elif traffic_light_color == "red":
    print("reduce speed to stop")
elif traffic_light_color == "yellow":
    print("reduce speed by half and check traffic_light_color again")
else:
    print("prepare to reduce speed")
```

##### !end-answer

##### !hint 

Always practice safe driving!

##### !end-hint
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 4 -->
<!-- if elif else -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 7e3a7cd7-4ae7-4cd9-9637-b736fe8539db
* title: If Elif Else Statements

##### !question

During holiday seasons, stores will often offer discounts based on membership tiers. Select the option that best describes the logic to create this discount system.

##### !end-question

##### !options

* 
``` Python
if membership_tier == "Basic":
    discount = .10
elif membership_tier == "Premium":
    discount = .15
elif membership_tier == "Platinum":
    discount = .20
else:
    print("Become a member and have access to discounts today! Terms and conditions will apply.")
```

* 
``` Python
if membership_tier = "Basic":
    discount = .10
elif membership_tier = "Premium":
    discount = .15
elif membership_tier = "Platinum":
    discount = .20
else:
    print("Become a member and have access to discounts today! Terms and conditions will apply.")
```

* 
``` Python
if membership_tier == "Basic":
    discount = .10
elif membership_tier == "Premium":
    discount = .15
elif membership_tier == "Platinum":
    discount = .20
else membership_tier == "None":
    discount = 0
```

##### !end-options

##### !answer

* 
``` Python
if membership_tier == "Basic":
    discount = .10
elif membership_tier == "Premium":
    discount = .15
elif membership_tier == "Platinum":
    discount = .20
else:
    print("Become a member and have access to discounts today! Terms and conditions will apply.")
```

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->


## Boolean Operations

<!-- Question 5 -->
<!-- if elif else -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 41ac7ae8-8b94-4305-8b05-40e0855fc00f
* title: If and

##### !question

Online-retailers often provide free shipping to members if their cart total reaches $100. Select the option that describes the logic to determine if a customer will receive free shipping or not.

##### !end-question

##### !options

* 
``` Python
if is_account_member and cart = $100:
    print("You are qualified for free shipping. Proceed to checkout.")
elif is_account_member is False and cart = $100:
    print("Sign up today for free shipping on your next order.")
else:
    print("Save on shipping by becoming a member and spending $100 on your order. Offer ends soon!")
```
* 
``` Python
if is_account_member and cart == $100:
    print("You are qualified for free shipping. Proceed to checkout.")
elif is_account_member is False and cart == $100:
    print("Sign up today for free shipping on your next order.")
else:
    print("Save on shipping by becoming a member and spending $100 on your order. Offer ends soon!")
```
* 
``` Python
if is_account_member and cart >= $100:
    print("You are qualified for free shipping. Proceed to checkout.")
elif is_account_member is False and cart >= $100:
    print("Sign up today for free shipping on your next order.")
else:
    print("Save on shipping by becoming a member and spending $100 on your order. Offer ends soon!")
```

##### !end-options

##### !answer

* 
``` Python
if is_account_member and cart >= $100:
    print("You are qualified for free shipping. Proceed to checkout.")
elif is_account_member is False and cart >= $100:
    print("Sign up today for free shipping on your next order.")
else:
    print("Save on shipping by becoming a member and spending $100 on your order. Offer ends soon!")
```

##### !end-answer

##### !hint

The is_account_member variable is a Boolean.

##### !end-hint

### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 6 -->
<!-- if elif else -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 744730ac-4364-42c7-84db-5d2951d08af2
* title: Boolean Practice

##### !question

Pretend you are a game developer for a new Mario Kart game. You are developing the game mechanic to unlock stages. In order for the player to unlock Peach's Castle, Mario needs to reach a skill level of 10 and earn at least 8 stars from previous stages. Which option best describes the conditional to build this feature?

##### !end-question

##### !options

* 
``` Python
if skill_level == 10 OR total_stars_count == 8:
    print("Peach's Castle is unlocked!")
else:
    print("Must reach level 10 and achieve 8 stars")
```
* 
``` Python
if skill_level >= 10 AND total_stars_count >= 8:
    print("Peach's Castle is unlocked!")
else:
    print("Must reach level 10 and achieved 8 stars")
```

* 
``` Python
if skill_level >= 10 OR total_stars_count >= 8:
    print("Peach's Castle is unlocked!")
else:
    print("Must reach level 10 and achieved 8 stars")
```

##### !end-options

##### !answer

* 
``` Python
if skill_level >= 10 AND total_stars_count >= 8:
    print("Peach's Castle is unlocked!")
else:
    print("Must reach level 10 and achieved 8 stars")
```
##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 7 -->
<!-- if elif else -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: 00216143-06ad-457e-b2aa-1d1dfd1e1a07
* title: Boolean Practice

##### !question

The Cinnamon Cinema prices movie tickets based on age, however, a new promotion is being implemented to reward individuals for pursuing an education, regardless of level. 

| Age Groups | Ticket Price|
|-----|-------------|
| Children 0-10 | $10 |
| Minors 11-17 | $13 |
| Adults 18+ | $15 |
| Seniors 60+ | $11 |

Which option best describes the logic to implement this pricing system?

##### !end-question

##### !options

* 
``` Python
if customer_age <= 10:
    ticket_price = 10.00
elif customer_age > 11 and customer_age <= 17:
    ticket_price = 13.00
elif customer_age >= 18 or customer_age < 60:
    ticket_price = 15.00
elif customer_age > 60:
    ticket_price = 11.00
else:
    print("please enter a valid age.")
```
* 
``` Python
if customer_age <= 10:
    ticket_price = 10.00
elif customer_age > 11 or customer_age <= 17:
    ticket_price = 13.00
elif customer_age >= 18 or customer_age < 60:
    ticket_price = 15.00
elif customer_age > 60:
    ticket_price = 11.00
else:
    print("please enter a valid age.")
```
* 
``` Python
if customer_age <= 10:
    ticket_price = 10.00
elif customer_age > 11 and customer_age <= 17:
    ticket_price = 13.00
elif customer_age >= 18 and customer_age < 60:
    ticket_price = 15.00
elif customer_age > 60:
    ticket_price = 11.00
else:
    print("please enter a valid age.")
```

##### !end-options

##### !answer

* 
``` Python
if customer_age <= 10:
    ticket_price = 10.00
elif customer_age > 11 and customer_age <= 17:
    ticket_price = 13.00
elif customer_age >= 18 and customer_age < 60:
    ticket_price = 15.00
elif customer_age > 60:
    ticket_price = 11.00
else:
    print("please enter a valid age.")
```

##### !end-answer
### !end-challenge
<!-- prettier-ignore-end -->

<!-- Question 8 -->
<!-- if elif else -->

<!-- prettier-ignore-start -->
### !challenge

* type: checkbox
* id: a61f06a0-94aa-4617-89a2-86f1217c8ef4
* title: Boolean practice

##### !question

Voice assistants like Alexa will turn on when their 'wake word' is announced nearby. Which option best describes this behavior?

##### !end-question
##### !options

* 
``` Python
if "alexa" in users_speech and "echo" in users_speech:
  print("processing your request...")
```
* 
``` Python
if "alexa" in users_speech or "echo" in users_speech:
  print("processing your request...")
```
* 
``` Python
if "alexa" == users_speech or "echo" == users_speech:
  print("processing your request...")
```

##### !end-options
##### !answer

* 
``` Python
if "alexa" in users_speech or "echo" in users_speech:
  print("processing your request...")
```

##### !end-answer
##### !hint 

`users_speech` is a string. 

##### !end-hint

##### !explanation

Alexa software requires at least one wake word in order to turn on and process requests. The `or` ensures that `print("processing your request...")` will execute if EITHER alexa or echo is used. `and` would require the user to say "Alexa echo" in order to turn on Alexa. 

##### !end-explanation
### !end-challenge
<!-- prettier-ignore-start -->
