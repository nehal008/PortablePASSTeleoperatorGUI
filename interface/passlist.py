class Passlist:
# A class that contains the dictionary for the pass tasks

	def __init__(self):

		self.passlist = {
            
            'allPass' : {
                'Chat': [
                    'Sure',
                    'Alright',
                    'Okay',
                    'Great']
                },
			'pass1' : {
				"ParticipantName, let's start the grocery shopping task by finding items on a shopping list.": {
					'RemindSupport':[],
					'Redirect':[]
				},
                'Here is a grocery list. Please select the items on the list from the table.': {
					'RemindSupport':[],
					'Redirect':[]
				},
                'Would you like the instructions repeated? Or would you like the instructions to be louder?': {
                    'RemindSupport': [
                        'Can you check to see if you are correct?', 
                        "ParticipantName, I'll read the list for you. We need to find a box of broccoli, a box of green peas, a box of spinach, and a box of green beans. Let's start by looking for the box of broccoli together.",
                        "Now, let’s find the green peas.", 
                        'Next, we need to find the spinach.',
                        "Finally, let’s look for the green beans."],
   					'Redirect': [
                           'How are you doing? Do you need any help?', 
                           "You're doing a great job, ParticipantName. It's okay to take your time and ask for help if you need it. We'll work together to find all the items on the list", 
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Great job finding the groceries.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'The next shopping task is to pay for the groceries.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Here is a receipt for the 4 items and a wallet.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Use the wallet money to pay the exact amount for the groceries.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like to hear the instructions again?': {
                    'RemindSupport':[
                        'First, look at the receipt and find the total amount. Next, count the money in the wallet. Finally, give the money to the researcher to pay for the items.',
                        "Let's add up the cost of the 4 items",
                        "The total cost is $2.82. we need to pay the exact amount using the money in the wallet."],
   					'Redirect':[
                           'How are you doing? Do you need any help?',
                           "You're doing a great job, ParticipantName. It's okay to take your time and ask for help if you need it. We will work together to find the correct money in the wallet.",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'The next shopping task uses coupons.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Here are several food coupons in this envelope.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Check to see if any coupons match the items you purchased.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'If they do, use the coupons and this money to pay for just the coupon items. The researcher will give you change.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like the instructions repeated? Would you like them to be read together?': {
                    'RemindSupport':[
                        'Can you check again to see if you are correct?',
                        "First, let's look for coupons that match our items. Then, let's pay for the coupon items using the money and coupons.",
                        "Let's look at the items together and see if any of them match the coupons. This coupon is for Brand A Chopped Broccoli. Do we have that item?",
                        "Let’s check to see if we have coupons for the other grocery items."],
   					'Redirect':[
                           'Do you need any help? For example, would a calculator or a pen and paper be helpful?',
                           "You're doing a wonderful job. Remember, it's okay to take your time and ask for help if you need it. We'll get through this task together.",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Excellent use of the coupons.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Here is your change. Did you get the correct change?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'How much change should you have gotten?': {
                    'RemindSupport':[
                        "Let’s make sure you have the right change. Can you count the change in your hand for me?",
                        'Would you like to use a calculator or paper and pen?'],
   					'Redirect':[
                           'How are you doing? Do you need any help?',
                           "You're doing a wonderful job. Remember, it's okay to take your time and ask for help if you need it. We'll work together to make sure you have the right change.",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'The shopping task is done. Thank you for your work.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like a break or some water?': {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},

			'pass2' : {
                'ParticipantName, the next task is to pay bills by check.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Pay the 2 utility bills using the checks given by the researcher.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "Please write checks for both bills. Please use today's date.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'An extra check is available if needed.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'If there are other items, like a pen or calculator, you usually use when you pay bills, feel free to use them.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like to hear the instructions again?': {
                    'RemindSupport':[
                        "Remember, ParticipantName, we're paying your utility bills by writing checks today. Here are the bills and your checkbook.",
                        "Let me guide you through filling out the check. First, write today's date here. Today is CurrentMonth CurrentDate, CurrentYear. Next, write the utility company's name on the 'Pay to the Order of' line. Then, write the amount in numbers and words. Finally, sign the check at the bottom.",
                        "The payee is the name of the company you're paying. For the electricity bill, it's 'XYZ Electric.' The amount due is $50. You can write 'Fifty dollars and 00/100' in the amount section."],
   					'Redirect':[
                           "It's okay if something went wrong. We have extra checks. Just take a new one and start again.",
                           'Sometimes check writing is hard. Do you need help with anything, such as writing in the amounts?',
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "•	Let’s skip the current step and continue."]
                },
                "'You've paid the first bill, the water bill. Now let's pay the electric bill using another check.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Great job writing the checks! Both bills are paid now.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "We can move on to the next activity or take a break if you'd like. Thank you for your work.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Great. Now, let’s proceed to the next task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},
            
            'pass3' : {
                'ParticipantName, we are going to practice using the telephone to get information.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Please call the drugstore to find their closing time for tomorrow. The number is on this paper.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like the instructions repeated?': {
                    'RemindSupport':[
                        "We are calling the drugstore to find out their closing time for tomorrow. When someone answers, you can ask, 'What time do you close tomorrow?'",
                        "ParticipantName, let me help you with dialing the number. Let's go through the numbers one by one, and I'll guide you."],
   					'Redirect':[
                           'Do you need any help?',
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Good, you have the number.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Can you please tell me what time they said they close tomorrow?': {
                    'RemindSupport':[
                        "Let's try again. Please ask them to repeat the closing time for tomorrow, or the researcher can help you with the call if you'd like.",
                        "ParticipantName, if you didn't hear or understand what they said, asking them to repeat the information is okay. You can say, 'Can you please repeat the closing time for tomorrow?'"],
   					'Redirect':[
                           "It's all right if you don't remember the exact time. I was listening, and they said the closing time for tomorrow is 9 PM.",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Great, you got the closing time.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Great job completing the task. Thank you.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},

			'pass4' : {
                'ParticipantName, we are going to look at how you would organize and keep track of your medicines.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have two bottles: Bottle 1 and Bottle 2.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Let’s start with Bottle 1.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Please read the prescription label on Bottle 1. Look at the instructions for taking this medication.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'If you were taking this medication today, when would you take the next pill?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like to hear the instructions again? or would you like the instructions to be louder?': {
                    'RemindSupport':[
                        'Today is the CurrentDay, and the time is CurrentHour AMPM. When do you think you should take the next pill?',
                        'I see that the label might be difficult to read. Would you like me to read it out loud for you?',
                        "The instructions say to take this medication 2 with breakfast, 1 with lunch, and 1 with dinner. Let's do this together. If you were to take it now, when would be the next time you'd need to take it?",
                        'Do you need any more clarification?'],
   					'Redirect':[
                           "Do you need any help? Would you like a break or some water?",
                           "ParticipantName, indeed, managing medications can be quite a task. How about we take a short break and then give it another shot? I am here to help you",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Great job. You figured out when to take the next pill.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "OptionalSay: That's okay.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'The next task involves organizing the medicine.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Here is a medication organizer.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'This medication organizer has the days of the week across the top and the time of the day along the side.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Using the organizer, please put the pills to be taken tomorrow and the day after tomorrow in the correct boxes.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like the instructions repeated? or would you like the instructions to be louder?': {
                    'RemindSupport':[
                        "Today is CurrentWeekDay. Let's organize your medication for tomorrow and the day after tomorrow.",
                        "Let's double-check the organizer to make sure each pill is in the right box. Here, we should have the 2 pills for tomorrow’s breakfast, 1 for tomorrow’s lunch, and 1 for tomorrow’s dinner. Similarly, we should have 2 pills for the following day’s breakfast, 1 for lunch, and 1 for dinner.",
                        "I understand that this organizer might look confusing. Let’s look at it again. The days of the week are written across the top of the paper, and the times of the day are along the side. Each box gives a specific day and time when you need to take your medication."],
   					'Redirect':[
                           "Take your time, and carefully place each pill in the appropriate time slot. If you need help, I'm here to assist you.",
                           "Let's take a moment to regroup, and then we can continue organizing your medication.",
                           "Let’s skip the current step and continue."]
                },
                "OptionalSay: Good work, ParticipantName! You've successfully organized your medicine for the next couple of days.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "OptionalSay: That's completely fine.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Now, please get Bottle 2.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Please read the prescription label on Bottle 2. Then, find the instructions for taking this medication.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'If you were taking this medication today, when would you have to take the next pill?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like to hear the instructions again?': {
                    'RemindSupport':[
                        'Today is CurrentWeekDay, and the time is CurrentHour AMPM. When do you think you should take the next pill?',
                        'I see that the label might be difficult to read. Would you like me to read it out loud for you?',
                        "The instructions say to take 1 pill with lunch and 1 pill at bedtime. Let's do this together. If you were to take this one pill now, when would be the next time you'd need to take it?",
                        'Do you need any more clarification?'],
   					'Redirect':[
                           'Do you need any help? ',
                           "ParticipantName, Gosh, managing medications is hard. Let's take a break, then we can do this together and try again. I am here to help you.",
                           "Let’s skip the current step and continue."]
                },
                'Again, put the pills to be taken tomorrow and the following day in the correct boxes.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
				'Would you like the instructions repeated?': {
					'RemindSupport':[
                        "Let's go over them again. We need to put the pills to be taken tomorrow and the day after tomorrow in the correct boxes based on the day and time.",
                        "Let's double-check the organizer to make sure each pill is in the right box. Here, we should have 1 pill for tomorrow’s lunch and 1 pill for tomorrow’s bedtime. Next, we should have 1 pill for the following day’s lunch and 1 pill for the following day’s bedtime.",
                        "I understand that this organizer might look confusing. Let me explain it again. The days of the week are written across the top, and the times of the day are along the side. Each box has a specific day and time when you need to take your medication."],
					'Redirect':[
                        "Take your time, and carefully place each pill in the right time slot. If you need help, I'm here to assist you.",
                        "I know it’s a little overwhelming. Let’s take a break and then continue organizing the medication.",
                        "Let’s skip the current step and continue."]
				},
                "Excellent work, ParticipantName! You've successfully organized your medicine for both bottles.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'This is the end of the task. Thank you. Thank you for your work.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like to take a break between tasks?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "OptionalSay: Great. Let's move on to the next task.": {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},
            
            'pass5' : {
                'ParticipantName, I will play a radio announcement for you. I want you to listen to the announcement and then tell me what it was about.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like the instructions repeated?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: I will play a radio announcement for you. Please listen to it and then tell me what it was about. Is that clear, ParticipantName?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Give me one second to play the radio.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Can you tell me what the announcement was about?': {
                    'RemindSupport':[
                        "That's alright, ParticipantName. Let's listen to the announcement again.",
                        "Can you tell me just one thing you heard in the announcement?",
                        "That's okay, ParticipantName. Did they say anything about tuna in the announcement?",
                        "ParticipantName, the announcement was about a recall of chunk tuna. Can you recall anything about the announcement?"],
   					'Redirect':[
                           "Would you like some help?",
                           "Would you like the announcement to be louder?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'Great job, ParticipantName! I appreciate your effort in understanding the announcement.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Tell me one thing you might do after hearing that announcement.': {
                    'RemindSupport': [
                        'Is there anything you would do after hearing that announcement? What would you do if you bought bad tuna?'],
   					'Redirect':[
                           'Do you need any help?',
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                "OptionalSay: That's a thoughtful response. Thank you.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Alright, thank you.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'This is the end of this task. Thank you.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Do you want a break or some water before the next task?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Great. Let’s proceed to the next task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},

			'pass6' : {
                'ParticipantName, here is a newspaper article. Please take a few minutes to read it': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Can you tell me what the article was about?': {
                    'RemindSupport':[
                        'ParticipantName, You can read the article again.',
                        "The article was about power outages. Tell me one other thing about the article.",
                        "It's okay if the article is hard to read or understand. Let's try reading it together. The researcher will read a sentence, and then you can read the next one."],
   					'Redirect':[
                           "Here, the researcher can help you hold the newspaper.",
                           "Can I help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Well done, ParticipantName. You understood the main points of the article.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'If you read this article in your local paper, and this happened to you, what is one thing you might do?': {
                    'RemindSupport':[
                        "Let's talk about the article more. What part of it stood out to you the most? Maybe we can think of a response together. "],
   					'Redirect':[
                           "Can I help, ParticipantName?",
                           "ParticipantName, if you want, feel free to go through the article again.",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                "OptionalSay: That's a good suggestion, ParticipantName! I can see you've thought about how this article might influence your actions.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Thank you for sharing your thoughts on that. You had a good idea.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "You successfully completed this task, ParticipantName, and I'm proud of your efforts. ": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like to take a break and then continue?': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Great. Let’s move on to the next task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Nicely done. We can now proceed with the next task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},
            
            'pass7' : {
                "Now, ParticipantName, let’s play a game of BINGO. ": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Here is your BINGO card and marker.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'The researcher has a card too.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'You can win by getting 5 numbers in a row: down, across, diagonal, or 4 corners. ': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "Call 'BINGO' when you get a winning row.": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like the instructions repeated? Would you like the instructions to be louder?': {
                    'RemindSupport':[
                        "ParticipantName, we will play a BINGO game. Please mark the numbers on your card when they are called. You can win by getting a row of five numbers.",
                        "The BINGO card has columns labeled B, I, N, G, and O. Each column has many numbers. Let's go over the columns and their numbers to help you understand better."],
   					'Redirect':[]
                },
                'Before we begin our Bingo game, folks, remember to mark the FREE spaces.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Ready to start, ParticipantName?!': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'SlowSpeed: B 3. B 3.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: You marked that number very quickly. Well done!': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'SlowSpeed: O 71. O 71.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: N 39. N 39.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                "OptionalSay: You're doing a great job following along, ParticipantName!": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'SlowSpeed: G 57. G 57.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: I 26. I 26.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: B 8. B 8.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                "OptionalSay: I can see you're really focused, ParticipantName. Keep up the good work!": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'SlowSpeed: O 69. O 69.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: I 30. I 30.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Good job marking the numbers, ParticipantName!': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'SlowSpeed: N 34. N 34.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: B 11. B 11. ': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: N 43. N 43.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: O 64. O 64.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: G 54. G 54. ': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: N 42. N 42. ': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                'SlowSpeed: B 12. B 12.': {
                    'RemindSupport':[
                        "ParticipantName, just use the marker to cover the number on your card when it is called. Do it like the researcher does. ",
                        "Do you want me to say the numbers again?",
                        "Do you want the researcher to help you find the numbers on the card? We can look for them together."],
   					'Redirect':[
                           "Do you want the volume louder? ",
                           "Should we slow down?",
                           "Do you need any help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue. Would you like some water?",
                           "Let’s skip the current step and continue."]
                },
                "That’s it for this task. Well done, ParticipantName! Thank you. ": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                "Great. Thank you. We can now proceed with the next task.": {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			},
			
			'pass8' : {
                "Next, ParticipantName, you are going to make a sandwich. ": {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Use at least two items. Please clean up whatever you use. ': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'First, please take a plate from the table to start making your sandwich. The bread, cheese, meat, vegetables, and condiments are in the lunch bag. ': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Choose at least two items to put on your sandwich. You can pick from cheese, meat, vegetables, and condiments. ': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Would you like me to repeat the instruction?': {
                    'RemindSupport':[
                        "Remember, you need to choose at least two items for your sandwich. You can pick from cheese, meat, vegetables, and condiments. ",
                        "So far, you have chosen one thing; would you like to add anything else?",
                        "Let’s see what else we can add to make the sandwich even more delicious. We want at least two items."],
   					'Redirect':[
                           "Can I help?",
                           "I know it’s a little overwhelming. Let’s take a break and then continue.",
                           "Let’s skip the current step and continue."]
                },
                'OptionalSay: Great job, ParticipantName.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'OptionalSay: Wonderful choice.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Enjoy your sandwich now, or use a Ziplock bag to take it with you.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'Please clean up the area after you are done.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'You can put the unused ingredients back into the lunch bag. Afterwards, please wipe down the table using the wipes provided.': {
                    'RemindSupport':[
                        "Let’s clean up together. First, we’ll put the unused ingredients back into the lunch bag. Then, we can wipe the table with the wipes provided. "],
   					'Redirect':[
                           "Do you need any help?"]
                },
                'Thank you for cleaning up, ParticipantName.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'We have couple of questions for you regarding this task.': {
                    'RemindSupport':[],
   					'Redirect':[]
                },
                'This is the end of all the tasks. Thank you, ParticipantName, for your effort and participation. You did an excellent job!  ': {
                    'RemindSupport':[],
   					'Redirect':[]
                }
			}

		}