import turtle
minLen = 2
def build_tree(t, branch_length, shorten_by, angle):
  if branch_length > minLen:
    t.forward(branch_length)
    new_length = branch_length - shorten_by
    t.left(angle)

    build_tree(t, new_length, shorten_by, angle)
    t.right(angle*2)

    build_tree(t, new_length, shorten_by, angle)
    t.left(angle)
    t.backward(branch_length)

tree = turtle.Turtle()
#tree.hideturtle()
tree.setheading(90)
tree.color('red')
build_tree(tree, 50, 10, 30)
#turtle.mainloop()