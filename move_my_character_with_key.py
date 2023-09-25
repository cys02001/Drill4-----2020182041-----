from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running, rl, ud,x, y, movement
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type ==  SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x= x + 10
                rl += 1
                movement = 1
            elif event.key == SDLK_LEFT:
                x = x- 10
                rl -= 1
                movement = 2
            elif event.key == SDLK_UP:
                y = y + 10
                ud += 1
                movement = 0
            elif event.key == SDLK_DOWN:
                y = y - 10
                ud -= 1
                movement = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                rl -= 1
            elif event.key == SDLK_LEFT:
                rl += 1
            elif event.key == SDLK_UP:
                ud -= 1
            elif event.key == SDLK_DOWN:
                ud += 1

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
rl =  0
ud = 0
movement = 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    new_x = x + rl * 5
    new_y = y + ud * 5

    if new_x < 0:
        new_x = 0
    elif new_x > TUK_WIDTH:
        new_x = TUK_WIDTH
    if new_y < 126:
        new_y = 126
    elif new_y > TUK_HEIGHT - 126:
        new_y = TUK_HEIGHT - 126

    x = new_x
    y = new_y

    character.clip_draw(frame * 126, movement * 126, 126, 126, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    x += rl * 5
    y += ud * 5
    delay(0.05)
close_canvas()
