### Password Generator

In this assignment, let's build a Password Generator application by applying the concepts we have learned so far.

#### Reference

[https://s3.ap-south-1.amazonaws.com/new-assets.ccbp.in/frontend/loading-data/password-generator_bv6zqv.gif](https://s3.ap-south-1.amazonaws.com/new-assets.ccbp.in/frontend/loading-data/password-generator_bv6zqv.gif)

#### Functionalities to be Achieved:

- Generate a new password when user moves the length slider (user can choose between 8 to 64 characters long password)
- Let users choose what to include in their password by selecting options:(uppercase letters: A-Z, lowercase letters: a-z, numbers: 0-9, symbols: !@#$%^&\*, spaces)
- If none of the options are selected, display a notification saying: **Please select at least one character type.**
- Show password strength using colored bars and text:

  - 1 Bar (Red) - **VERY WEAK**

    - Using only one type:

      - Only numbers (e.g., "123456789")
      - Only lowercase (e.g., "abcdefgh")
      - Only uppercase (e.g., "ABCDEFGH")
      - Only symbols (e.g., "@#$%&\*!")

  - 2 Bars (Orange) - **WEAK**

    - Using any two types:

      - Numbers + lowercase (e.g., "abc123def")
      - Numbers + uppercase (e.g., "ABC123DEF")
      - Lowercase + uppercase (e.g., "abcDEFghi")
      - Symbols + numbers (e.g., "123@#$456")

  - 3 Bars (Yellow) - **MEDIUM**

    - Using any three types:

      - Numbers + lowercase + uppercase (e.g., "abc123DEF")
      - Numbers + lowercase + symbols (e.g., "abc123@#$")
      - Uppercase + lowercase + symbols (e.g., "abcDEF@#$")

  - 4 Bars (Green) - **STRONG** Must meet ALL these conditions:

    - Using all four types together:

      - Numbers + lowercase + uppercase + symbols
      - Password length greater than 12 characters
      - Example: "abcDEF123@#$!"

- Ensure a password is generated when the **Generate Password** button is clicked, based on the selected options.
- Add a copy button that copies the password to clipboard (shows a checkmark icon for 1 second after copying)
- Save the last 5 passwords generated in a history section (each saved password can be clicked to copy it again)
- Create readable passwords when **Pronounceable** option is selected (example: "TropicalBird92!" instead of "Tj9#mK2$pL")
- Avoid confusing characters when **No Similar Characters** is checked (won't use: 1/l/I, 0/O, S/5 which look alike)
- Ensure no character repeats when **No Duplicates** is checked (example: "abcd123" is valid, "aabc123" is not)
- Show password length number as user moves the slider (displays current length like **12 characters**)
- Enable one-click password regeneration using refresh button (creates new password keeping all current settings)

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
