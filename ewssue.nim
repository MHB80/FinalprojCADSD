import ui
proc main*() = 
    var mainwin :Window
    var menu  =newMenu("Help")
    menu.addItem("About",proc()= 
        msgBox(mainwin,"Authors","This programe is created by: \n\tMohammadHassanBarati\n\tHamidRezaBolouriKashani")
        )
    mainwin =newWindow("scheme",500,250,true)
    mainwin.onClosing = (proc (): bool = return true)
    let box = newVerticalBox(true)
    mainwin.setChild(box)
    let hbox = newHorizontalBox()
    hbox.padded=true
    box.add(hbox,true)
    #creating 3 groups each will be in one third of the window
    # they are leftgroup,middlegroup and right group in this order

        # left group
    var leftgroup = newGroup("ewstosue")
    leftgroup.margined=true
    hbox.add(leftgroup,true)
    var ewstosue = newVerticalBox(true)
    leftgroup.child=ewstosue
    var ewstarget=newEntry("target directory")
    ewstosue.add(ewstarget)
    ewstosue.add(newButton("find the file",proc()=
        let filename = ui.openFolder(mainwin)
        if filename.len == 0:
            msgBoxError(mainwin, "No file selected", "")
        else:
            ewstarget.text=filename
            
    )
    )
    ewstosue.add newHorizontalSeparator()
    # your code will be here
    ewstosue.add(newButton("Convert to Sue",proc() = 
        msgBox(mainwin,"Convertion Log","= > outcome")
        ))
        # middle group
        #there sholud be a picture here
    # var picture = newVerticalBox(true)
    # hbox.add(picture,true)

        # right group
    # var rightgroup = newGroup("suetoews")
    # rightgroup.margined=true
    # hbox.add(rightgroup,true)
    # var suetoews = newVerticalBox(true)
    # rightgroup.child=suetoews
    # var suetarget=newEntry("target directory")
    # suetoews.add(suetarget)
    # suetoews.add(newButton("find the file",proc()=
    #     let filename = ui.openFolder(mainwin)
    #     if filename.len == 0:
    #         msgBoxError(mainwin, "No file selected", "")
    #     else:
    #         suetarget.text=filename
    # )
    # )
    # suetoews.add newHorizontalSeparator()
    # suetoews.add(newButton("Convert to ews",proc() = 
    #     msgBox(mainwin,"Convertion Log","= > outcome")
    #     ))

        
    show(mainwin)
    mainLoop()
init()
main()