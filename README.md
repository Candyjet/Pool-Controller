A modified Endless Pool Remote Controller.
Allows user-defined program, such as interval training, using a Raspberry Pi controlling the Remote Control






It is important to note a couple of things.

-1. This project is not, and is unlikely to ever be, waterproof. This may seem like a massive flaw, but in reality it is not. The Remote Controller, (RC) which is normally used from the pool, does not actually talk to the pool itself. It communicates with the whiney, hydraulic power pack, which supplies the pool with hydraulic pressure. You can see the little aerial sticking out of the hydraulic pack. 
When in use, I keep the Pi/RC combination inside. The RC is strong enough to transmit through walls. 

So, in use, this is how it works. You boot up the Pi (less than a minute). Start the interval program. I have set it to have a user-defined dormant period, to give time to prepare for swimming, and warm up in the pool. I have mine set for 20 minutes. It takes me 5-mins to get into the pool, then 15 mins of warm up. 

It then runs the interval program. The number and length of intervals is user-defined in the python program. You can set preferred defaults, or just choose options from the GUI interface. It will then 'press' the buttons on the RC for you, to run these intervals. 

NB you start and stop the pool using your normal pool controller. The Pi/RC only controls the speed during interval training. In addition, you can alter the speed as normal during your swimming session.

-2. The pool remembers your RC button presses even when SWITCHED OFF. An Endless Pool, when started, uses the speed that it was running at when last switched off. However, (and this baffled me for a while when testing the device), if you press the slower or faster buttons on a RC even when the pool is NOT running, when next switched on, the pool will run as if those buttons had been pressed when the pool was running.

What this means is this. When you are building this device, and say testing the 'faster' channel, when you next switch on the pool, the speed will go off like a rocket! I therefore recommend that, after testing your device with the pool off, press the 'slower' button on your RC, to reduce the pool speed to a reasonable rate when you next switch it on.

-3. What the device does. 
It simply shorts out, electronically, the wires connected to the slower/faster buttons.

Here's how to make the device. You need

A Raspberry Pi Model 2 or 3

A Spare Endless Pool RC

2 Resistors (180 Ohm)

2 Optocouplers (4N25 or 4N35)

A prototyping board with GPIO header
Some soldering skills.

How to Make it.

Firstly you need to remove the screws from the spare RC. You then carefully prise the board out, breaking small blue plastic legs holding the board in place. Then solder wires to each end of the buttons as shown in image contoller1.jpg.

You can test that you have the correct wires before soldering by simply shorting where you think the wires should go. A pair of metal scissors will do this for you, across the switch. The little blue light will light up on the RC. (Now remember point 2 above - you have now altered the starting speed of the pool next time!)

Solder 4 wires. One on each end of S1 and S2. To test your soldering, short out the wires across each switch, ie the wires connect to each end of S1 together. The blue LED will light if your soldering is good. Test S2 in the same way. Now put some insulating tape at the other end of the wires to prevent shorting and activating inadvertent button presses.

To survive robust handling, I put a dab of glue at the edge of the RC and glued the insulated wires to the controller at the edge. Soldering is not a mechanical joint!

The image Pool Wiring shows the correct soldering needed to the remote controller, using conventional colours, ie red for Positive, black for ground.

The image optocoupler wiring shows how to connect the optocoupler to both the remote controller at the top of the image, and the pi GPIO outputs at the bottom. Orientation of the optocoupler is given by the text written on them ie wire it with the writing as shown.

I have uploaded 2 programs running python3.

Newdemo is purely to test your wiring. If correct, the blue led on the remote will come on 4 times in total.
Newacg7 will run the program. The norm setting seems to be better than easy.  I am still adjusting the timing on the easy settings.

I have used GPIO ports 12 and 24 in the programs. Port 24 increases the speed of the pool. Port 12 decreases the speed.




