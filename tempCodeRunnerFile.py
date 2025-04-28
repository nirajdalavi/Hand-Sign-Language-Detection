
def hold():
    label_widget.destroy()

button1 = Button(app, text="Start detecting!", command=asl)
button1.pack()



button3= Button(app,text="stop",command=hold)
button3.pack()
app.mainloop()