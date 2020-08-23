I've noticed I mostly only have problems with the larger projects, 
because I think I don't always know where to start.  Do you have any
tips or tricks?  On slack, someone pointed out that in section 48
there's exercises on Problem Solving Patterns and Whiteboarding - do you
think it might be a good idea to jump to that section and then return to
python?
_________________________________________________________________________

surveyAppQuestions
You'll see that I uploaded 3 versions of app.py.  app.py is without session,
appSession.py is my version with session, and then appSolution was the provided
solution. 

1. Along with providing surveys.py - They gave us the directions:
Play with the satisfaction_survey in ipython to get a feel for how it works: 
it is an instance of the Survey class, and its .questions attribute is a list 
of instances of the Question class. You’ll need to understand this structure well, 
so don’t move on until you feel comfortable with it.

I could get to the title and the instructions, but the questions attribute returns:
[<__main__.Question at 0x7fa8f8077850>,
 <__main__.Question at 0x7fa8f8077910>,
 <__main__.Question at 0x7fa8f80776d0>,
 <__main__.Question at 0x7fa8f8077d30>]

satisfaction_survey.questions[0] returns <__main__.Question at 0x7fa8f8077850>
Yet in the solution they use "question = survey.questions[qid]"
I'm confused on how you actually access the questions themselves.

2. Could we go over session in some detail?
I wasnt sure why they made: RESPONSES_KEY = "responses"

and later in the /answers route why they were able to do:
    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses
whereas I needed to wrap responses in quotes:
    responses = session['responses']
    responses.append(choice)
    session['responses'] = responses
