import random
import pygame
pygame.init()

# sets window dimensions and title
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mastermind")
rect_size = 40
rect_spacing = 60
count = 0

# set the colours (More colours can be added here when needed)
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Defines the font pygame will be using 
font = pygame.font.Font(None, 14)

#Variables
code = []  # the secret code to guess
colours = [red, green, blue, white]  # available colours for the code
all_guesses = []  # list of all guesses made by the player
guesses = []  # list of the current guess made by the player
num_guesses = 0  # number of guesses made by the player
max_guesses = 8  # maximum number of guesses allowed
all_correctpos = [] #list of the number of correct positions
all_correctcol = [] #list of the number of correct colours 

# generate a random code
for i in range(4):
    code.append(random.choice(colours))
print(code)

#Instructions
result_text = font.render("How to play:", True, white)
screen.blit(result_text, (0, 50))
result_text = font.render("Type 4 numbers (Red = 1, Green = 2, Blue = 3, White = 4. Then it will tell you how many you got right, Number of Blue Squares = Correct colour + position, Number of White Squares = Correct Colour but not position", True, white)
screen.blit(result_text, (0, 75))
pygame.display.flip()
pygame.time.delay(10000)  # pause for 10 seconds
screen.fill(black) #fills the screen with black to remove text
font = pygame.font.Font(None, 36) #Changes text size to bigger

# Infinite loop to allow the game to run until a condition is met, allowing for easy changing of things like win conditions and number of guesses 
running = True
while running:
    # check for events occurring such as the Quit event or Keydown event
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #Allows for the adding of a quit button (That I didn't quite get time to implement)
            running = False
        if count == 4:
          count = 0
        elif event.type == pygame.KEYDOWN:
            # allow the player to enter their guess by pressing the corresponding keys
            # this could also be implemented as a button
            count += 1 #keeps track of how many inputs you have made
            print(count) # should be in gui but kept on breaking
            if event.key == pygame.K_1:
                guesses.append(colours[0])
            elif event.key == pygame.K_2:
                guesses.append(colours[1])
            elif event.key == pygame.K_3:
                guesses.append(colours[2])
            elif event.key == pygame.K_4:
                guesses.append(colours[3])
            # check if the player has entered a complete guess
            if len(guesses) == 4:
                all_guesses.append(guesses)  # add the current guess to the list of all guesses
                # compare the player's guess to the secret code by counting each number of correct 
                #positions and colours for each row, and then appending it to a list for future use
                correct_positions = 0
                correct_colours = 0
                for i in range(4):
                    if guesses[i] == code[i]:
                        correct_positions += 1
                    elif guesses[i] in code:
                        correct_colours += 1
                all_correctpos.append(correct_positions)
                all_correctcol.append(correct_colours)
                if correct_positions != 4:
                    num_guesses += 1
                    guesses = []
    
                
                # displays the result to the player
                screen.fill(black)
                result_text = font.render("Correct positions: {}  Correct colours: {}".format(correct_positions, correct_colours), True, white) #Renders the text in an appropriate format
                screen.blit(result_text, (100, 100)) #Draws the rendered text onto the window
                pygame.display.flip()
                #If it is not correctly guessed, num of guesses had increases
                
    for i in range(len(all_guesses)):
      for j in range(4):
        pygame.draw.rect(screen, all_guesses[i][j], (100 + j * 50, 200 + i * 50, 50, 50)) 
        #Draws all the rows out each time, due to blacking out the screen each time. This is very inefficient 
        #This was done due to not knowing about how to do other methods until I had run out of time
    #Draws, nexto the guesses, the number of colours in the correct place 
      for j in range(all_correctpos[i]):
        pygame.draw.rect(screen, blue, (100 + 4 * rect_spacing + j * rect_spacing, 200 + i * 50, rect_size, rect_size))

    # Draws nexto the number in the correct place, the number with the correct colour but not place
      for j in range(all_correctcol[i]):
        pygame.draw.rect(screen, white, (100 + 4 * rect_spacing + all_correctpos[i] * rect_spacing + j * rect_spacing, 200 + i * 50, rect_size, rect_size))
        pygame.display.flip() #Updates display (which I should have used more often)

  # check if the player has won or lost the game and tells them accordingly 
      if correct_positions == 4:
        screen.fill(black)
        result_text = font.render("You won!", True, white)
        screen.blit(result_text, (100, 100))
        pygame.display.flip()
        pygame.time.delay(500)  # pause 
        running = False
      elif num_guesses == max_guesses:
        screen.fill(black)
        result_text = font.render("You lost!", True, white)
        screen.blit(result_text, (100, 100))
        pygame.display.flip()
        pygame.time.delay(500)  # pause
        screen.fill(black)
        #Draws what the correct guess was
        result_text = font.render("Correct Positions Are", True, white)
        screen.blit(result_text, (100, 100))
        for v in range(4):
          pygame.draw.rect(screen, code[v], (100 + v * 50, 200, 50, 50))
          pygame.display.flip()
          running = False
