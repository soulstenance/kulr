## kulr
### A simple Python color library using ANSI escape sequences to spruce up your Python scripts with ease
I'm just messing around and learning Python. While there are surely better options for color formatting, feel free to give this a try and leave any feedback you have!

#### License Notice
This library is licensed under MIT and is provided as-is with no guarantee of suitability for a particular purpose. Use at your own risk. A copy of the license should accompany this library so you can always know your rights and responsibilities.

#### How to use
This script, once imported to your project using `import kulr` or `import kulr as custom_alias` is pretty straight forward.

**Colors**  
You can use the following colors in this library: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan` and `white`.

**Text Colors**  
By default , you will change the text color by using the above colors. There are also bright variants of each color - simply prefix it with `b`. For example, bright blue would be `bblue`.

**Background colors**  
The colors can also be used for backgrounds. To do this just add `_bg` to the end. For example, a green background would be `green_bg`. You can combine this with the aforementioned `b` prefix for a brighter background color.

**Additional formatting**  
Kulr comes with some additional non-color related options which can be combined with other options for a more customized look. Please note that some terminals may not support all options or display them in an expected way.  
`bold` - Makes the text bold  
`dim` - Dims the text  
`italic` - Puts text in italics  
`under` - Underlines text  
`blink` - Makes the text blink  
`blink2` - Also makes blinking text (Unsure if this is different from the above option in some terminals)  
`reverse` - Reverses the background and text color  
`conceal` - Hides text but it can still be copied out and pasted  

**Usage**  
Please reference the example Python script for more details. After importing, to use a color in your script, you simply need to call the desired variable from the library. For example, `kulr.cyan` would call the variable to make your text cyan. When finished, it is best practice to reset your text with `kulr.reset`.
