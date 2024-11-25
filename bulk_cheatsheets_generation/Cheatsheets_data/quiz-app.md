### Quiz App

In this assignment, let's build a Quiz application by applying the concepts we have learned so far.

#### Reference

[https://s3.ap-south-1.amazonaws.com/new-assets.ccbp.in/frontend/loading-data/quizapp_v3neqz.mp4](https://s3.ap-south-1.amazonaws.com/new-assets.ccbp.in/frontend/loading-data/quizapp_v3neqz.mp4)

#### Functionalities to be Achieved:

- Show a friendly welcome screen with quiz name, what it's about, how many questions there are, time limits, how hard it is, and a big **Start** button
- Build a quiz screen that shows how far along you are, a countdown timer, how many answers you got right and wrong, and dots to show which question you're on
- Show each question with its topic, answer choices that turn green if correct or red if wrong, and an explanation of the right answer
- Let users move between questions using **Previous** and **Next** buttons (Next button stays disabled until an answer is selected), clicking the question dots, and navigation is restricted until an answer is chosen
- When timer runs out without any selection, it auto-selects wrong answer, disables all options, and waits for user to click Next button to proceed
- Display final results with a trophy icon, your score, what percentage you got right, how long it took, and a nice message about how well you did
- Add a **Review** button that shows all questions again with what you answered, what was correct, and why each answer was right or wrong
- Make a timer that turns red and blinks when only 3 seconds are left, locks all options when time runs out (only Next button remains active), and keeps track of total quiz time
- Question Object Format (For Reference):

```

const questionFormat = {
    question: "What is HTML?",    // Question text
    topic: "HTML Basics",         // Question topic
    options: ["option1", "option2"], // Answer choices
    correct: 0,                   // Index of correct answer
    explanation: "HTML is..."     // Answer explanation
}

```


#### Submission Instructions

- Publish your project as a code snippet in learning portal or any other deployment platform
- Submit your project in this [form]()

### Highlight Your Technical Excellence!

<MultiLineNote>
<div style="display: flex; flex-wrap: wrap; gap: 40px; padding: 30px; background: linear-gradient(to right, #f0f2f5, #ffffff); border-radius: 12px; max-width: 1200px; margin: 20px auto;">
    <div style="flex: 1 1 300px;">
        <h2 style="font-family: Arial, sans-serif; color: #0a66c2; margin: 0 0 15px 0; font-size: clamp(1.5rem, 4vw, 2.5rem);">Share on LinkedIn</h2>
        <p style="color: #666; line-height: 1.5;">Let your work speak for itself. Showcase your achievements and connect with professionals who share your passion.</p>
        <a href="https://www.linkedin.com" 
           style="display: inline-block; margin-top: 15px; padding: 10px 20px; background-color: #0a66c2; color: white; text-decoration: none; border-radius: 5px; font-family: Arial, sans-serif;">
            LinkedIn.com
        </a>
    </div>
    <div style="flex: 0 1 300px;">
        <img src="https://res.cloudinary.com/dpvbaiyus/image/upload/v1730870613/programmer-work-laptop-computer-website-code-program-concept_133260-5402_ffsbmo.avif" 
             style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" 
             alt="Programmer working on laptop">
    </div>
</div>
</MultiLineNote>
