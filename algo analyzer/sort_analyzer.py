import pygame
from pygame.constants import KEYDOWN, K_b
from pygame.locals import *

pygame.init()

bg = (200,200,200)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

# Screen/Window 
win = pygame.display.set_mode((800,600))
screen = pygame.Surface((800,600))
pygame.display.set_caption("Sorting Algorithms")
base_font = pygame.font.Font(None,32)
user_entry = ""

# Instructions
instructions = base_font.render('Enter numbers separated by commas, press Enter, click on sort algorithm', True, black, red)
instRect = instructions.get_rect()
instRect.center = (400, 500)

# User input surface
input_rect = pygame.Rect(200, 400, 140, 32)
color = pygame.Color('lightskyblue3')

x = 40
y = 40

width = 20
height = [0]

clicked = False
counter = 0

# Defines uniformed button objects
class button():
    button_col = (25,190,225) 
    hover_col = (75,225,255)
    click_col = (50,150,255)
    text_col = (255,255,255)
    width = 180
    height = 40

    def __init__(self,x,y,text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False

        pos = pygame.mouse.get_pos()

        button_rect = Rect(self.x,self.y, self.width, self.height)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] ==1:
                clicked = True
                pygame.draw.rect(win, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(win, self.hover_col, button_rect)
        else:
            pygame.draw.rect(win, self.button_col, button_rect)

        pygame.draw.line(win, white, (self.x, self.y), (self.x + self.width, self.y), 2 )
        pygame.draw.line(win, white, (self.x, self.y), (self.x, self.y + self.height), 2 )
        pygame.draw.line(win, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2 )
        pygame.draw.line(win, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2 )

        text_img = base_font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        win.blit(text_img,(self.x + int(self.width / 2) - int(text_len / 2), self.y + 5))
        return action


# Draws bar graph of number array
def show(alist):
    
    for i in range(len(alist)):
        pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, alist[i]))

# Updates screen
def display(array, duration):

    win.fill((black))
    win.blit(win, (0,0))
    show(array)
    pygame.time.delay(duration)
    pygame.display.update()

# Sorting algorithms

def bubbleSort(alist):
    
    for i in range(len(alist)- 1):
                for j in range(len(alist) -i - 1):
                    if alist[j] > alist[j + 1]:
                        t = alist[j]
                        alist[j] = alist[j + 1]
                        alist[j + 1] = t

                    display(alist, 200)


def selectionSort(alist):
    
    swaps = True
    while swaps:
        switch = 0
        for i in range(len(alist)):
            min = i
            for j in range(i+1, len(alist)):
                if alist[min] > alist[j]:
                    min = j
                    switch += 1   

                    alist[i], alist[min] = alist[min], alist[i]

                    display(alist, 300)  

        if switch == 0:
            swaps = False
        

def heapify(array, n, i):

    large = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and array[large] < array[l]:
        large = l

    if r < n and array[large] < array[r]:
        large = r

    if large != i:
        array[i], array[large] = array[large], array[i]

        display(array, 500)

        heapify(array,n,large)


def heapSort(array):

    n= len(array)

    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    
    display(array, 300)


def merge(arr, start, m, end):
    
    s = start
    mid = m+1
    temp = []

    for i in range(start, end+1):
        if s > mid:
            temp.append(arr[mid])
            mid += 1
        elif mid > end:
            temp.append(arr[s])
            s += 1
        elif arr[s] < arr[mid]:
            temp.append(arr[s])
            s += 1
        else:
            temp.append(arr[mid])
            mid += 1

    for s in range(len(temp)):
        arr[start] = temp[s]
        start += 1

 
def mergeSort(arr, start, end):
    
    if start < end:
 
        m = start+(end-start)//2
 
        mergeSort(arr, start, m)
        mergeSort(arr, m+1, end)
        merge(arr, start, m, end)

        display(arr, 300)

    display(arr, 300)
    
# Sorting selection buttons
bubble = button(20,540,'BubbleSort')
selection = button(210,540,'SelectionSort')
heap = button(400,540,'HeapSort')
mergeS = button(590,540,'MergeSort')

run = True

while run:

    execute = False
    pygame.time.delay(30) 
    win.blit(instructions, instRect)
    pygame.display.update()

    if bubble.draw_button():
        bubbleSort(height)
    if selection.draw_button():
        selectionSort(height)
    if heap.draw_button():
        heapSort(height)
    if mergeS.draw_button():
        mergeSort(height,0,len(height)-1)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                execute = True
            elif event.key == pygame.K_BACKSPACE:
                user_entry = user_entry[:-1]
            else:
                user_entry += event.unicode
            
        if execute == False:
            
            win.fill((black))
            show(height)
            pygame.display.update()

        else:

            height = list(map(int, user_entry.split(",")))   
                    

    pygame.draw.rect(win, color, input_rect, 2)
    text_surface = base_font.render(user_entry, True, (255,255,255))
    win.blit(text_surface, (input_rect.x+ 5, input_rect.y + 5 ))
    input_rect.w = max(100, text_surface.get_width() + 10)
    pygame.display.flip()
    clock.tick(300)

pygame.quit()


