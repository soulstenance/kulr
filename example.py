# First import the library
import kulr

# Then you can print, for example with f strings
print(f"{kulr.bold}{kulr.under}These are examples of how you can use my color library in your scripts.{kulr.reset}\n")
print(f"{kulr.yellow}Example yellow text.{kulr.reset}")
print(f"{kulr.green}{kulr.red_bg}Example green text with a red background.{kulr.reset}")
print(f"{kulr.byellow_bg}A bright yellow backround for your text.{kulr.reset}")
print(f"{kulr.byellow_bg}{kulr.black}Maybe make the text black for readability...{kulr.reset}")
print(f"{kulr.cyan}Perhaps cyan is more to your liking.{kulr.reset}")
print(f"{kulr.bold}{kulr.italic}{kulr.blue}You can combine certain options as well like this bold, italic, blue text.{kulr.reset}\n")

# Or even inputs like this
# Note the [end=""] argument ensures no new line is made
print("Please type some red text: ", end="")
print(kulr.red, end="")
input() # User input will now be red
print(f"{kulr.green}Good job!\n")
print("I hope you enjoy using my library!") # Note how this is still green because we didn't reset the formatting
