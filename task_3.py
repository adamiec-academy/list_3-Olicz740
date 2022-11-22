from random import randint

speed("slow")

step = 20
mount = [0, 10, 20, 45, 70, 90, 120, 125, 140, 180, 150, 130, 90, 75, 50, 30, 10, 0]
forward(len(mount))
backward(len(mount))
for i in range(len(mount)):
    if mount[i] <= 20:
        goto(step + i * step, mount[i])
    else:
        goto(step + i * step, mount[i] + randint(-20, 20))
forward(step)
for i in range(len(mount)):
    if mount[i] <= 20:
        goto(step + (len(mount) + i) * step, mount[i])
    else:
        goto(step + (len(mount) + i) * step, mount[i] + randint(-20, 20))

exitonclick()
