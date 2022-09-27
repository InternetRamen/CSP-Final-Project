app.bg = Image("https://images.unsplash.com/photo-1504493408076-2017927bbb1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=600&q=80", -80, 0)
app.cr = Image("https://raw.github.com/InternetRamen/image/17c4b91ec69ada795243d71f63ed4a3e66811603/Kyouko_Hori_Anime_Design_2%20(1).png", 0, 0)

box = Group(
    Rect(40, 280, 320, 80, border="white"),
    Label("It's cold out! Let's go get some ramen.", 200, 320, fill="white", size=15)
    )
shape = Label("Click to move on, left and right to select option", 200, 380, fill="white")
app.scene = 1
lines = Group()
options = Group(
    Label("Give her a towel", 120, 340, fill="white", size=15),
    Label("Ignore her", 280, 340, fill="white", size=15),
    RegularPolygon(55, 340, 7, 3, fill="white", rotateAngle=90),
    )
    
options.visible = False
options.children[2].v = True
option2 = Group(
    Label("Tonkatsu Ramen", 120, 340, fill="white", size=15),
    Label("Broccoli Ramen", 280, 340, fill="white", size=15),
    RegularPolygon(55, 340, 7, 3, fill="white", rotateAngle=90),
    )
    
option2.visible = False
option2.children[2].v = True
# 55, 340, 230

app.towel = ""
def onMousePress(x,y):
    app.scene+=1

    if app.scene == 2:
        app.cr = Image("https://raw.github.com/InternetRamen/image/17c4b91ec69ada795243d71f63ed4a3e66811603/Kyouko_Hori_Anime_Design_2%20(2).png", 0, 0)
        for i in range(30):
                line = Line(0,0,4,4, fill="lightblue")
                line.centerX = randrange(0, 400)
                line.centerY = randrange(0, 400)
                lines.add(line)
        lines.toFront()
        box.toFront()
        box.children[1].value = "Oh no! It's raining. Quick, get inside!"
    elif app.scene == 3:
        for i in lines.children:
            i.visible = False
        app.bg = Image("https://images.unsplash.com/photo-1569096651661-820d0de8b4ab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80", 0, -200)
        app.cr.toFront()
        app.cr.centerY += 80
        box.toFront()
        box.children[1].value = "Aw man, I got so wet."
    elif app.scene == 4:
        options.visible = True
    elif app.scene == 5:
        options.visible = False
        if (options.children[2].v):
            box.children[1].value = "Thanks <3! ILY"
            app.cr =  Image("https://raw.github.com/InternetRamen/image/17c4b91ec69ada795243d71f63ed4a3e66811603/Kyouko_Hori_Anime_Design_2%20(1).png", 0, 80)
            app.towel = Rect(160,240, 80,80, fill="lightgray", border="gray")
            box.toFront()
        else:
            box.children[1].value = "Really... I'm so done. Don't call me back."
            app.cr.centerY -= 80
    elif app.scene == 6:
        if not options.children[2].v:
            lost()
        else:
            app.towel.visible = False
            box.children[1].value = "What ramen do you want?"
    elif app.scene == 7:
        option2.visible = True
    elif app.scene == 8:
        if option2.children[2].v:
            option2.visible = False
            box.children[1].value = "I love tonkatsu ramen too!"
        else:
            option2.visible = False
            app.cr = Image("https://raw.github.com/InternetRamen/image/17c4b91ec69ada795243d71f63ed4a3e66811603/Kyouko_Hori_Anime_Design_2%20(2).png", 0, 0)
            box.children[1].value = "WTF?! That's nasty."
            box.toFront()
    elif app.scene == 9:
        if not option2.children[2].v:
            lost()
        else:
            won()
    elif app.scene == -2:
        reset()
    shape.toFront()
def onKeyPress(key):
    if app.scene == 4:
        if key == "left":
            options.children[2].v = True
         
            options.children[2].centerX = 55
        elif key == "right":
            options.children[2].v = False
            
            options.children[2].centerX = 230
    elif app.scene == 7:
        if key == "left":
            option2.children[2].v = True
         
            option2.children[2].centerX = 55
        elif key == "right":
            option2.children[2].v = False
            
            option2.children[2].centerX = 210
def reset():
    app.bg = Image("https://images.unsplash.com/photo-1504493408076-2017927bbb1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=600&q=80", -80, 0)
    app.cr = Image("https://raw.github.com/InternetRamen/image/17c4b91ec69ada795243d71f63ed4a3e66811603/Kyouko_Hori_Anime_Design_2%20(1).png", 0, 0)
    
    box = Group(
        Rect(40, 280, 320, 80, border="white"),
        Label("It's cold out! Let's go get some ramen.", 200, 320, fill="white", size=15)
        )
    app.scene = 1
    options.visible = False
    for i in lines:
        lines.remove(i)
    options.children[2].centerX = 55
    options.children[2].v = True
    option2.children[2].centerX = 55
    option2.children[2].v = True
    
    
def lost():
    Rect(0,0,400,400)
    Label("You Lost!", 200,200, fill="white", size=30)
    app.scene = -3
def won():
    Rect(0,0,400,400)
    Label("You guys got married!", 200,200, fill="white", size=30)
    app.scene = -3 
