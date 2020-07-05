# FriendlyCareRobotics
The Friendly Care Robotics application was built in occasion of the 2020 [TIM Smart Spaces Hackathon](https://events.codemotion.com/hackathons/hackathon-tim-smart-spaces/home/) by team21.

## The challenge
#### **Topic 5: Care Residence**

> In che modo la tecnologia può avere un reale impatto sulle modalità di
> utilizzo degli spazi in cui ci prendiamo cura dei nostri cari?

In which way technology can have a real impact on the use of spaces in which we take care of our loved ones?

> Esploriamo il potenziale delle più moderne tecnologie nel contesto
> dell’assistenza a persone in difficoltà, anziani e disabili
> nell’ambito ospedaliero o dei servizi di health care.

Let's explore the potential of the most cutting-edge technologies within the context of assistance to people in need, the elderly and the disabled in an hospital setting or health care services.

## Our proposed solution
We've built an application that moves the robot autonomously in an environment. In this way, we can enable remote assistance that can be easily integrated with other applications, such as [Friendly Care](https://github.com/trajkd/FriendlyCare).

## Usage of APIs
In order to work properly, the web app needs to communicate with an API. 

 - [Cloud Robotics](https://5g-api-portal.telecomitalia.it/apiexposure/web/node/119) for robot movements.

***IMPORTANT*** Kindly replace the API key with your API key inside `command.py`

   
    headers = {
          # Replace with your API key
          'apikey': 'xyladasjdj23knw22oo2no2',
          'Content-Type': 'application/json'
       }

and inside `status.py`

    headers = {
      # Replace with your API key
      'apikey': 'xyladasjdj23knw22oo2no2'
    }

## Requirements
This application was written in Python. Make sure you have a version of Python 3 installed.

## Usage
Run `python command.py` to start the robot.

Run `python status.py` to check its status.
