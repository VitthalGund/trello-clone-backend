# Coding Round

Hi there!

Thank you for your interest in applying for the Django Backend Developer position at IIT Bombay and welcome to the second round of the interview process. Here we’re looking to understand the candidate's thought process, coding ability, documentation and problem-solving skills.

You have 7 days(168 hours) from the receipt of this document to submit your designs through the forms [here](https://docs.google.com/forms/d/e/1FAIpQLScMN7IntaDklMKhE8F-JtgudP2RyFOBoo6vaLnGMf3OvIFxgg/viewform?usp=sf_link) with a Gmail login. 

***Please Note: Contents of this document are confidential. You are not allowed to share this document with the outside world.***


## Problem Statement

![Trello](https://d2k1ftgv7pobq7.cloudfront.net/meta/p/res/images/spirit/product/89d378b845766a8f0c48e955336266f8/board.png)


- Implement a simple api to model the [Trello](https://trello.com/) backend

- The API should be made in Django DRF and should have a browsable API.


The API should be able to handle the following

- Define and update users

- Basic User management - adding users, user login

- Define and update columns

- Define and update cards

- Each column will contain multiple cards

- Implement an efficient data structure to reduce the number of queries during reordering

### Add Card

- On clicking the add card button, the browsable API should show a form

- The form should contain a title, description, and column selection dropdown

- Title should be validated and should only contain alphabets.

- Description should be validated and should be a minimum of 25 characters.

- On submit, the card should be added to the end of the selected column.

### Edit Card

- On clicking a card, the browsable API should be shown with the add card form with the prefilled data.

- If the user changes the column then, the card should be added to the end of the selected column.

# Instructions

- Use the Django DRF library.

- The interface should have a browsable API. [Details](https://www.django-rest-framework.org/topics/browsable-api/)

- The codebase should be hosted in a public git repo.
- Share the screenshot of the browsable API for each endpoint and add it to a Demo folder in the git repo.

# Deliverables

- Link to the public git repo for this design exercise.
- Screenshots of the endpoints to be added in Demo folder in the repo.
- Documentation file detailing the design approach and choices used in the code design should also to be added in the git repo.

Deliverables must be submitted in 7 days(168 hours) from the receipt of this document via the forms [here](https://docs.google.com/forms/d/e/1FAIpQLScMN7IntaDklMKhE8F-JtgudP2RyFOBoo6vaLnGMf3OvIFxgg/viewform?usp=sf_link).

Candidates clearing this round will be intimated via email a couple of weeks after their submissions.

Note: We take plagiarism very seriously and hence please don't directly copy-paste code from somewhere else without linking it to the source or giving the source due credit. We will run the codebase through an internal plagiarism code checker during code evaluation. We know Code LLMs exist and it might get the job done faster, but you do miss out on the fun of pure coding. Its pretty easy to make out the code output from them. It’s your unique approach to problem-solving that we’re most interested in. So, gear up, trust your abilities, and happy coding!

PS: Some of you might think this coding round is trivial and easy. That’s intentional! Our goal is to gauge your understanding of the core fundamentals before we dive deeper in the subsequent stages of the interview. Remember, being a developer isn’t about writing the most intricate code. It’s about creating solutions that are efficient, maintainable, and address real-world problems - even if they seem mundane or basic at times. So please keep this in mind as you move forward.

### Good Luck!