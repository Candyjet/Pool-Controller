from flask import Flask, render_template, request, redirect, url_for
import threading
from time import sleep
from gpiozero import LED

threadLock = threading.Lock()
intervals = []
currentSpeed = '1:42'

changeTimeInitial = 0.45
changeTimeDeltaPerStep = 0.62
stepsPerBatch = 3
batchBreakTime = .8

gpioPinFaster = LED(17)
gpioPinSlower = LED(23)

speeds = ['1:14', '1:15', '1:16', '1:17', '1:18', '1:19', '1:20',
          '1:21', '1:22', '1:23', '1:24', '1:25', '1:26', '1:27', '1:28',
          '1:31', '1:35', '1:38', '1:42', '1:46', '1:50', '1:54',
          '1:59', '2:03', '2:08', '2:13', '2:19', '2:29', '2:41',
          '2:55', '3:12', '3:25', '3:41', '3:59', '4:20', '4:31',
          '4:43', '4:55', '5:09', '5:24', '5:31' ]

def buttonTimeForSteps(steps):
    return changeTimeInitial + changeTimeDeltaPerStep * steps

def toSeconds(readable):
    parts = readable.split(':')
    return (int)(parts[0]) * 60 + (int)(parts[1])

def minSec(dict, tag):
    return '{}:{}'.format(dict[tag + 'Minutes'], dict[tag + 'Seconds'])

def changeSpeed(newSpeed):
    print("Changing speed to " + newSpeed)
    threadLock.acquire()
    global currentSpeed
    currentIndex = speeds.index(currentSpeed)
    print("current speed {} index {}".format(currentSpeed, currentIndex))
    newSpeedInSeconds = toSeconds(newSpeed)
    for x in range(0, len(speeds) - 1):
        if toSeconds(speeds[x]) >= newSpeedInSeconds:
            break
    newIndex = x
    waited = 0
    while newIndex != currentIndex:
        steps = min(abs(currentIndex - newIndex), stepsPerBatch)
        buttonTime = buttonTimeForSteps(steps)
        if newIndex < currentIndex:
            pin = gpioPinFaster
            indexDelta = -steps
            print("faster")
        else:
            pin = gpioPinSlower
            indexDelta = steps
            print("slower")
        print("changing steps: " + str(newIndex - currentIndex))
        print("holding button {} for {}".format(pin, buttonTime))
        pin.on()
        sleep(buttonTime)
        waited += buttonTime
        pin.off()
        currentIndex += indexDelta
        if (newIndex != currentIndex):
            print("waiting for {} before next batch".format(batchBreakTime))
            sleep(batchBreakTime)
            waited += batchBreakTime
    currentSpeed = speeds[newIndex]
    threadLock.release()
    print("current speed {} index {}".format(currentSpeed, newIndex))
    return (int)(waited + .9)

class WorkoutThread(threading.Thread):
  def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
  def run(self):
      print ("Starting " + self.name)
      threadLock.acquire()
      global intervals
      print(intervals)
      n = len(intervals)
      threadLock.release()
      for i in range(0, n):
          threadLock.acquire()
          if len(intervals) <= i:
              threadLock.release()
              print ("Exiting " + self.name)
              return
          if i:
            intervals[i - 1]['current'] = False
          intervals[i]['current'] = True
          interval = intervals[i]
          threadLock.release()
          print(interval)
          timeLeft = toSeconds(interval['duration'])
          timeLeft -= changeSpeed(interval['speed'])
          while timeLeft > 0:
              sleep(1)
              timeLeft -= 1
              if not timeLeft % 5:
                  print(timeLeft)
              threadLock.acquire()
              if len(intervals) <= i:
                  threadLock.release()
                  print ("Exiting " + self.name)
                  return
              threadLock.release()              
      threadLock.acquire()
      intervals = []
      threadLock.release()
      print ("Exiting " + self.name)


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    threadLock.acquire()
    if len(intervals):
        ret = render_template('workout.html', intervals=intervals, currentSpeed=currentSpeed)
    else:
        parts = currentSpeed.split(':')
        speed = {'minutes' : parts[0], 'seconds' : parts[1]}
        ret = render_template('pool.html', speed = speed)
    threadLock.release()
    return ret

@app.route('/stop')
def stop():
    threadLock.acquire()
    # Signal existing workout threads (if any) to stop.
    global intervals
    intervals = []
    threadLock.release()
    return redirect(url_for('index'))
    
@app.route('/workout', methods=['POST'])
def workout():
    workDur = minSec(request.form, 'workDuration')
    workSpeed = minSec(request.form, 'workSpeed')
    restDur = minSec(request.form, 'restDuration')
    restSpeed = minSec(request.form, 'restSpeed')

    global intervals
    global currentSpeed
    global changeTimeInitial
    global changeTimeDeltaPerStep
    global stepsPerBatch
    global batchBreakTime
    changeTimeInitial = (float)(request.form['initial']) / 100
    changeTimeDeltaPerStep = (float)(request.form['delta']) / 100
    stepsPerBatch = (int)(request.form['batchSteps'])
    batchBreakTime = (int)(request.form['batchBreakTime']) / 100

    threadLock.acquire()

    # Signal existing workout threads (if any) to stop.
    intervals = []
    threadLock.release()
    sleep(1)
    
    threadLock.acquire()
    currentSpeed = minSec(request.form, 'currentSpeed')
    intervals = []
    for i in range(0, (int)(request.form['intervals'])):
        interval = {'type':'Work',
                    'current': False,
                    'duration': workDur,
                    'speed': workSpeed}
        intervals.append(interval)
        interval = {'type':'Rest',
                    'current': False,
                    'duration': restDur,
                    'speed': restSpeed}
        intervals.append(interval)
    print(intervals)
    threadLock.release()
    thread = WorkoutThread(1, "Thread-1")
    thread.start()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
