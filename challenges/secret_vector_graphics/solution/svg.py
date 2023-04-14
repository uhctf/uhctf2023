import svgwrite
import random

text_r1 = '''According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
Yellow, black. Yellow, black. Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.
Barry! Breakfast is ready!
Coming!
Hang on a second.
Hello?
Barry?
Adam?
Can you believe this is happening?
I can't.
I'll pick you up.
Looking sharp.
Use the stairs, Your father paid good money for those.
Sorry. I'm excited.
Here's the graduate.
We're very proud of you, son.
A perfect report card, all B's.
Very proud.
Ma! I got a thing going here.
You got lint on your fuzz.
Ow! That's me!
Wave to us! We'll be in row 118,000.'''.lower().replace(' ', '_')
text_r1_count = 0

text_r2 = '''the world we live in. it's so... wonderous. mysterious. even magical. no... no no no.. not that world. i meant this one. the smartphone. each system and program app is it's own little planet of perfect. technology. all providing services so necessary, so crucial, so unbelievably profound. look who just sent me a text! addie mccallister? it must be a mistake. or a joke. or a scam! don't send her your social security number. she's right there! that's our user, alex. and, like every freshman in high school, his whole life, everything, revolves around his phone. and, because the pace of life gets, faster and faster... phones down in five. and attention spans get shorter and shorter... and... you're probably not even listening to me right now. who has the time to type out actual words?'''.lower().replace(' ', '_')
text_r2_count = 0

text_g1 = 'The flag is hidden in plain sight, but you might need to focus on a singular colour.'.lower().replace(' ', '_')
text_g1_count = 0

text_g2 = 'uhctf{3d_goggles_could_have_helped}'.lower().replace(' ', '_')
text_g2_count = 0

text_b1 = '''void main(void)/* This really IS void, no error here. */
{   /* The startup routine assumes (well, ...) this */
/*
 * Interrupts are still disabled. Do necessary setups, then
 * enable them
 */time_init();tty_init();trap_init();sched_init();buffer_init();hd_init();sti();move_to_user_mode();
 if (!fork()) {  /* we count on this going ok */
  init();
 }
/*
 *   NOTE!!   For any other task 'pause()' would mean we have to get a
 * signal to awaken, but task0 is the sole exception (see 'schedule()')
 * as task 0 gets activated at every idle moment (when no other tasks
 * can run). For task0 'pause()' just means we go check if some other
 * task can run, and if not we return here.
 */
 for(;;) pause();
}'''.lower().replace(' ', '_')
text_b1_count = 0

text_b2 = 'Sometimes, you might encounter a red{flag}'.lower().replace(' ', '_')
text_b2_count = 0

# print(text_b)

doc_x = 800
svg_document = svgwrite.Drawing(filename = "secrets.svg",
                                size = ("800px", "1800px"))

text_x = 0
text_y = 20
offset = 20

text = ''
choices = {
    'r1': [text_r1, text_r1_count],
    'r2': [text_r2, text_r2_count],
    'g1': [text_g1, text_g1_count],
    'g2': [text_g2, text_g2_count],
    'b1': [text_b1, text_b1_count],
    'b2': [text_b2, text_b2_count],
}
last_choice = ''

while len(choices) > 0:
    c = random.choice(list(choices.keys()))
    tc = choices[c]
    
    if tc[1] >= len(tc[0]):
        del choices[c]
    else:
        cc = tc[0][tc[1]]
        if (len(text) == 0 or last_choice == c or text[-1] != cc):
            text += cc
        tc[1] += 1
    
    last_choice = c

text = ''.join(text)

text_count = 0
text_r1_count = 0
text_r2_count = 0
text_g1_count = 0
text_g2_count = 0
text_b1_count = 0
text_b2_count = 0

while text_count < len(text) and \
        (text_r1_count < len(text_r1) or \
         text_r2_count < len(text_r2) or \
         text_g1_count < len(text_g1) or \
         text_g2_count < len(text_g2) or \
         text_b1_count < len(text_b1) or \
         text_b2_count < len(text_b2) ):


    c = text[text_count]
    text_count += 1

    col_r1 = '0'
    col_r2 = '0'
    col_g1 = '0'
    col_g2 = '0'
    col_b1 = '0'
    col_b2 = '0'

    if text_r1_count < len(text_r1):
        if c == text_r1[text_r1_count]:
            col_r1 = 'F'
            text_r1_count += 1

    if text_r2_count < len(text_r2):
        if c == text_r2[text_r2_count]:
            col_r2 = 'F'
            text_r2_count += 1

    if text_g1_count < len(text_g1):
        if c == text_g1[text_g1_count]:
            col_g1 = 'F'
            text_g1_count += 1
    
    if text_g2_count < len(text_g2):
        if c == text_g2[text_g2_count]:
            col_g2 = 'F'
            text_g2_count += 1

    if text_b1_count < len(text_b1):
        if c == text_b1[text_b1_count]:
            col_b1 = 'F'
            text_b1_count += 1
    
    if text_b2_count < len(text_b2):
        if c == text_b2[text_b2_count]:
            col_b2 = 'F'
            text_b2_count += 1

    svg_document.add(svg_document.text(c,
                                   insert = (text_x, text_y),
                                   fill='#' + col_r1 + col_r2 + col_g1 + col_g2 + col_b1 + col_b2))
    text_x += offset
    if text_x >= doc_x:
        text_x = 0
        text_y += offset

print('r1:', text_r1_count, '/', len(text_r1))
print('r2:', text_r2_count, '/', len(text_r2))
print('g1:', text_g1_count, '/', len(text_g1))
print('g2:', text_g2_count, '/', len(text_g2))
print('b1:', text_b1_count, '/', len(text_b1))
print('b2:', text_b2_count, '/', len(text_b2))

#print(svg_document.tostring())
svg_document.save()
